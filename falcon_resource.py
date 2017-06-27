import falcon
import json
from falcon_lookup import grade_step

class Resource(object):
### when a function is part of a class it's called a method
    def on_get(self, req, resp):
        gs = grade_step()
        return

        # if 'application/json' not in gs:
        #     response = {"error": "Only JSON data is accepted.", "data": None}
        #     resp.status = falcon.HTTP_UNSUPPORTED_MEDIA_TYPE
        #     resp.content(json.dumps(response))
        #     return
        #
        # try:
        #     input_data = json.loads(gs)
        # except ValueError:
        #     reponse = {"error": "Could not decode JSON input.", "data": None}
        #     resp.status = falcon.HTTP_BAD_REQUEST
        #     resp.content(json.dumps(response))
        #     return
        #
        # if not isinstance(input_data, list):
        #     reponse = {"error": "Input should be a list of input data objects.", "data": None}
        #     resp.status = falcon.HTTP_BAD_REQUEST
        #     resp.content(json.dumps(response))
        #     return
        #
        # for item in input_data:
        #     has_first = item.get('first', '')
        #     has_last = item.get('last', '')
        #     has_grade = item.get('grade', '')
        #     has_step = item.get('step', '')
        #     if not (has_first and has_last) and not (has_grade and has_step):
        #         reponse = {"error": "Each data object requires at least [first and last name] or [grade and step].", "data": None}
        #         resp.status = falcon.HTTP_BAD_REQUEST
        #         resp.content(json.dumps(response))
        #         return
        #
        # response = {"error": None, "data": result}
        # resp.status = falcon.HTTP_OK
        # resp.data = json.dumps(result)
        # return
