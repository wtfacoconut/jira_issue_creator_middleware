from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from requests.auth import HTTPBasicAuth
import json
from requests.models import Response

app = Flask(__name__)
api = Api(app)

def createJiraIssue(inUrl, username, userSecret, issueSummary, projectKey, issueTypeId="10002"):
    url = inUrl
    auth = HTTPBasicAuth(username, userSecret)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps(
        {
            "fields": {
                "summary": issueSummary,
                "issuetype": {
                    "id": issueTypeId
                },
                "project": {
                    "key": projectKey
                }
            }
        }
    )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    responsePrintData =  json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(responsePrintData)
    return response

def testGetCall(inUrl="https://jsonplaceholder.typicode.com/todos/1"):
    url = inUrl

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers
    )
    return response

def testCall2(inUrl, username, userSecret, issueSummary,  projectKey, issueTypeId="10002"):
    outData = {
        "INPUT_DATA": {
            "URL": inUrl,
            "USERNAME": username,
            "USER_SECRET": userSecret,
            "ISSUE_SUMMARY": issueSummary,
            "ISSUE_TYPE_ID": issueTypeId,
            "PROJECT_KEY": projectKey
        }
    }
    return outData

class Issue(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('usersecret', required=True)
        parser.add_argument('issuesummary', required=True)
        parser.add_argument('projectkey', required=True)
        parser.add_argument('issuetypeid', required=False)
        args = parser.parse_args()

        response=""
        if args['issuetypeid']:
            response = createJiraIssue(args['url'], args['username'], args['usersecret'], args['issuesummary'], args['issuetypeid'])
        else:
            response = createJiraIssue(args['url'], args['username'], args['usersecret'], args['issuesummary'])

        return response.json(), response.status_code

# class PreMadeIssue(Resource):
#     def post(self):
#         response = self.testCall(self, "https://jsonplaceholder.typicode.com/todos/1")
#         return response.json(), response.status_code  # return data and 200 OK code

class TestIssue(Resource):
    def get(self):
        testOut = testCall2("https://someUrl.com", "awesomeUser", "superSecret123", "This is a bad issue!", "proj123")
        return testOut, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True)
        parser.add_argument('username', required=True)
        parser.add_argument('usersecret', required=True)
        parser.add_argument('issuesummary', required=True)
        parser.add_argument('projectkey', required=True)
        parser.add_argument('issuetypeid', required=False)
        args = parser.parse_args()

        testOut=""
        if args['issuetypeid']:
            testOut = testCall2(args['url'], args['username'], args['usersecret'], args['issuesummary'], args['issuetypeid'])
        else:
            testOut = testCall2(args['url'], args['username'], args['usersecret'], args['issuesummary'])

        return testOut, 200
        
api.add_resource(Issue, '/issue')
# api.add_resource(PreMadeIssue, '/premadeissue')
api.add_resource(TestIssue, '/testissue')

if __name__ == '__main__':
    app.run() 