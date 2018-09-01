# codechef_client.ProblemsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**problems_category_name_get**](ProblemsApi.md#problems_category_name_get) | **GET** /problems/{categoryName} | Get the list of problems for given categoryName.


# **problems_category_name_get**
> InlineResponse2008 problems_category_name_get(category_name, fields=fields, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)

Get the list of problems for given categoryName.

Returns a list of Problems according to the catergory name provided.

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
api_instance = codechef_client.ProblemsApi(codechef_client.ApiClient(configuration))
category_name = 'category_name_example' # str | Possible categories are: school, easy, medium, hard, challenge, extcontest
fields = 'fields_example' # str | Possible fields are problemCode, problemName, successfulSubmissions, accuracy. Multiple fields can be entered using comma. (optional)
offset = 56 # int | Starting index of the list, eg. 3 (optional)
limit = 56 # int | Number of problems in a list, max 100 (optional)
sort_by = 'successfulSubmissions' # str | Possible fields are -problemCode, problemName, successfulSubmissions, accuracy.  (optional) (default to successfulSubmissions)
sort_order = 'sort_order_example' # str | Possible fields are: asc or desc , Default = asc (optional)

try:
    # Get the list of problems for given categoryName.
    api_response = api_instance.problems_category_name_get(category_name, fields=fields, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemsApi->problems_category_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_name** | **str**| Possible categories are: school, easy, medium, hard, challenge, extcontest | 
 **fields** | **str**| Possible fields are problemCode, problemName, successfulSubmissions, accuracy. Multiple fields can be entered using comma. | [optional] 
 **offset** | **int**| Starting index of the list, eg. 3 | [optional] 
 **limit** | **int**| Number of problems in a list, max 100 | [optional] 
 **sort_by** | **str**| Possible fields are -problemCode, problemName, successfulSubmissions, accuracy.  | [optional] [default to successfulSubmissions]
 **sort_order** | **str**| Possible fields are: asc or desc , Default &#x3D; asc | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

