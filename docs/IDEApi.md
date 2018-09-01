# codechef_client.IDEApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ide_run_post**](IDEApi.md#ide_run_post) | **POST** /ide/run | Runs a code submitted by user.
[**ide_status_get**](IDEApi.md#ide_status_get) | **GET** /ide/status | Get status of submitted code.


# **ide_run_post**
> InlineResponse20022 ide_run_post(parameters)

Runs a code submitted by user.

Takes input, language and sourceCode

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
api_instance = codechef_client.IDEApi(codechef_client.ApiClient(configuration))
parameters = codechef_client.IdeRunSourceCode() # IdeRunSourceCode | Enter the source code, language, input to be executed. look at samples for example.

try:
    # Runs a code submitted by user.
    api_response = api_instance.ide_run_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IDEApi->ide_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**IdeRunSourceCode**](IdeRunSourceCode.md)| Enter the source code, language, input to be executed. look at samples for example. | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ide_status_get**
> InlineResponse20023 ide_status_get(link)

Get status of submitted code.

Takes link

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
api_instance = codechef_client.IDEApi(codechef_client.ApiClient(configuration))
link = 'link_example' # str | Enter status code recieved after code execution.    eg. VGQUp0

try:
    # Get status of submitted code.
    api_response = api_instance.ide_status_get(link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IDEApi->ide_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**| Enter status code recieved after code execution.    eg. VGQUp0 | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

