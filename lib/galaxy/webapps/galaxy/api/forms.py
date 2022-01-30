"""
API operations on FormDefinition objects.
"""
import logging

from galaxy import web
from galaxy.forms.forms import form_factory
from galaxy.util import XML
from galaxy.webapps.base.controller import url_for
from . import BaseGalaxyAPIController

log = logging.getLogger(__name__)


class FormDefinitionAPIController(BaseGalaxyAPIController):

    @web.legacy_expose_api
    def index(self, trans, **kwd):
        """
        GET /api/forms
        Displays a collection (list) of forms.
        """
        if not trans.user_is_admin:
            trans.response.status = 403
            return "You are not authorized to view the list of forms."
        query = trans.sa_session.query(trans.app.model.FormDefinition)
        rval = []
        for form_definition in query:
            item = form_definition.to_dict(value_mapper={'id': trans.security.encode_id, 'form_definition_current_id': trans.security.encode_id})
            item['url'] = url_for('form', id=trans.security.encode_id(form_definition.id))
            rval.append(item)
        return rval

    @web.legacy_expose_api
    def show(self, trans, id, **kwd):
        """
        GET /api/forms/{encoded_form_id}
        Displays information about a form.
        """
        form_definition_id = id
        try:
            decoded_form_definition_id = trans.security.decode_id(form_definition_id)
        except TypeError:
            trans.response.status = 400
            return f"Malformed form definition id ( {str(form_definition_id)} ) specified, unable to decode."
        try:
            form_definition = trans.sa_session.query(trans.app.model.FormDefinition).get(decoded_form_definition_id)
        except Exception:
            form_definition = None
        if not form_definition or not trans.user_is_admin:
            trans.response.status = 400
            return f"Invalid form definition id ( {str(form_definition_id)} ) specified."
        item = form_definition.to_dict(view='element', value_mapper={'id': trans.security.encode_id, 'form_definition_current_id': trans.security.encode_id})
        item['url'] = url_for('form', id=form_definition_id)
        return item

    @web.legacy_expose_api
    def create(self, trans, payload, **kwd):
        """
        POST /api/forms
        Creates a new form.
        """
        if not trans.user_is_admin:
            trans.response.status = 403
            return "You are not authorized to create a new form."
        xml_text = payload.get('xml_text', None)
        if xml_text is None:
            trans.response.status = 400
            return "Missing required parameter 'xml_text'."
            # enhance to allow creating from more than just xml
        form_definition = form_factory.from_elem(XML(xml_text))
        trans.sa_session.add(form_definition)
        trans.sa_session.flush()
        encoded_id = trans.security.encode_id(form_definition.id)
        item = form_definition.to_dict(view='element', value_mapper={'id': trans.security.encode_id, 'form_definition_current_id': trans.security.encode_id})
        item['url'] = url_for('form', id=encoded_id)
        return [item]
