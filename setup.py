import os
import setuptools


VERSION = os.environ.get("VERSION", "0.0.1")

with open("./README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="multa-cdk-recipies",
    version=VERSION,
    url="http://cdkrecipies.s3-website-us-east-1.amazonaws.com",
    description="A CDK Python Construct for AWS IoT Infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Eugenio Efrain Breijo",
    author_email="eebf1993@gmail.com",
    packages=["multa-cdk-recipies", "multa-cdk-recipies.utils", "multa-cdk-recipies.settings"],
    install_requires=[
        "appdirs==1.4.3",
        "attrs==19.3.0",
        "aws-cdk.assets==1.22.0",
        "aws-cdk.aws-apigateway==1.22.0",
        "aws-cdk.aws-applicationautoscaling==1.22.0",
        "aws-cdk.aws-autoscaling-common==1.22.0",
        "aws-cdk.aws-certificatemanager==1.22.0",
        "aws-cdk.aws-cloudformation==1.22.0",
        "aws-cdk.aws-cloudwatch==1.22.0",
        "aws-cdk.aws-dynamodb==1.22.0",
        "aws-cdk.aws-ec2==1.22.0",
        "aws-cdk.aws-elasticloadbalancingv2==1.22.0",
        "aws-cdk.aws-events==1.22.0",
        "aws-cdk.aws-iam==1.22.0",
        "aws-cdk.aws-iot==1.21.1",
        "aws-cdk.aws-iotanalytics==1.22.0",
        "aws-cdk.aws-kinesis==1.22.0",
        "aws-cdk.aws-kms==1.22.0",
        "aws-cdk.aws-lambda==1.22.0",
        "aws-cdk.aws-lambda-event-sources==1.22.0",
        "aws-cdk.aws-logs==1.22.0",
        "aws-cdk.aws-route53==1.22.0",
        "aws-cdk.aws-s3==1.22.0",
        "aws-cdk.aws-s3-assets==1.22.0",
        "aws-cdk.aws-s3-notifications==1.22.0",
        "aws-cdk.aws-sagemaker==1.22.0",
        "aws-cdk.aws-sns==1.22.0",
        "aws-cdk.aws-sns-subscriptions==1.22.0",
        "aws-cdk.aws-sqs==1.22.0",
        "aws-cdk.aws-ssm==1.22.0",
        "aws-cdk.core==1.22.0",
        "aws-cdk.cx-api==1.22.0",
        "aws-cdk.region-info==1.22.0",
        "black==19.10b0",
        "boto3==1.11.7",
        "botocore==1.14.7",
        "cattrs==1.0.0",
        "Click==7.0",
        "contextlib2==0.5.5",
        "docutils==0.15.2",
        "Jinja2==2.10.3",
        "jmespath==0.9.4",
        "jsii==0.21.2",
        "MarkupSafe==1.1.1",
        "pathspec==0.7.0",
        "publication==0.0.3",
        "python-dateutil==2.8.1",
        "regex==2020.1.8",
        "s3pypi==0.10.1",
        "s3transfer==0.3.1",
        "schema==0.7.1",
        "six==1.14.0",
        "toml==0.10.0",
        "typed-ast==1.4.1",
        "typing-extensions==3.7.4.1",
        "urllib3==1.25.8",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)