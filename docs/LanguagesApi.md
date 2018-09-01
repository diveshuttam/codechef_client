# codechef_client.LanguagesApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_get**](LanguagesApi.md#language_get) | **GET** /language | Get the list of languages on codechef.


# **language_get**
> InlineResponse2007 language_get(search=search, offset=offset, limit=limit)

Get the list of languages on codechef.

Returns a list of languages.

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
api_instance = codechef_client.LanguagesApi(codechef_client.ApiClient(configuration))
search = 'search_example' # str | Search string for language, eg. C (optional)
offset = 56 # int | Starting index of the list, eg. 3 (optional)
limit = 56 # int | Number of languages in the list, max 100 (optional)

try:
    # Get the list of languages on codechef.
    api_response = api_instance.language_get(search=search, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string for language, eg. C | [optional] 
 **offset** | **int**| Starting index of the list, eg. 3 | [optional] 
 **limit** | **int**| Number of languages in the list, max 100 | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

