import falcon
import msgpack

API = application = falcon.API()
pay = Resource()
api.add_route('https://www.federalpay.org/employees/lookup', pay)

class Resource(object): # just a regular class
    def on_get(self, req, resp): # function defines HTTP resource // on_* where * is any standard HTTP method, lowercase
        doc = {
            'pay': [
                {
                'year': '2015', 'firstName': first_name, 'lastName': last_name, 'state': 'IL'
                }
            ]
        }

        # Create JSON representation ofo the Resource
        resp.data = msgpack.packb(doc, use_bin_type=True)

        resp.content_type = 'application/msgpack'

        resp.status = falcon.HTTP_200 # 200 is the default response but can be overridden as-needed

def input_name():
        first_name = raw_input("first name:")
        if not first_name:
            return None, None
        last_name = raw_input("last name:")
        if not last_name:
            return None, None

        return first_name, last_name



def fetch_pay_for_name(first_name, last_name):
    f = 
    return pay

def input_grade():
    state = raw_input("Employee state: ")
    county = raw_input("Employee county: ")
    grade = raw_input("Employee grade: ")
    step = raw_input("Employee step: ")
    return state, county, grade, step

def fetch_pay_for_grade(state, county, grade, step):
    q = requests.get(GS_LOOKUP_URL, params={'year': '2017', 'state': state, 'county': county, 'grade': grade, 'step': step, "s": 2})
    qreponse = json.loads(html_filter.sub('', q.content))
    pay = float(qreponse['AdjustedSalary'])
    return pay

########################## NEW STUFF ###############################

total_pay = []
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

cost_per_second = float(sum(total_pay)) / WORK_SECONDS_IN_YEAR
meeting_cost = 0.00
print
# system interrupt
while True:
    try:
        sys.stdout.write("\rCurrent meeting is costing taxpayers: ${0:.2f}".format(meeting_cost))
        sys.stdout.flush()
        sleep(1)
        meeting_cost += cost_per_second
    except KeyboardInterrupt:
        sys.exit(0)




# filtered_result = """{
#     "queryExecutionTime": 0.0003,
#     "result": [
#         {
#             "name": "Robert W. Steetz",
#             "slug": "steetz-robert-w",
#             "agency_slug": "federal-acquisition-service",
#             "occupation_slug": "miscellaneous-administration-and-program",
#             "year": "2015",
#             "occupation": "Miscellaneous Administration and Program",
#             "agency": "Federal Acquisition Service",
#             "state": "ILLINOIS",
#             "country": "United States",
#             "pay": "109759",
#             "location": "Illinois",
#             "formatted_pay": "$109,759"
#         }
#     ]
# }"""
#
#
# raw_json_result = """{
#     "queryExecutionTime": 0.0003,
#     "result": [
#         {
#             "name": "<a href=/employees/federal-acquisition-service/steetz-robert-w>Robert W. Steetz</a>",
#             "slug": "steetz-robert-w",
#             "agency_slug": "federal-acquisition-service",
#             "occupation_slug": "miscellaneous-administration-and-program",
#             "year": "2015",
#             "occupation": "<a href=/employees/occupations/miscellaneous-administration-and-program>Miscellaneous Administration and Program</a>",
#             "agency": "<a href=/employees/federal-acquisition-service>Federal Acquisition Service</a>",
#             "state": "ILLINOIS",
#             "country": "United States",
#             "pay": "109759",
#             "location": "Illinois",
#             "formatted_pay": "$109,759"
#         }
#     ]
# }"""
#
#
# # Here is the URL to fetch salary data for a given GS and step.
# gs_lookup_url = 'https://www.federalpay.org/api/calculator/GS?s=2&state=Illinois&county=Cook&grade=10&step=4&year=2017'
#
# sample_output = """
#     {
#         "Rank": "Captain",
#         "BaseSalary": "52394",
#         "AdjustedSalary": "66461.79",
#         "IsSalaryCapped": "False",
#         "WeeksToIncreaseStep": "104",
#         "LocalityAreaName": "Chicago",
#         "LocalityAreaLongName": "CHICAGO-NAPERVILLE, IL-IN-WI",
#         "LocalityRate": "0.2685",
#         "Education": "Master's Degree",
#         "Experience": "At least 1 year experience at GS-9 or equivalent",
#         "s": "2",
#         "year": "2017",
#         "grade": "10",
#         "step": "4",
#         "state": "Illinois",
#         "county": "Cook"
#     }"""
