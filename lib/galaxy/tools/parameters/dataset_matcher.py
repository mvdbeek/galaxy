from collections import defaultdict
from logging import getLogger
from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlalchemy import (
    alias,
    and_,
    any_,
    func,
    not_,
    or_,
    select,
)
from sqlalchemy.orm import (
    joinedload,
    object_session,
)
from sqlalchemy.orm.attributes import set_committed_value

import galaxy.model
from galaxy.model import (
    CollectionStateSummary,
    Dataset,
    DatasetCollection,
    DatasetCollectionElement,
    DatasetPermissions,
    HistoryDatasetAssociation,
    HistoryDatasetCollectionAssociation,
    ImplicitlyConvertedDatasetAssociation,
)

if TYPE_CHECKING:
    from galaxy.model import History

log = getLogger(__name__)


def set_dataset_matcher_factory(trans, tool):
    trans.dataset_matcher_factory = DatasetMatcherFactory(trans, tool)


def unset_dataset_matcher_factory(trans):
    trans.dataset_matcher_factory = None


def get_dataset_matcher_factory(trans):
    dataset_matcher_factory = getattr(trans, "dataset_matcher_factory", None)
    return dataset_matcher_factory or DatasetMatcherFactory(trans)


class DatasetMatcherFactory:
    """"""

    def __init__(self, trans, tool=None):
        self._trans = trans
        self._tool = tool
        self._data_inputs = []
        self._matches_format_cache = {}
        self._collection_summaries_cache: dict[tuple, tuple[dict[int, CollectionStateSummary], set[int]]] = {}
        if tool:
            valid_input_states = tool.valid_input_states
        else:
            valid_input_states = galaxy.model.Dataset.valid_input_states
        self.valid_input_states = valid_input_states
        can_process_summary = False
        if tool is not None:
            for input in tool.inputs.values():
                self._collect_data_inputs(input)

            require_public = self._tool and self._tool.tool_type == "data_destination"
            if not require_public and self._data_inputs:
                can_process_summary = True
                for data_input in self._data_inputs:
                    if data_input.options:
                        can_process_summary = False
                        break
        self._can_process_summary = can_process_summary

    def matches_any_format(self, hda_extension, formats):
        for format in formats:
            if self.matches_format(hda_extension, format):
                return True
        return False

    def matches_format(self, hda_extension, format):
        # cache datatype checking combinations for fast recall
        if hda_extension not in self._matches_format_cache:
            self._matches_format_cache[hda_extension] = {}

        formats = self._matches_format_cache[hda_extension]
        if format not in formats:
            datatype = galaxy.model.datatype_for_extension(
                hda_extension, datatypes_registry=self._trans.app.datatypes_registry
            )
            formats[format] = datatype.matches_any([format])

        return formats[format]

    def _collect_data_inputs(self, input):
        type_name = input.type
        if type_name == "repeat" or type_name == "upload_dataset" or type_name == "section":
            for child_input in input.inputs.values():
                self._collect_data_inputs(child_input)
        elif type_name == "conditional":
            for case in input.cases:
                for child_input in case.inputs.values():
                    self._collect_data_inputs(child_input)
        elif type_name == "data" or type_name == "data_collection":
            self._data_inputs.append(input)

    def dataset_matcher(self, param, other_values):
        return DatasetMatcher(self, self._trans, param, other_values)

    def batch_collection_summaries(self, session, history_id, collection_type_filter, visible_only):
        cache_key = (history_id, frozenset(collection_type_filter) if collection_type_filter else None, visible_only)
        if cache_key not in self._collection_summaries_cache:
            self._collection_summaries_cache[cache_key] = _batch_collection_summaries(
                session, history_id, collection_type_filter, self.valid_input_states, visible_only=visible_only
            )
        return self._collection_summaries_cache[cache_key]

    def dataset_collection_matcher(self, dataset_matcher):
        if self._can_process_summary:
            return SummaryDatasetCollectionMatcher(self, self._trans, dataset_matcher)
        else:
            return DatasetCollectionMatcher(self._trans, dataset_matcher)


