import requests
import json
import re

GS_LOOKUP_URL = 'https://www.federalpay.org/api/calculator/GS'
html_filter = re.compile('<[^<]+?>')

def input_grade_step():
    grade = raw_input("Employee GS Grade:")
    step = raw_input("GS Step:")
    return grade, step

def fetch_pay_for_grade(grade, step):
    r = requests.get(GS_LOOKUP_URL, params={'year': '2017', 'state': 'Illinois', 'county': 'Cook', 'grade': grade, 'step': step, "s": 2})
    reponse = json.loads(html_filter.sub('', r.content))
    pay = float(reponse['AdjustedSalary'])
    # pay.append(fetch_pay_for_grade(**gs))
    # pay.append(fetch_pay_for_grade(grade, step))
    return pay

def grade_step():
    salary = []

    while True:
        grade, step = input_grade_step() # make this a loop
        if not grade or not step:
            break
        try:
            salary.append(fetch_pay_for_grade(grade, step))
            print salary
        except KeyboardInterrupt:
            break
    return
