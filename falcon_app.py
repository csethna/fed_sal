import falcon
import json
from falcon_resource import Resource

api = application = falcon.API()

salary = Resource()
api.add_route('/salary', salary)

#total_pay = json.dumps()


#
# ### total_pay = [] ### make a list containing all salaries
#
#         ## HOMEWORK
#         # Fetch a salary for each user in the list
#         # Use the bits from our commandline version to fetch a salary for each data point.
#         # set the respose to json.dumps(the_list) and status to 200 and return
#
#
# # sample_input = [
# #     {"first": "...",
# #      "last": "...",
# #      "grade": "...",
# #      "step": "..."},
# #     {"first": "...",
# #      "last": "...",
# #      "grade": "...",
# #      "step": "..."},
# #     ...
# # ]
