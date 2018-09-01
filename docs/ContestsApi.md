# codechef_client.ContestsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contests_contest_code_get**](ContestsApi.md#contests_contest_code_get) | **GET** /contests/{contestCode} | Get contest details.
[**contests_get**](ContestsApi.md#contests_get) | **GET** /contests | Get the list of contests.


# **contests_contest_code_get**
> InlineResponse2003 contests_contest_code_get(contest_code, fields=fields, sort_by=sort_by, sort_order=sort_order)

Get contest details.

Takes contestCode as a parameter and fetches contest details.

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
api_instance = codechef_client.ContestsApi(codechef_client.ApiClient(configuration))
contest_code = 'contest_code_example' # str | Code of the contest. e.g. -> JAN17 for January Long Challenge, 2017
fields = 'fields_example' # str | Possible fields are- code, name, startDate, endDate, type, bannerFile, freezingTime, announcements, problemsList.  Multiple fields can be entered using comma. (optional)
sort_by = 'successfulSubmissions' # str | Possible fields are- problemName, problemCode, successfulSubmissions,  accuracy.  Default = successfulSubmissions (optional) (default to successfulSubmissions)
sort_order = 'desc' # str | Possible fields are: asc or desc.  Default = desc (optional) (default to desc)

try:
    # Get contest details.
    api_response = api_instance.contests_contest_code_get(contest_code, fields=fields, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContestsApi->contests_contest_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contest_code** | **str**| Code of the contest. e.g. -&gt; JAN17 for January Long Challenge, 2017 | 
 **fields** | **str**| Possible fields are- code, name, startDate, endDate, type, bannerFile, freezingTime, announcements, problemsList.  Multiple fields can be entered using comma. | [optional] 
 **sort_by** | **str**| Possible fields are- problemName, problemCode, successfulSubmissions,  accuracy.  Default &#x3D; successfulSubmissions | [optional] [default to successfulSubmissions]
 **sort_order** | **str**| Possible fields are: asc or desc.  Default &#x3D; desc | [optional] [default to desc]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contests_get**
> InlineResponse2002 contests_get(fields=fields, status=status, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)

Get the list of contests.

Returns a list of contests.

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
api_instance = codechef_client.ContestsApi(codechef_client.ApiClient(configuration))
fields = 'fields_example' # str | Possible fields are- code, name, startDate, endDate.  Multiple fields can be entered using comma. (optional)
status = 'status_example' # str | Possible values: past, present, future (optional)
offset = 56 # int | Starting index of the list, eg. 4 (optional)
limit = 56 # int | Number of contests in a list eg. 10 (optional)
sort_by = 'startDate' # str | Possible fields are- code, name, startDate, endDate. Default = startDate (optional) (default to startDate)
sort_order = 'sort_order_example' # str | Possible fields are: asc or desc. Default = desc (optional)

try:
    # Get the list of contests.
    api_response = api_instance.contests_get(fields=fields, status=status, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContestsApi->contests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Possible fields are- code, name, startDate, endDate.  Multiple fields can be entered using comma. | [optional] 
 **status** | **str**| Possible values: past, present, future | [optional] 
 **offset** | **int**| Starting index of the list, eg. 4 | [optional] 
 **limit** | **int**| Number of contests in a list eg. 10 | [optional] 
 **sort_by** | **str**| Possible fields are- code, name, startDate, endDate. Default &#x3D; startDate | [optional] [default to startDate]
 **sort_order** | **str**| Possible fields are: asc or desc. Default &#x3D; desc | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