class DatasetMatcher:
    """Utility class to aid DataToolParameter and similar classes in reasoning
    about what HDAs could match or are selected for a parameter and value.

    Goal here is to both encapsulate and reuse logic related to filtering,
    datatype matching, hiding errored dataset, finding implicit conversions,
    and permission handling.
    """

    def __init__(self, dataset_matcher_factory, trans, param, other_values):
        self.dataset_matcher_factory = dataset_matcher_factory
        self.trans = trans
        self.param = param
        self.tool = param.tool
        filter_values = set()
        if param.options and other_values:
            try:
                for v in param.options.get_options(trans, other_values):
                    filter_values.add(v[0])
            except IndexError:
                pass  # no valid options
        self.filter_values = filter_values

    def valid_hda_match(self, hda, check_implicit_conversions=True):
        """Return False if this parameter can not be matched to the supplied
        HDA, otherwise return a description of the match (either a
        HdaDirectMatch describing a direct match or a HdaImplicitMatch
        describing an implicit conversion.)
        """
        rval = False
        formats = self.param.formats
        direct_match, target_ext, converted_dataset = hda.find_conversion_destination(formats)
        if direct_match:
            rval = HdaDirectMatch(hda)
        else:
            if not check_implicit_conversions:
                return False
            if target_ext:
                original_hda = hda
                if converted_dataset:
                    hda = converted_dataset
                rval = HdaImplicitMatch(hda, target_ext, original_hda)
            else:
                return False
        if self.filter(hda):
            return False
        return rval

    def hda_match(self, hda, check_implicit_conversions=True, ensure_visible=True):
        """If HDA is accessible, return information about whether it could
        match this parameter and if so how. See valid_hda_match for more
        information.
        """
        dataset = hda.dataset
        valid_state = dataset.state in self.dataset_matcher_factory.valid_input_states
        if valid_state and (not ensure_visible or hda.visible):
            # If we are sending data to an external application, then we need to make sure there are no roles
            # associated with the dataset that restrict its access from "public".
            require_public = self.tool and self.tool.tool_type == "data_destination"
            if require_public and not self.trans.app.security_agent.dataset_is_public(dataset):
                return False
            return self.valid_hda_match(hda, check_implicit_conversions=check_implicit_conversions)

    def hda_match_collections(self, hdas, check_implicit_conversions=True, ensure_visible=True):
        """Batch-match HDAs with pre-loaded conversion data."""
        valid_input_states = self.dataset_matcher_factory.valid_input_states
        require_public = self.tool and self.tool.tool_type == "data_destination"

        candidates = [
            hda
            for hda in hdas
            if hda.dataset.state in valid_input_states
            and (not ensure_visible or hda.visible)
            and (not require_public or self.trans.app.security_agent.dataset_is_public(hda.dataset))
        ]

        if candidates and check_implicit_conversions:
            _prefetch_implicitly_converted_datasets(candidates)

        results = []
        for hda in candidates:
            hda_match = self.valid_hda_match(hda, check_implicit_conversions=check_implicit_conversions)
            if hda_match and not self.filter(hda_match.hda):
                results.append((hda, hda_match))
        return results

    def filter(self, hda):
        """Filter out this value based on other values for job (if
        applicable).
        """
        param = self.param
        return param.options and param.get_options_filter_attribute(hda) not in self.filter_values


class HdaDirectMatch:
    """Supplied HDA was a valid option directly (did not need to find implicit
    conversion).
    """

    def __init__(self, hda):
        self.hda = hda

    @property
    def implicit_conversion(self):
        return False


class HdaImplicitMatch:
    """Supplied HDA was a valid option directly (did not need to find implicit
    conversion).
    """

    def __init__(self, hda, target_ext, original_hda):
        self.original_hda = original_hda
        self.hda = hda
        self.target_ext = target_ext

    @property
    def implicit_conversion(self):
        return True


class HdcaDirectMatch:
    implicit_conversion = False
    requires_adapter = False

    def __init__(self):
        pass


class HdcaImplicitMatch:
    implicit_conversion = True

    def __init__(self):
        pass


