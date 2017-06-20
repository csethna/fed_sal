import falcon
import json

api = application = falcon.API()
pay = Resource()
api.add_route('/salary', pay)

name = {}

def input_name():
        first_name = raw_input("first name:")
        if not first_name:
            return None, None
        last_name = raw_input("last name:")
        if not last_name:
            return None, None
        name.append(first_name,last_name)
        return name

class Resource(object):

    def on_get(self, req, resp):
        if 'application/json' not in req.content_type:
            response = {"error": "Only JSON data is accepted.", "data": None}
            resp.status = falcon.HTTP_UNSUPPORTED_MEDIA_TYPE
            resp.content(json.dumps(response))
            return

        try:
            input_data = json.loads(req.body)
        except ValueError:
            reponse = {"error": "Could not decode JSON input.", "data": None}
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.content(json.dumps(response))
            return

        if not isinstance(input_data, list):
            reponse = {"error": "Input should be a list of input data objects.", "data": None}
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.content(json.dumps(response))
            return

        for item in input_data:
            has_first = item.get('first', '')
            has_last = item.get('last', '')
            has_grade = item.get('grade', '')
            has_step = item.get('step', '')
            if not (has_first and has_last) and not (has_grade and has_step):
                reponse = {"error": "Each data object requires at least first and last name or grade and step.", "data": None}
                resp.status = falcon.HTTP_BAD_REQUEST
                resp.content(json.dumps(response))
                return

        ## HOMEWORK
        # Fetch a salary for each user in the list
        # Use the bits from our commandline version to fetch a salary for each data point.
        # set the respose to json.dumps(the_list) and status to 200 and return


sample_input = [
    {"first": "...",
     "last": "...",
     "grade": "...",
     "step": "..."},
    {"first": "...",
     "last": "...",
     "grade": "...",
     "step": "..."},
    ...
]
