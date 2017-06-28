import falcon
import json
from falcon_resource import GetSalaryResource

api = application = falcon.API()

api.add_route('/salary', GetSalaryResource())
