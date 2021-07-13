# jira_issue_creator_middleware
A middleware rest API for creating issues in Jira. Written in Python.

Requirements:
- Python 3.7 or higher

Setup instructions:
1. install required modules from the requirements.txt
2. run jiraIssueCreationApi.py

    `python jiraIssueCreationApi.py`

    or :  `python3 jiraIssueCreationApi.py`

How to call the API:

There are two api end points, "<host>:5000/issue" and "<host>:5000/premadeissue".

- POST Calls to "<host>:5000/issue" will require that you provide data to parameters:

    `curl -d "url=https://www.google.com&username=bob&usersecret=password123&issuesummary=this is a bad issue&projectkey=AOS1&issuetypeid=10002" -X POST http://localhost:5000/issue`

- Please note the requirement status for the following parameters:

  -- ('url', required=True)

  -- ('username', required=True)
  
  -- ('usersecret', required=True)
  
  -- ('issuesummary', required=True)
  
  -- ('projectkey', required=True)
  
  -- ('issuetypeid', required=False)


- There is also "<host>:5000/testissue" that accpets POST and GET. 
  - GET requests will result in some default data being sent back in the request.
  - POST requests will echo back any data supplied to the parameters.

    `curl -d "url=https://www.google.com&username=bob&usersecret=password123&issuesummary=this is a bad issue&projectkey=AOS1&issuetypeid=10002" -X POST http://localhost:5000/testissue`