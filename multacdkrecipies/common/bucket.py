from aws_cdk import aws_s3 as s3


def base_bucket(construct, **kwargs):
    """
    Function that generates an S3 Bucket.
    :param construct: Custom construct that will use this function. From the external construct is usually 'self'.
    :param kwargs:
    :return: S3 Bucket Construct.
    """
    bucket_name = construct.prefix + "-" + kwargs["bucket_name"] + "-bucket-" + construct.environment_
    versioned = kwargs.get("versioned")
    public_read_access = kwargs["public_read_access"]
    cors_settings = kwargs.get("cors")
    website_error_document = kwargs.get("website", {}).get("error")
    website_index_document = kwargs.get("website", {}).get("index")

    if cors_settings is not None:
        allowed_methods = [value for value in list(s3.HttpMethods) if value.value in cors_settings["allowed_origins"]]
        cors_settings = s3.CorsRule(
            allowed_methods=cors_settings["allowed_methods"],
            allowed_origins=allowed_methods
        )
        cors_settings = [cors_settings]

    bucket = s3.Bucket(
        construct,
        id=bucket_name,
        bucket_name=bucket_name,
        cors=cors_settings,
        versioned=versioned,
        website_error_document=website_error_document,
        website_index_document=website_index_document
    )

    if public_read_access is True:
        bucket.grant_public_access()

    return bucket