class SummaryDatasetCollectionMatcher:
    def __init__(self, dataset_matcher_factory, trans, dataset_matcher):
        self.dataset_matcher_factory = dataset_matcher_factory
        self._trans = trans
        self.dataset_matcher = dataset_matcher

    def hdca_match(self, history_dataset_collection_association):
        dataset_collection = history_dataset_collection_association.collection

        if not dataset_collection.populated_optimized:
            return False

        summary = dataset_collection.dataset_states_and_extensions_summary
        states = summary.states
        extensions = summary.extensions
        for state in states.keys():
            if state not in self.dataset_matcher_factory.valid_input_states:
                return False

        formats = self.dataset_matcher.param.formats
        uses_implicit_conversion = False
        for extension in extensions:
            datatypes_registry = self._trans.app.datatypes_registry
            direct_match, converted_ext, _ = datatypes_registry.find_conversion_destination_for_dataset_by_extensions(
                extension, formats
            )
            if direct_match:
                continue
            if not converted_ext:
                return False
            else:
                uses_implicit_conversion = True

        return HdcaImplicitMatch() if uses_implicit_conversion else HdcaDirectMatch()

    def hdca_match_collections(self, history, collection_type_filter=None, visible_only=True):
        """Batch-match HDCAs via lightweight DB queries.

        Returns list of (hdca_id, implicit_conversion) for matching HDCAs.
        """
        session = object_session(history)
        summaries, unpopulated_ids = self.dataset_matcher_factory.batch_collection_summaries(
            session, history.id, collection_type_filter, visible_only
        )

        formats = self.dataset_matcher.param.formats
        datatypes_registry = self._trans.app.datatypes_registry

        results = []
        for hdca_id, summary in summaries.items():
            uses_implicit_conversion = False
            skip = False
            for extension in summary.extensions:
                direct_match, converted_ext, _ = datatypes_registry.find_conversion_destination_for_dataset_by_extensions(
                    extension, formats
                )
                if direct_match:
                    continue
                if not converted_ext:
                    skip = True
                    break
                uses_implicit_conversion = True
            if not skip:
                results.append((hdca_id, uses_implicit_conversion))
        return results


class DatasetCollectionMatcher:
    def __init__(self, trans, dataset_matcher):
        self.dataset_matcher = dataset_matcher
        self._trans = trans

    def __valid_element(self, element):
        # Simplify things for now and assume these are hdas and not implicit
        # converts. One could imagine handling both of those cases down the
        # road.
        if element.ldda:
            return False

        if child_collection := element.child_collection:
            return self.dataset_collection_match(child_collection)

        hda = element.hda
        if not hda:
            return False
        hda_match = self.dataset_matcher.hda_match(hda, ensure_visible=False)
        return hda_match

    def hdca_match(self, history_dataset_collection_association):
        dataset_collection = history_dataset_collection_association.collection
        return self.dataset_collection_match(dataset_collection)

    def dataset_collection_match(self, dataset_collection):
        # If dataset collection not yet populated, cannot determine if it
        # would be a valid match for this parameter.
        if not dataset_collection.populated_optimized:
            return False

        valid = True
        uses_implicit_conversion = False
        for element in dataset_collection.elements:
            match_element = self.__valid_element(element)
            if not match_element:
                valid = False
                break
            elif match_element.implicit_conversion:
                uses_implicit_conversion = True

        return valid and (HdcaImplicitMatch() if uses_implicit_conversion else HdcaDirectMatch())

    def hdca_match_collections(self, history, collection_type_filter=None, visible_only=True):
        """Fallback batch match — loads full models and delegates to per-item hdca_match."""
        hdcas = history.active_visible_dataset_collections if visible_only else history.active_dataset_collections
        results = []
        for hdca in hdcas:
            if collection_type_filter and hdca.collection.collection_type not in collection_type_filter:
                continue
            hdca_match = self.hdca_match(hdca)
            if hdca_match:
                results.append((hdca.id, hdca_match.implicit_conversion))
        return results


