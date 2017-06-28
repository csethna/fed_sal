import falcon
import json
from falcon_lookup import fetch_pay_for_name, fetch_pay_for_grade

class GetSalaryResource(object):
### when a function is part of a class it's called a method
    def on_get(self, req, resp):

        if not req.content_type or (req.content_type and 'application/json' not in req.content_type):
            response = {"error": "Only JSON data is accepted.", "data": None}
            resp.status = falcon.HTTP_UNSUPPORTED_MEDIA_TYPE # 412 ?
            resp.body = json.dumps(response)
            return

        try:
            input_data = json.load(req.stream)
        except ValueError:
            response = {"error": "Could not decode JSON input.", "data": None}
            resp.status = falcon.HTTP_BAD_REQUEST # 400
            resp.body = json.dumps(response)
            return

        if not isinstance(input_data, list):
            response = {"error": "Input should be a list of input data objects.", "data": None}
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.body = json.dumps(response)
            return

        for item in input_data:
            first = item.get('first', '')
            last = item.get('last', '')
            grade = item.get('grade', '')
            step = item.get('step', '')
            if not (first and last) and not (grade and step):
                response = {"error": "Each data object requires at least [first and last name] or [grade and step].", "data": None}
                resp.status = falcon.HTTP_BAD_REQUEST
                resp.body = json.dumps(response)
                return

        result = []
        for item in input_data:
            first = item.get('first', '')
            last = item.get('last', '')
            grade = item.get('grade', '')
            step = item.get('step', '')

            if grade and step:
                salary = fetch_pay_for_grade('Illinois', 'Cook', grade, step)
            else:
                try:
                    salary = fetch_pay_for_name(first, last)
                except:
                    salary = 0
            result.append(salary)

        response = {"error": None, "data": result}
        resp.status = falcon.HTTP_OK
        resp.body = json.dumps(response)
        return
