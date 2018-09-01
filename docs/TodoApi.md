# codechef_client.TodoApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todo_add_post**](TodoApi.md#todo_add_post) | **POST** /todo/add | Adds a problem to todo list.
[**todo_delete_all_delete**](TodoApi.md#todo_delete_all_delete) | **DELETE** /todo/delete/all | Deletes all the problems added to the todo list.
[**todo_delete_delete**](TodoApi.md#todo_delete_delete) | **DELETE** /todo/delete/ | Deletes a problem added to the todo list.
[**todo_problems_get**](TodoApi.md#todo_problems_get) | **GET** /todo/problems | Gets problems listed in todo.


# **todo_add_post**
> list[InlineResponse20015] todo_add_post(parameters)

Adds a problem to todo list.

Takes problemCode and contestCode of the problem to be added. Look at the samples for example

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
api_instance = codechef_client.TodoApi(codechef_client.ApiClient(configuration))
parameters = codechef_client.AddTodoParameters() # AddTodoParameters | Takes problemCode, contestCode

try:
    # Adds a problem to todo list.
    api_response = api_instance.todo_add_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodoApi->todo_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**AddTodoParameters**](AddTodoParameters.md)| Takes problemCode, contestCode | 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todo_delete_all_delete**
> list[InlineResponse20016] todo_delete_all_delete()

Deletes all the problems added to the todo list.

Takes no parameters.

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
api_instance = codechef_client.TodoApi(codechef_client.ApiClient(configuration))

try:
    # Deletes all the problems added to the todo list.
    api_response = api_instance.todo_delete_all_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodoApi->todo_delete_all_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20016]**](InlineResponse20016.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todo_delete_delete**
> list[InlineResponse20016] todo_delete_delete(problem_code)

Deletes a problem added to the todo list.

Takes problem code as parameter.

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
api_instance = codechef_client.TodoApi(codechef_client.ApiClient(configuration))
problem_code = 'problem_code_example' # str | Username of the user.

try:
    # Deletes a problem added to the todo list.
    api_response = api_instance.todo_delete_delete(problem_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodoApi->todo_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_code** | **str**| Username of the user. | 

### Return type

[**list[InlineResponse20016]**](InlineResponse20016.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todo_problems_get**
> InlineResponse20014 todo_problems_get(fields=fields)

Gets problems listed in todo.

Takes no paramters

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
api_instance = codechef_client.TodoApi(codechef_client.ApiClient(configuration))
fields = 'fields_example' # str | Possible fields are- problemCode, contestCode, creationTime, status, tags, problemName, contestUrl, problemUrl, problemRedirect. Multiple fields can be entered using comma. (optional)

try:
    # Gets problems listed in todo.
    api_response = api_instance.todo_problems_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodoApi->todo_problems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Possible fields are- problemCode, contestCode, creationTime, status, tags, problemName, contestUrl, problemUrl, problemRedirect. Multiple fields can be entered using comma. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