def _batch_collection_summaries(
    session,
    history_id: int,
    collection_type_filter: Optional[set[str]],
    valid_input_states: set[str],
    visible_only: bool = True,
) -> tuple[dict[int, CollectionStateSummary], set[int]]:
    """Batch-fetch collection summaries for all candidate HDCAs in a history.

    Returns:
        (summaries, unpopulated_ids) where summaries maps hdca_id to
        CollectionStateSummary (only for populated collections whose dataset
        states are all in valid_input_states), and unpopulated_ids is the
        set of hdca_ids whose collections are not fully populated.
    """
    hdca_t = HistoryDatasetCollectionAssociation.__table__
    dc_t = DatasetCollection.__table__

    # Phase 1: lightweight metadata query — no ORM models
    meta_q = (
        select(
            hdca_t.c.id.label("hdca_id"),
            dc_t.c.id.label("collection_id"),
            dc_t.c.collection_type,
            dc_t.c.populated_state,
        )
        .select_from(hdca_t.join(dc_t, dc_t.c.id == hdca_t.c.collection_id))
        .where(
            hdca_t.c.history_id == history_id,
            not_(hdca_t.c.deleted),
        )
    )
    if visible_only:
        meta_q = meta_q.where(hdca_t.c.visible == True)  # noqa: E712
    if collection_type_filter:
        meta_q = meta_q.where(dc_t.c.collection_type.in_(collection_type_filter))

    rows = session.execute(meta_q).all()
    if not rows:
        return {}, set()

    # Map hdca_id -> (collection_id, collection_type, populated_state)
    hdca_to_coll: dict[int, tuple[int, str, str]] = {}
    for r in rows:
        hdca_to_coll[r.hdca_id] = (r.collection_id, r.collection_type, r.populated_state)

    # Group collection_ids by type; track flat-unpopulated separately
    coll_ids_by_type: dict[str, list[int]] = defaultdict(list)
    hdca_by_coll: dict[int, list[int]] = defaultdict(list)  # coll_id -> [hdca_id, ...]
    unpopulated_hdca_ids: set[int] = set()

    for hdca_id, (coll_id, coll_type, pop_state) in hdca_to_coll.items():
        hdca_by_coll[coll_id].append(hdca_id)
        if ":" not in coll_type:
            # Flat: populated_state on root is sufficient
            if pop_state != DatasetCollection.populated_states.OK:
                unpopulated_hdca_ids.add(hdca_id)
                continue
        coll_ids_by_type[coll_type].append(coll_id)

    # Phase 2: for nested types, batch check populated_optimized
    is_postgres = session.bind and session.bind.dialect.name == "postgresql"
    for coll_type, coll_ids in list(coll_ids_by_type.items()):
        if ":" not in coll_type:
            continue
        nested_unpop = _batch_populated_check(session, coll_type, coll_ids, is_postgres)
        for coll_id in nested_unpop:
            for hid in hdca_by_coll[coll_id]:
                unpopulated_hdca_ids.add(hid)
        # Remove unpopulated from summary fetch
        coll_ids_by_type[coll_type] = [c for c in coll_ids if c not in nested_unpop]

    # Phase 3: batch summary query per type group
    summaries: dict[int, CollectionStateSummary] = {}  # hdca_id -> summary
    for coll_type, coll_ids in coll_ids_by_type.items():
        if not coll_ids:
            continue
        coll_summaries = _batch_summary_query(session, coll_type, coll_ids, is_postgres)
        for coll_id, summary in coll_summaries.items():
            # State pre-filter
            if any(s not in valid_input_states for s in summary.states):
                continue
            for hid in hdca_by_coll[coll_id]:
                if hid not in unpopulated_hdca_ids:
                    summaries[hid] = summary

    return summaries, unpopulated_hdca_ids


