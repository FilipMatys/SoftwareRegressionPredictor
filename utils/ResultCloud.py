import json
import requests


class ResultCloud:
    URL = ""
    token = ""
    isValid = False
    errors = list()
    last_response = dict()

    def __init__(self, url):
        self.URL = url

    def auth(self, username, password):
        resp = self.send_request("auth", "login", {"username": username, "password": password})
        if resp['IsValid']:
            self.token = resp['Result']['TokenKey']
        return self.check_valid(resp)

    def send_request(self, method, function, params):
        str_values = "&".join(["%s=%s" % (k, v) for k, v in params.items()])

        if not str_values:
            request = "%s%s.%s" % (self.URL, method, function)
        else:
            request = "%s%s.%s?%s" % (self.URL, method, function, str_values)

        print(request)

        resp = json.loads(requests.get(request).text)
        return resp

    def get_plugins(self):
        resp = self.send_request("plugins", "get", {})
        return self.check_valid(resp)

    def get_submissions_by_project(self, projectId):
        resp = self.send_request('submissions', 'getList', {"project": projectId})
        return self.check_valid(resp)

    def get_submission_by_hash(self, hash):
        resp = self.send_request("submissions", "getByHash", {"hash" : hash})
        return self.check_valid(resp)

    def get_project(self, project_id):
        resp = self.send_request("projects", "get", {"project" : project_id})
        return self.check_valid(resp)

    def get_git_projects(self):
        resp = self.send_request("projects", "getGitList", {})
        return self.check_valid(resp)

    def check_valid(self, resp):
        self.last_response = resp
        if not resp['IsValid']:
            self.errors = resp['Errors']

        self.isValid = resp['IsValid']
        return self.isValid
