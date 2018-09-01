# codechef_client.TagsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_problems_get**](TagsApi.md#tags_problems_get) | **GET** /tags/problems | Get list of tags for a given problem.


# **tags_problems_get**
> InlineResponse20011 tags_problems_get(filter=filter, fields=fields, limit=limit, offset=offset)

Get list of tags for a given problem.

Fetches all the problem related tags

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
api_instance = codechef_client.TagsApi(codechef_client.ApiClient(configuration))
filter = 'filter_example' # str | Takes comma separated tags/authors. eg: jan13,kingofnumbers (optional)
fields = 'fields_example' # str | Possible fields are- code, tags, author, solved, attempted, partiallySolved. Multiple fields can be entered using comma. (optional)
limit = 56 # int | Limit of list, maximum 20, eg. 10 (optional)
offset = 56 # int | Starting index of list, eg. 5 (optional)

try:
    # Get list of tags for a given problem.
    api_response = api_instance.tags_problems_get(filter=filter, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Takes comma separated tags/authors. eg: jan13,kingofnumbers | [optional] 
 **fields** | **str**| Possible fields are- code, tags, author, solved, attempted, partiallySolved. Multiple fields can be entered using comma. | [optional] 
 **limit** | **int**| Limit of list, maximum 20, eg. 10 | [optional] 
 **offset** | **int**| Starting index of list, eg. 5 | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

