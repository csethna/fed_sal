import requests, re, json, sys

html_filter = re.compile('<[^<]+?>')
GS_LOOKUP_URL = 'https://www.federalpay.org/api/calculator/GS?s=2&state=Illinois&county=Cook&grade=10&step=4&year=2017'

def input_grade():
    state = raw_input("Employee state: ")
    # if not state:
    #     return None, None
    county = raw_input("Employee county: ")
    # if not county:
    #     return None, None
    grade = raw_input("Employee grade: ")
    # if not grade:
    #     return None, None
    step = raw_input("Employee step: ")
    # if not step:
    #     return None, None

    return state, county, grade, step

def fetch_pay_for_grade(state, county, grade, step):
    q = requests.get(GS_LOOKUP_URL, params={'year': '2017', 'state': state, 'county': county, 'grade': grade, 'step': step})
    qreponse = json.loads(html_filter.sub('', q.content))
    pay = int(qreponse['sample_output'][0]['pay'])
    return pay
    print pay

grade_pay = []
while True:
    try:
        state, county, grade, step = input_grade()
        if not state or not county or not grade or not step:
            break
        grade_pay.append(fetch_pay_for_grade(state, county, grade, step))
        print grade_pay
    except KeyboardInterrupt:
        break
