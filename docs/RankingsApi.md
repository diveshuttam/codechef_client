# codechef_client.RankingsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankings_contest_code_get**](RankingsApi.md#rankings_contest_code_get) | **GET** /rankings/{contestCode} | Return ranklist for a particular contest.


# **rankings_contest_code_get**
> InlineResponse2009 rankings_contest_code_get(contest_code, fields=fields, country=country, institution=institution, institution_type=institution_type, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)

Return ranklist for a particular contest.

Returns a ranklist of a contest according to the parameters provided.

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
api_instance = codechef_client.RankingsApi(codechef_client.ApiClient(configuration))
contest_code = 'contest_code_example' # str | Contest code, eg. JAN13
fields = 'fields_example' # str | Possible fields are- rank, username, totalTime, penalty, country, countryCode, institution, rating, institutionType, contestId, contestCode, totalScore, problemScore. Multiple fields can be entered using comma. (optional)
country = 'country_example' # str | Country to which the user belongs, eg. India (optional)
institution = 'institution_example' # str | Institution to which the user belongs, eg. Jaypee Institute of Information Technology (optional)
institution_type = 'institution_type_example' # str | Possible values: school, college or organization. (optional)
offset = 56 # int | Starting index of rankings (optional)
limit = 56 # int | Number of rankings in the list, max 25 (optional)
sort_by = 'sort_by_example' # str | Possible fields are: rank. (optional)
sort_order = 'asc' # str | Possible fields are: asc or desc. Default = asc (optional) (default to asc)

try:
    # Return ranklist for a particular contest.
    api_response = api_instance.rankings_contest_code_get(contest_code, fields=fields, country=country, institution=institution, institution_type=institution_type, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->rankings_contest_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contest_code** | **str**| Contest code, eg. JAN13 | 
 **fields** | **str**| Possible fields are- rank, username, totalTime, penalty, country, countryCode, institution, rating, institutionType, contestId, contestCode, totalScore, problemScore. Multiple fields can be entered using comma. | [optional] 
 **country** | **str**| Country to which the user belongs, eg. India | [optional] 
 **institution** | **str**| Institution to which the user belongs, eg. Jaypee Institute of Information Technology | [optional] 
 **institution_type** | **str**| Possible values: school, college or organization. | [optional] 
 **offset** | **int**| Starting index of rankings | [optional] 
 **limit** | **int**| Number of rankings in the list, max 25 | [optional] 
 **sort_by** | **str**| Possible fields are: rank. | [optional] 
 **sort_order** | **str**| Possible fields are: asc or desc. Default &#x3D; asc | [optional] [default to asc]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

