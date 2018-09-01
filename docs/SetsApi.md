# codechef_client.SetsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sets_add_post**](SetsApi.md#sets_add_post) | **POST** /sets/add | Adds set to the user&#39;s account to whom the access token being used belongs.
[**sets_delete_delete**](SetsApi.md#sets_delete_delete) | **DELETE** /sets/delete | Deletes set from the user&#39;s account to whom the access token belongs.
[**sets_get**](SetsApi.md#sets_get) | **GET** /sets/ | Get set details for logged in user
[**sets_members_add_post**](SetsApi.md#sets_members_add_post) | **POST** /sets/members/add | Adds set members to an existing set of the user to whom the access token belongs.
[**sets_members_delete_delete**](SetsApi.md#sets_members_delete_delete) | **DELETE** /sets/members/delete | Removes members belonging to a set.
[**sets_members_get_get**](SetsApi.md#sets_members_get_get) | **GET** /sets/members/get | Get set details for particular sets of the logged in user
[**sets_update_put**](SetsApi.md#sets_update_put) | **PUT** /sets/update | Updates set of the logged in user&#39;s account.


# **sets_add_post**
> list[InlineResponse20018] sets_add_post(parameters)

Adds set to the user's account to whom the access token being used belongs.

Takes setName, description as parameters and adds the set to user's account. Look at samples for example

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
parameters = codechef_client.AddSetParameters() # AddSetParameters | Takes setName and description

try:
    # Adds set to the user's account to whom the access token being used belongs.
    api_response = api_instance.sets_add_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**AddSetParameters**](AddSetParameters.md)| Takes setName and description | 

### Return type

[**list[InlineResponse20018]**](InlineResponse20018.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_delete_delete**
> list[InlineResponse20019] sets_delete_delete(set_name)

Deletes set from the user's account to whom the access token belongs.

Takes setName as condition parameters to delete the set from the user's account.

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
set_name = 'set_name_example' # str | Enter the name of the set you want to delete

try:
    # Deletes set from the user's account to whom the access token belongs.
    api_response = api_instance.sets_delete_delete(set_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_name** | **str**| Enter the name of the set you want to delete | 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_get**
> InlineResponse20017 sets_get(fields=fields)

Get set details for logged in user

Shows all the sets created by user to whom the access token being used belongs.

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
fields = 'fields_example' # str | Possible fields are: setName, description. (optional)

try:
    # Get set details for logged in user
    api_response = api_instance.sets_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Possible fields are: setName, description. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_members_add_post**
> InlineResponse20021 sets_members_add_post(parameters)

Adds set members to an existing set of the user to whom the access token belongs.

Takes setName, memberHandle(username of the member to be added) as parameters. Look at samples for example

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
parameters = codechef_client.AddSetMemberParameters() # AddSetMemberParameters | Takes setName and memberHandle

try:
    # Adds set members to an existing set of the user to whom the access token belongs.
    api_response = api_instance.sets_members_add_post(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_members_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**AddSetMemberParameters**](AddSetMemberParameters.md)| Takes setName and memberHandle | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_members_delete_delete**
> InlineResponse20021 sets_members_delete_delete(set_name, member_handle)

Removes members belonging to a set.

Takes setName, memberHandle as parameters

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
set_name = 'set_name_example' # str | Enter the set name whose set member you want to delete.
member_handle = 'member_handle_example' # str | Enter the username of the set member you want to remove from set.

try:
    # Removes members belonging to a set.
    api_response = api_instance.sets_members_delete_delete(set_name, member_handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_members_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_name** | **str**| Enter the set name whose set member you want to delete. | 
 **member_handle** | **str**| Enter the username of the set member you want to remove from set. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_members_get_get**
> InlineResponse20020 sets_members_get_get(set_name, fields=fields)

Get set details for particular sets of the logged in user

Shows the details of the set.

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
set_name = 'set_name_example' # str | Set name whose member information is required.
fields = 'fields_example' # str | Possible fields are: setName, memberName, country, allContestRating,longContestRating, shortContestRating, lTimeContestRating, allSchoolContestRating, longSchoolContestRating, shortSchoolContestRating, lTimeSchoolContestRating. Multiple fields can be entered using comma. (optional)

try:
    # Get set details for particular sets of the logged in user
    api_response = api_instance.sets_members_get_get(set_name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_members_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_name** | **str**| Set name whose member information is required. | 
 **fields** | **str**| Possible fields are: setName, memberName, country, allContestRating,longContestRating, shortContestRating, lTimeContestRating, allSchoolContestRating, longSchoolContestRating, shortSchoolContestRating, lTimeSchoolContestRating. Multiple fields can be entered using comma. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_update_put**
> list[InlineResponse20019] sets_update_put(parameters)

Updates set of the logged in user's account.

Takes setName as condition parameters and setName and/or description as extraParameters to update the set in user's account. Look at samples for example

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
api_instance = codechef_client.SetsApi(codechef_client.ApiClient(configuration))
parameters = codechef_client.UpdateSetParameters() # UpdateSetParameters | Takes setName and description

try:
    # Updates set of the logged in user's account.
    api_response = api_instance.sets_update_put(parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetsApi->sets_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**UpdateSetParameters**](UpdateSetParameters.md)| Takes setName and description | 

### Return type

[**list[InlineResponse20019]**](InlineResponse20019.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

