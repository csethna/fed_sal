import falcon
import json
#from falcon_resource import Resource

class Resource(object):

    def on_get(self, req, resp):
        salary = {
            'url':[
            {'name_href' : 'https://www.federalpay.org/employees/lookup',
            'grade_href' : 'https://www.federalpay.org/api/calculator/GS'}
            ]
        }

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
                reponse = {"error": "Each data object requires at least [first and last name] or [grade and step].", "data": None}
                resp.status = falcon.HTTP_BAD_REQUEST
                resp.content(json.dumps(response))
                return
        return on_get()

api = application = falcon.API()
pay = Resource()
api.add_route('/salary', pay)


def input_name():
    name = []
    first_name = input("first name:")
    if not first_name:
        return None, None
    last_name = input("last name:")
    if not last_name:
        return None, None
    name.append((first_name, last_name))
    return(first_name, last_name)

# Get pay for all attendees
while True:
    try:
        first, last = input_name()
        if not first or not last:
            break
        try:
            total_pay.append(fetch_pay_for_name(first, last))
        except ValueError, IndexError:
            # Handle error fetching via name by falling back to fetching via general schedule
            print "Could not find employee with that name; we can look up by grade and step..."
            state, county, grade, step = input_grade()
            if not state or not county or not grade or not step:
                break
            total_pay.append(fetch_pay_for_grade(state, county, grade, step))
        print total_pay
    except KeyboardInterrupt:
        break
# fetch_salary = on_get(attendees)
# print(fetch_salary)

### total_pay = [] ### make a list containing all salaries

        ## HOMEWORK
        # Fetch a salary for each user in the list
        # Use the bits from our commandline version to fetch a salary for each data point.
        # set the respose to json.dumps(the_list) and status to 200 and return


# sample_input = [
#     {"first": "...",
#      "last": "...",
#      "grade": "...",
#      "step": "..."},
#     {"first": "...",
#      "last": "...",
#      "grade": "...",
#      "step": "..."},
#     ...
# ]
