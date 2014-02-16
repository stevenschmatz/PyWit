class MockConnector(object):
    def __init__(self, token, uri):
        self.response = None
        self.status_code = None
        self.token = token
        self.uri = uri

    def set_response(self, response, status_code):
        self.response = MockResponse(response, status_code)

    def post(self, body, resource, headers={}):
        return self.response

    def get(self, body, resource, headers={}):
        return self.response

class MockResponse(object):
    def __init__(self, response, status_code):
        self.response = response
        self.status_code = 200

    def json(self):
        return self.response