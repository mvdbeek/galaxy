import graphene
from starlette.graphql import GraphQLApp

from galaxy import model
from galaxy import app

from graphene import String
from graphene.types.json import JSONString

from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from graphene_sqlalchemy.converter import convert_sqlalchemy_type

from sqlalchemy import inspect
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import Mapper

from galaxy.model.custom_types import JSONType, TrimmedString, UUIDType


@convert_sqlalchemy_type.register(JSONType)
def convert_column_to_string(type, column, registry=None):
    return JSONString


@convert_sqlalchemy_type.register(TrimmedString)
@convert_sqlalchemy_type.register(UUIDType)
def convert_column_to_string(type, column, registry=None):
    return String


adapted_classes = {}
query = app.app.model.session.query_property()
for cls_name, cls in model.__dict__.items():
    if cls_name == 'WorkflowStepConnection':
        continue
    try:
        if isinstance(inspect(cls), Mapper):
            new_meta = type('Meta', (object,), {'model': cls, 'interfaces': (relay.Node, )})
            new_cls = type(cls_name, (SQLAlchemyObjectType,), {'Meta': new_meta})
            adapted_classes[cls_name] = new_cls
            cls.query = query
    except Exception:
        # TODO: Don't know how to convert the SQLAlchemy field happens for SELECT avg() columns
        continue




class Query(graphene.ObjectType):
    hdas = graphene.List(adapted_classes['HistoryDatasetAssociation'], user_id = graphene.Int(), history_id=graphene.Int())
    datasets = graphene.List(adapted_classes['Dataset'])
    hdcas = graphene.List(adapted_classes['HistoryDatasetCollectionAssociation'], user_id = graphene.Int(), history_id=graphene.Int())
    histories = graphene.List(adapted_classes['History'], user_id = graphene.Int(), history_id=graphene.Int())
    jobs = graphene.List(adapted_classes['Job'])

    get_histories_for_user = graphene.Field

    def resolve_hdas(self, info, user_id, history_id):
        query = adapted_classes['HistoryDatasetAssociation'].get_query(info)  # SQLAlchemy query
        query = query.filter_by(user_id=user_id, history_id=history_id)
        return query.all()
    
    def resolve_hdcas(self, info, user_id, history_id):
        query = adapted_classes['HistoryDatasetCollectionAssociation'].get_query(info)  # SQLAlchemy query
        query = query.filter_by(user_id=user_id, history_id=history_id)
        return query.all()

    def resolve_histories(self, info, user_id):
        query = adapted_classes['History'].get_query(info).filter_by(user_id=user_id)  # SQLAlchemy query
        query = query.filter_by(user_id=user_id)
        return query.all()

    def resolve_jobs(self, info, history_id, user_id):
        query = adapted_classes['Job'].get_query(info)  # SQLAlchemy query
        query = query.filter_by(user_id=user_id, history_id=history_id)
        return query.all()


graphql_app = GraphQLApp(schema=graphene.Schema(query=Query))