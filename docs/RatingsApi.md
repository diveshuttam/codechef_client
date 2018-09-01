# codechef_client.RatingsApi

All URIs are relative to *https://api.codechef.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ratings_contest_type_get**](RatingsApi.md#ratings_contest_type_get) | **GET** /ratings/{contestType} | Return ratinglist for a particular contest type.


# **ratings_contest_type_get**
> InlineResponse20010 ratings_contest_type_get(contest_type, fields=fields, country=country, institution=institution, institution_type=institution_type, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)

Return ratinglist for a particular contest type.

Returns a ranklist of a contest according to the parameters provided. Contest types can be - all, cookOff, longChallenge, lunchTime, cookOffSchool, longChallengeSchool, lunchTimeSchool or allSchool.

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
api_instance = codechef_client.RatingsApi(codechef_client.ApiClient(configuration))
contest_type = 'contest_type_example' # str | enter contest type for which you want to fetch the ranklist- all, cookOff, longChallenge, lunchTime, cookOffSchool, longChallengeSchool, lunchTimeSchool, allSchool. 
fields = 'fields_example' # str | Possible fields are- username, globalRank, countryCode, countryRank, country, institution, institutionType, rating, diff.  Multiple fields can be entered using comma. (optional)
country = 'country_example' # str | filter by country: eg India (optional)
institution = 'institution_example' # str | filter by institution: eg Indian Institute of Technology Delhi.  (optional)
institution_type = 'institution_type_example' # str | filter by type of institute: eg: School, College or Organisation (optional)
offset = 56 # int | Starting index of list, eg. 3 (optional)
limit = 56 # int | Number of ratings in a list, max 25 (optional)
sort_by = 'globalRank' # str | Possible fields are- username, globalRank, rating, diff. Default = globalRank (optional) (default to globalRank)
sort_order = 'asc' # str | Possible fields are: asc or desc. Default = asc (optional) (default to asc)

try:
    # Return ratinglist for a particular contest type.
    api_response = api_instance.ratings_contest_type_get(contest_type, fields=fields, country=country, institution=institution, institution_type=institution_type, offset=offset, limit=limit, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingsApi->ratings_contest_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contest_type** | **str**| enter contest type for which you want to fetch the ranklist- all, cookOff, longChallenge, lunchTime, cookOffSchool, longChallengeSchool, lunchTimeSchool, allSchool.  | 
 **fields** | **str**| Possible fields are- username, globalRank, countryCode, countryRank, country, institution, institutionType, rating, diff.  Multiple fields can be entered using comma. | [optional] 
 **country** | **str**| filter by country: eg India | [optional] 
 **institution** | **str**| filter by institution: eg Indian Institute of Technology Delhi.  | [optional] 
 **institution_type** | **str**| filter by type of institute: eg: School, College or Organisation | [optional] 
 **offset** | **int**| Starting index of list, eg. 3 | [optional] 
 **limit** | **int**| Number of ratings in a list, max 25 | [optional] 
 **sort_by** | **str**| Possible fields are- username, globalRank, rating, diff. Default &#x3D; globalRank | [optional] [default to globalRank]
 **sort_order** | **str**| Possible fields are: asc or desc. Default &#x3D; asc | [optional] [default to asc]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[codechef_auth](../README.md#codechef_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

