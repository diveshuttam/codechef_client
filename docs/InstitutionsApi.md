# codechef_client.InstitutionsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**institution_get**](InstitutionsApi.md#institution_get) | **GET** /institution | Get the list of institutions on codechef.


# **institution_get**
> InlineResponse2006 institution_get(search, offset=offset, limit=limit)

Get the list of institutions on codechef.

Returns a list of instituitions.

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
api_instance = codechef_client.InstitutionsApi(codechef_client.ApiClient(configuration))
search = 'search_example' # str | Search string for institution, eg. jaypee
offset = 56 # int | Starting index of the list (optional)
limit = 56 # int | Number of entities to be fetched, max 100 (optional)

try:
    # Get the list of institutions on codechef.
    api_response = api_instance.institution_get(search, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string for institution, eg. jaypee | 
 **offset** | **int**| Starting index of the list | [optional] 
 **limit** | **int**| Number of entities to be fetched, max 100 | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

