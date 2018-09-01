# codechef_client.UsersApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UsersApi.md#users_get) | **GET** /users | Get the list of users maximum 20.
[**users_me_get**](UsersApi.md#users_me_get) | **GET** /users/me | Fetches all the details of logged-in user.
[**users_username_get**](UsersApi.md#users_username_get) | **GET** /users/{username} | Fetches all the details of a user.


# **users_get**
> InlineResponse200 users_get(search, fields=fields, limit=limit, offset=offset)

Get the list of users maximum 20.

Search of users based on usernames. Possible fields- username, fullname, country, state, city, rankings, ratings, occupation, organisation, language

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
api_instance = codechef_client.UsersApi(codechef_client.ApiClient(configuration))
search = 'search_example' # str | Search string for username by any prefix of username, eg. search by hacker for usernames like hacker_ratty
fields = 'fields_example' # str | Possible fields are- username, fullname, country, state, city, rankings, ratings, occupation, organization, language.  Multiple fields can be entered using comma (optional)
limit = 56 # int | Limit of list, maximum 20, eg. 10 (optional)
offset = 56 # int | Starting index of list, eg. 5 (optional)

try:
    # Get the list of users maximum 20.
    api_response = api_instance.users_get(search, fields=fields, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string for username by any prefix of username, eg. search by hacker for usernames like hacker_ratty | 
 **fields** | **str**| Possible fields are- username, fullname, country, state, city, rankings, ratings, occupation, organization, language.  Multiple fields can be entered using comma | [optional] 
 **limit** | **int**| Limit of list, maximum 20, eg. 10 | [optional] 
 **offset** | **int**| Starting index of list, eg. 5 | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_get**
> InlineResponse2001 users_me_get()

Fetches all the details of logged-in user.

Fetches all the details of logged-in user.

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
api_instance = codechef_client.UsersApi(codechef_client.ApiClient(configuration))

try:
    # Fetches all the details of logged-in user.
    api_response = api_instance.users_me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_username_get**
> InlineResponse2001 users_username_get(username, fields=fields)

Fetches all the details of a user.

Complete detail of a user. Possible fields are- username, fullname, country, state, city, rankings, ratings, occupation, organization, language

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
api_instance = codechef_client.UsersApi(codechef_client.ApiClient(configuration))
username = 'username_example' # str | Username of the user, eg. hacker_ratty
fields = 'fields_example' # str | Possible fields are - username, fullname, country, state, city, rankings, ratings, occupation, language, organization, problemStats, submissionStats.  Multiple fields can be entered using comma (optional)

try:
    # Fetches all the details of a user.
    api_response = api_instance.users_username_get(username, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the user, eg. hacker_ratty | 
 **fields** | **str**| Possible fields are - username, fullname, country, state, city, rankings, ratings, occupation, language, organization, problemStats, submissionStats.  Multiple fields can be entered using comma | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

