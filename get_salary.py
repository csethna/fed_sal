import falcon
import msgpack

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