def _batch_populated_check(session, collection_type: str, collection_ids: list[int], is_postgres: bool) -> set[int]:
    """Return the set of collection_ids that are NOT fully populated (nested types only)."""
    if not collection_ids:
        return set()

    dce_table = DatasetCollectionElement.__table__
    dc_table = DatasetCollection.__table__
    n_intermediates = collection_type.count(":")

    if is_postgres:
        inner_dce = alias(dce_table)
        child_ids_array = func.array(
            select(inner_dce.c.child_collection_id)
            .where(inner_dce.c.dataset_collection_id == any_(collection_ids))
            .scalar_subquery()
        )
        level_conditions = [dc_table.c.id == any_(child_ids_array)]
        for _ in range(n_intermediates - 1):
            next_dce = alias(dce_table)
            child_ids_array = func.array(
                select(next_dce.c.child_collection_id)
                .where(next_dce.c.dataset_collection_id == any_(child_ids_array))
                .scalar_subquery()
            )
            level_conditions.append(dc_table.c.id == any_(child_ids_array))

        # Find any sub-collection that is not OK
        stmt = (
            select(dc_table.c.id)
            .where(
                or_(*level_conditions),
                dc_table.c.populated_state != DatasetCollection.populated_states.OK,
            )
        )
        bad_sub_ids = {r[0] for r in session.execute(stmt).all()}
        if not bad_sub_ids:
            return set()

        # Walk back to find which root IDs have bad sub-collections
        # Re-walk the tree to map bad sub-collection -> root
        unpopulated_roots: set[int] = set()
        for root_id in collection_ids:
            inner = alias(dce_table)
            child_array = func.array(
                select(inner.c.child_collection_id)
                .where(inner.c.dataset_collection_id == root_id)
                .scalar_subquery()
            )
            all_conditions = [dc_table.c.id == any_(child_array)]
            for _ in range(n_intermediates - 1):
                nxt = alias(dce_table)
                child_array = func.array(
                    select(nxt.c.child_collection_id)
                    .where(nxt.c.dataset_collection_id == any_(child_array))
                    .scalar_subquery()
                )
                all_conditions.append(dc_table.c.id == any_(child_array))
            check = (
                select(func.count())
                .select_from(dc_table)
                .where(
                    or_(*all_conditions),
                    dc_table.c.populated_state != DatasetCollection.populated_states.OK,
                )
            )
            if session.execute(check).scalar():
                unpopulated_roots.add(root_id)
        return unpopulated_roots
    else:
        # SQLite: use outerjoin chain per root to check populated states
        unpopulated: set[int] = set()
        for root_id in collection_ids:
            dc = alias(dc_table)
            dce = alias(dce_table)
            q = (
                select(dc.c.populated_state)
                .select_from(dc)
                .join(dce, dce.c.dataset_collection_id == dc.c.id)
                .where(dc.c.id == root_id)
            )
            depth = collection_type
            while ":" in depth:
                inner_dce = alias(dce_table)
                inner_dc = alias(dc_table)
                q = q.outerjoin(inner_dce, inner_dce.c.dataset_collection_id == dce.c.child_collection_id)
                q = q.outerjoin(inner_dc, inner_dc.c.id == dce.c.child_collection_id)
                q = q.add_columns(inner_dc.c.populated_state)
                dce = inner_dce
                depth = depth.split(":", 1)[1]
            for row in session.execute(q):
                if any(s not in (DatasetCollection.populated_states.OK, None) for s in row):
                    unpopulated.add(root_id)
                    break
        return unpopulated


def _batch_summary_query(
    session, collection_type: str, collection_ids: list[int], is_postgres: bool
) -> dict[int, CollectionStateSummary]:
    """Batch-fetch summaries for collections of a single type. Returns {collection_id: summary}."""
    if not collection_ids:
        return {}

    dce_table = DatasetCollectionElement.__table__
    dc_table = DatasetCollection.__table__
    hda_table = HistoryDatasetAssociation.__table__
    dataset_table = Dataset.__table__

    if ":" not in collection_type:
        # Flat collection — simple join
        dce = alias(dce_table)
        q = (
            select(
                dce.c.dataset_collection_id.label("root_id"),
                hda_table.c.extension,
                dataset_table.c.state,
            )
            .select_from(dce)
            .join(hda_table, hda_table.c.id == dce.c.hda_id)
            .join(dataset_table, dataset_table.c.id == hda_table.c.dataset_id)
            .where(dce.c.dataset_collection_id.in_(collection_ids))
        )
    elif is_postgres:
        # Nested on PostgreSQL — ARRAY walk pattern
        n_intermediates = collection_type.count(":")
        inner_dce = alias(dce_table)
        child_ids_subq = select(inner_dce.c.child_collection_id).where(
            inner_dce.c.dataset_collection_id == any_(collection_ids)
        )
        # Track root: walk back from leaf
        # We need to build a nav chain from leaf to root
        for _ in range(n_intermediates - 1):
            next_dce = alias(dce_table)
            child_ids_subq = select(next_dce.c.child_collection_id).where(
                next_dce.c.dataset_collection_id == any_(func.array(child_ids_subq.scalar_subquery()))
            )

        leaf_dce = alias(dce_table)
        q = (
            select()
            .select_from(leaf_dce)
            .where(leaf_dce.c.dataset_collection_id == any_(func.array(child_ids_subq.scalar_subquery())))
        )

        # Build nav chain to find root_id
        coll_ids_chain = [leaf_dce.c.dataset_collection_id]
        for _ in range(n_intermediates):
            nav = alias(dce_table)
            coll_ids_chain.append(
                select(nav.c.dataset_collection_id)
                .where(nav.c.child_collection_id == coll_ids_chain[-1])
                .correlate(leaf_dce)
                .limit(1)
                .scalar_subquery()
            )

        root_id_expr = coll_ids_chain[-1]
        q = q.add_columns(root_id_expr.label("root_id"))
        q = (
            q.join(hda_table, hda_table.c.id == leaf_dce.c.hda_id)
            .join(dataset_table, dataset_table.c.id == hda_table.c.dataset_id)
            .add_columns(
                hda_table.c.extension,
                dataset_table.c.state,
            )
        )
    else:
        # Nested on SQLite — outerjoin chain
        dc = alias(dc_table)
        dce = alias(dce_table)
        q = (
            select(dc.c.id.label("root_id"))
            .select_from(dc)
            .join(dce, dce.c.dataset_collection_id == dc.c.id)
            .where(dc.c.id.in_(collection_ids))
        )
        depth = collection_type
        while ":" in depth:
            inner_dce = alias(dce_table)
            q = q.outerjoin(inner_dce, inner_dce.c.dataset_collection_id == dce.c.child_collection_id)
            dce = inner_dce
            depth = depth.split(":", 1)[1]

        q = (
            q.join(hda_table, hda_table.c.id == dce.c.hda_id)
            .join(dataset_table, dataset_table.c.id == hda_table.c.dataset_id)
            .add_columns(
                hda_table.c.extension,
                dataset_table.c.state,
            )
        )

    # Execute and aggregate per root_id
    rows_by_root: dict[int, list] = defaultdict(list)
    for row in session.execute(q):
        if row.root_id is not None:
            rows_by_root[row.root_id].append(row)

    result: dict[int, CollectionStateSummary] = {}
    for coll_id, rows in rows_by_root.items():
        extensions: set[str] = set()
        states: dict[str, int] = defaultdict(int)
        for row in rows:
            if row.extension:
                extensions.add(row.extension)
            if row.state:
                states[row.state] += 1
        filtered_extensions = sorted(e for e in extensions if e is not None)
        result[coll_id] = CollectionStateSummary([], filtered_extensions, dict(states), 0)

    return result


