import os
import setuptools


VERSION = os.environ.get("VERSION", "0.6.1")
CDK_VERSION = os.environ.get("CDK_VERSION", "1.51.0")

with open("./README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="multacdkrecipies",
    version=VERSION,
    author="Eugenio Efrain Breijo",
    author_email="eebf1993@gmail.com",
    description="A CDK Python Construct for AWS IoT Infrastructure",
    keywords=["aws", "aws-cdk", "cdk", "infrastructure", "cloudformation", "python", "constructs", "framework"],
    licence="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Eugenio Efrain Breijo",
    maintainer_email="eebf1993@gmail.com",
    url="https://github.com/u93/multacdkrecipies",
    packages=[
        "multacdkrecipies",
        "multacdkrecipies.utils",
        "multacdkrecipies.settings",
        "multacdkrecipies.common",
        "multacdkrecipies.scripts",
        "multacdkrecipies.scripts.iot_analytics_notebook",
    ],
    install_requires=[
        "appdirs==1.4.3",
        "attrs==19.3.0",
        f"aws-cdk.assets=={CDK_VERSION}",
        f"aws-cdk.aws-apigateway=={CDK_VERSION}",
        f"aws-cdk.aws-applicationautoscaling=={CDK_VERSION}",
        f"aws-cdk.aws-autoscaling-common=={CDK_VERSION}",
        f"aws-cdk.aws-codebuild=={CDK_VERSION}",
        f"aws-cdk.aws-codecommit=={CDK_VERSION}",
        f"aws-cdk.aws-codepipeline=={CDK_VERSION}",
        f"aws-cdk.aws-certificatemanager=={CDK_VERSION}",
        f"aws-cdk.aws-cloudformation=={CDK_VERSION}",
        f"aws-cdk.aws-cloudwatch=={CDK_VERSION}",
        f"aws-cdk.aws-cognito=={CDK_VERSION}",
        f"aws-cdk.aws-dynamodb=={CDK_VERSION}",
        f"aws-cdk.aws-ec2=={CDK_VERSION}",
        f"aws-cdk.aws-elasticloadbalancingv2=={CDK_VERSION}",
        f"aws-cdk.aws-events=={CDK_VERSION}",
        f"aws-cdk.aws-events-targets=={CDK_VERSION}",
        f"aws-cdk.aws-iam=={CDK_VERSION}",
        f"aws-cdk.aws-iot=={CDK_VERSION}",
        f"aws-cdk.aws-iotanalytics=={CDK_VERSION}",
        f"aws-cdk.aws-kinesis=={CDK_VERSION}",
        f"aws-cdk.aws-kinesisfirehose=={CDK_VERSION}",
        f"aws-cdk.aws-kms=={CDK_VERSION}",
        f"aws-cdk.aws-lambda=={CDK_VERSION}",
        f"aws-cdk.aws-lambda-event-sources=={CDK_VERSION}",
        f"aws-cdk.aws-logs=={CDK_VERSION}",
        f"aws-cdk.aws-route53=={CDK_VERSION}",
        f"aws-cdk.aws-s3=={CDK_VERSION}",
        f"aws-cdk.aws-s3-assets=={CDK_VERSION}",
        f"aws-cdk.aws-s3-notifications=={CDK_VERSION}",
        f"aws-cdk.aws-sagemaker=={CDK_VERSION}",
        f"aws-cdk.aws-sns=={CDK_VERSION}",
        f"aws-cdk.aws-sns-subscriptions=={CDK_VERSION}",
        f"aws-cdk.aws-sqs=={CDK_VERSION}",
        f"aws-cdk.aws-ssm=={CDK_VERSION}",
        f"aws-cdk.core=={CDK_VERSION}",
        f"aws-cdk.cx-api=={CDK_VERSION}",
        f"aws-cdk.region-info=={CDK_VERSION}",
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
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
