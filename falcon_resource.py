import falcon
import json
import requests
import re
from falcon_lookup import input_grade_step

GS_LOOKUP_URL = 'https://www.federalpay.org/api/calculator/GS'
html_filter = re.compile('<[^<]+?>')

class Resource(object):
### when a function is part of a class it's called a method
    def on_get(self, req, resp):
        gs = input_grade_step()
        return

    def fetch_pay_for_grade(grade, step):
        r = requests.get(GS_LOOKUP_URL, params={'year': '2017', 'state': 'Illinois', 'county': 'Cook', 'grade': grade, 'step': step, "s": 2})
        reponse = json.loads(html_filter.sub('', r.content))
        pay = float(reponse['AdjustedSalary'])
        # pay.append(fetch_pay_for_grade(**gs))
        pay.append(fetch_pay_for_grade(on_get()))
        return pay
        print pay

        # if 'application/json' not in req.content_type:
        #     response = {"error": "Only JSON data is accepted.", "data": None}
        #     resp.status = falcon.HTTP_UNSUPPORTED_MEDIA_TYPE
        #     resp.content(json.dumps(response))
        #     return
        #
        # try:
        #     input_data = json.loads(req.body)
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