def _prefetch_implicitly_converted_datasets(hdas):
    """Batch-load implicitly_converted_datasets for HDAs to avoid N+1."""
    if not hdas:
        return
    session = object_session(hdas[0])
    if session is None:
        return
    hda_ids = [hda.id for hda in hdas if "implicitly_converted_datasets" not in hda.__dict__]
    if not hda_ids:
        return
    stmt = (
        select(ImplicitlyConvertedDatasetAssociation)
        .where(ImplicitlyConvertedDatasetAssociation.hda_parent_id.in_(hda_ids))
        .options(joinedload(ImplicitlyConvertedDatasetAssociation.dataset))
    )
    assocs = session.scalars(stmt).unique().all()
    by_parent: dict[int, list] = defaultdict(list)
    for a in assocs:
        by_parent[a.hda_parent_id].append(a)
    for hda in hdas:
        if hda.id in hda_ids:
            set_committed_value(hda, "implicitly_converted_datasets", by_parent.get(hda.id, []))


def _load_hdcas(session, hdca_ids):
    """Load full HDCA ORM objects by ID with collection + tags."""
    if not hdca_ids:
        return {}
    stmt = (
        select(HistoryDatasetCollectionAssociation)
        .where(HistoryDatasetCollectionAssociation.id.in_(hdca_ids))
        .options(
            joinedload(HistoryDatasetCollectionAssociation.collection),
            joinedload(HistoryDatasetCollectionAssociation.tags),
        )
    )
    return {hdca.id: hdca for hdca in session.scalars(stmt).unique().all()}


def _direct_match_types(history_query) -> Optional[set[str]]:
    """Extract collection_type strings accepted by direct_match."""
    if history_query.collection_type_descriptions is None:
        return None
    types: set[str] = set()
    for desc in history_query.collection_type_descriptions:
        ct = desc.collection_type
        types.add(ct)
        if ct == "paired":
            types.add("paired_or_unpaired")
        elif ct == "paired_or_unpaired":
            types.add("paired")
        if ct.endswith(":paired_or_unpaired"):
            prefix = ct[: -len(":paired_or_unpaired")]
            types.add(prefix)
            types.add(f"{prefix}:paired")
    return types


__all__ = ("get_dataset_matcher_factory", "set_dataset_matcher_factory", "unset_dataset_matcher_factory")
