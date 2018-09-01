# codechef_client.SubmissionApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submissions_get**](SubmissionApi.md#submissions_get) | **GET** /submissions/ | Get submissions for particular user, problemCode, result and year.
[**submissions_submission_id_get**](SubmissionApi.md#submissions_submission_id_get) | **GET** /submissions/{submissionId} | Get details of a submission.


# **submissions_get**
> InlineResponse20013 submissions_get(result=result, year=year, username=username, language=language, problem_code=problem_code, contest_code=contest_code, limit=limit, offset=offset, fields=fields)

Get submissions for particular user, problemCode, result and year.

Takes result (result code), problemCode, year, username as condition parameters.

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
api_instance = codechef_client.SubmissionApi(codechef_client.ApiClient(configuration))
result = 'result_example' # str | Search submission by result, eg. AC, WA, RE etc. (optional)
year = 56 # int | Search submission by year, eg. 2012 (optional)
username = 'username_example' # str | Search submission by username, eg. hacker_ratty (optional)
language = 'language_example' # str | Search submission by language, eg. C++ 4.3.2 (optional)
problem_code = 'problem_code_example' # str | Code for problem, eg. SALARY (optional)
contest_code = 'contest_code_example' # str | Code of contest, eg. JAN13 (optional)
limit = 10 # int | limit for no. of submissions. Default = 10, max = 20 (optional) (default to 10)
offset = 0 # int | starting index for list. Default = 0 (optional) (default to 0)
fields = 'fields_example' # str | Possible fields are- id, date, username, problemCode, language, contestCode, result, time, memory.   Multiple fields can be entered using comma. (optional)

try:
    # Get submissions for particular user, problemCode, result and year.
    api_response = api_instance.submissions_get(result=result, year=year, username=username, language=language, problem_code=problem_code, contest_code=contest_code, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionApi->submissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | **str**| Search submission by result, eg. AC, WA, RE etc. | [optional] 
 **year** | **int**| Search submission by year, eg. 2012 | [optional] 
 **username** | **str**| Search submission by username, eg. hacker_ratty | [optional] 
 **language** | **str**| Search submission by language, eg. C++ 4.3.2 | [optional] 
 **problem_code** | **str**| Code for problem, eg. SALARY | [optional] 
 **contest_code** | **str**| Code of contest, eg. JAN13 | [optional] 
 **limit** | **int**| limit for no. of submissions. Default &#x3D; 10, max &#x3D; 20 | [optional] [default to 10]
 **offset** | **int**| starting index for list. Default &#x3D; 0 | [optional] [default to 0]
 **fields** | **str**| Possible fields are- id, date, username, problemCode, language, contestCode, result, time, memory.   Multiple fields can be entered using comma. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submissions_submission_id_get**
> InlineResponse20012 submissions_submission_id_get(submission_id, fields=fields)

Get details of a submission.

Takes SubmissionId as the parameter and fetches details of a submission.

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
api_instance = codechef_client.SubmissionApi(codechef_client.ApiClient(configuration))
submission_id = 56 # int | 
fields = 'fields_example' # str | Possible fields are- id, date, username, problemCode, language, contestCode, result, time, memory. Multiple fields can be entered using comma. (optional)

try:
    # Get details of a submission.
    api_response = api_instance.submissions_submission_id_get(submission_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmissionApi->submissions_submission_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **int**|  | 
 **fields** | **str**| Possible fields are- id, date, username, problemCode, language, contestCode, result, time, memory. Multiple fields can be entered using comma. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

