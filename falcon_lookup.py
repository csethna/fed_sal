import requests
import json
import re


html_filter = re.compile('<[^<]+?>')
LOOKUP_URL = 'https://www.federalpay.org/employees/lookup'
GS_LOOKUP_URL = 'https://www.federalpay.org/api/calculator/GS'


def fetch_pay_for_name(first_name, last_name):
    # Note how the params are a dictionary of key-value pairs;
    # requests will build the query params into the URL before making the request
    # Think about how you could build the params programmatically to request info on any given nameprint "first name:"
    r = requests.get(LOOKUP_URL, params={'year': '2015', 'firstName': first_name, 'lastName': last_name, 'state': 'IL'})
    # The two lines below both do two things at once; feel free to make these separate lines in your code
    # if that makes it easier to follow.
    response = json.loads(html_filter.sub('', r.content))
    # print response
    pay = int(response['result'][0]['pay'])
    # except ValueError:
    #     print ' '.join(["Salary redacted for", first_name, last_name])
    #     pay = 0
    # except IndexError:
    #     print ' '.join(["Employee", first_name, last_name, "not found, please check name."])
    #     pay = 0
    return pay


def fetch_pay_for_grade(state, county, grade, step):
    q = requests.get(GS_LOOKUP_URL, params={'year': '2017', 'state': state, 'county': county, 'grade': grade, 'step': step, "s": 2})
    qreponse = json.loads(html_filter.sub('', q.content))
    pay = int(float(qreponse['AdjustedSalary']))
    return pay
