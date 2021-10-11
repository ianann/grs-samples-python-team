import random
import string
import setup_catalog

from google.api_core.client_options import ClientOptions

from google.cloud.retail_v2 import SearchServiceClient, SearchRequest

project_number = "SET HERE VALID PROJECT NUMBER"
endpoint = "retail.googleapis.com"
isolation_filter_key = "INTEGRATION_FILTER_KEY"
title_query = "Nest_Maxi"
visitor_id = "visitor"
test_id = ''.join(random.sample(string.ascii_lowercase, 1))

# [START search_client]
default_search_placement = "projects" + project_number + "locations/global/catalogs/default_catalog/placements/default_search"


def get_search_service_client():
    client_options = ClientOptions(endpoint)
    return SearchServiceClient(client_options=client_options)


# [END search_client]


def build_isolation_filter(test__id: str):
    return 'attributes.{0}: ANY("{1}")'.format(isolation_filter_key, test__id)


# [START search_product_with_boost_spec]
def search_products_with_boost_spec(query: str, _condition: str, _boost_strength: float):
    boost_spec = SearchRequest().BoostSpec()

    boost_spec.ConditionBoostSpec().condition = _condition
    boost_spec.ConditionBoostSpec.boost = _boost_strength

    search_request = SearchRequest()
    search_request.placement = default_search_placement
    search_request.query = query
    search_request.filter = build_isolation_filter(test_id)
    search_request.visitor_id = visitor_id
    search_request.boost_spec = boost_spec
    print("---search request---")
    print(search_request)

    return get_search_service_client().search(search_request)


# [END search_product_with_boost_spec]

def search():
    setup_catalog.ingest_products(test_id)
    
    # [TRY DIFFERENT BOOST CONDITIONS HERE:]
    condition = "(colorFamily: ANY(\"blue\"))"
    boost = 0.5
    
    search_response = search_products_with_boost_spec(title_query, condition, boost)
    print("---boost search response---")
    print(search_response)

    setup_catalog.delete_products()


search()
