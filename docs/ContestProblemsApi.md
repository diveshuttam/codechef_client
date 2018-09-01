# codechef_client.ContestProblemsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contests_contest_code_problems_problem_code_get**](ContestProblemsApi.md#contests_contest_code_problems_problem_code_get) | **GET** /contests/{contestCode}/problems/{problemCode} | Get details of a problem.


# **contests_contest_code_problems_problem_code_get**
> InlineResponse2004 contests_contest_code_problems_problem_code_get(problem_code, contest_code, fields=fields)

Get details of a problem.

Takes problemCode as the parameter and fetches details of that problem.

### Example
```python
from __future__ import print_function
import time
import codechef_client
from codechef_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: codechef_auth
configuration = codechef_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = codechef_client.ContestProblemsApi(codechef_client.ApiClient(configuration))
problem_code = 'problem_code_example' # str | Problem code of the problem, eg. SALARY
contest_code = 'contest_code_example' # str | Contest code of the contest, eg. PRACTICE, COOK97, JAN17
fields = 'fields_example' # str | Possible fields are- problemCode, author, problemName, languagesSupported, sourceSizeLimit,  dateAdded, challengeType, maxTimeLimit, successfulSubmissions, body, totalSubmissions, partialSubmissions, tags.  Multiple fields can be entered using comma. (optional)

try:
    # Get details of a problem.
    api_response = api_instance.contests_contest_code_problems_problem_code_get(problem_code, contest_code, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContestProblemsApi->contests_contest_code_problems_problem_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_code** | **str**| Problem code of the problem, eg. SALARY | 
 **contest_code** | **str**| Contest code of the contest, eg. PRACTICE, COOK97, JAN17 | 
 **fields** | **str**| Possible fields are- problemCode, author, problemName, languagesSupported, sourceSizeLimit,  dateAdded, challengeType, maxTimeLimit, successfulSubmissions, body, totalSubmissions, partialSubmissions, tags.  Multiple fields can be entered using comma. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

