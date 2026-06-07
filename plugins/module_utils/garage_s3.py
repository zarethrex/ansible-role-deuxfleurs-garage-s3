# Common Functionality for Interacting with a Garage S3 instance

import garage_admin_sdk

def _get_client(
    host: str,
    access_token: str
) -> garage_admin_sdk.ApiClient:
    """Create API client."""
    _configuration = garage_admin_sdk.Configuration(
        host=host,
        access_token=access_token
    )
    return garage_admin_sdk.ApiClient(_configuration)


def get_buckets(
    host: str,
    access_token: str
) -> list[garage_admin_sdk.ListBucketsResponseItem]:
    """Retrieve list of available buckets."""
    _api_client = _get_client(
        host=host,
        access_token=access_token
    )
    _bucket_api = garage_admin_sdk.BucketApi(_api_client)
    return _bucket_api.list_buckets()


def create_bucket(
    name: str,
    *,
    host: str,
    access_token: str
) -> garage_admin_sdk.GetBucketInfoResponse:
    """Create new S3 bucket."""
    _api_client = _get_client(
        host=host,
        access_token=access_token
    )
    _bucket_api = garage_admin_sdk.BucketApi(_api_client)
    _request = garage_admin_sdk.CreateBucketRequest(globalAlias=name)
    return _bucket_api.create_bucket(_request)
