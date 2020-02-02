from aws_cdk import (
    core,
    aws_iotanalytics as analytics,
)

from .utils import IOT_ANALYTICS_FAN_OUT, validate_configuration, WrongTypeException


class AwsIotAnalyticsFanOut(core.Construct):
    """
    AWS CDK Construct that defines a pipe where a Rules captures an MQTT Message sent to or from AWS IoT MQTT Broker,
    then the message is sent to an SQS Queue and a Lambda function subscribed to the topic can process it and take
    proper actions. The construct takes a few inputs.

    Attributes:
        prefix (str): The prefix set on the name of each resource created in the stack. Just for organization purposes.
        environment_ (str): The environment that all resources will use. Also for organizational and testing purposes.

    """

    def __init__(self, scope: core.Construct, id: str, *, prefix: str, environment: str, configuration, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.prefix = prefix
        self.environment_ = environment
        validate_configuration(configuration_schema=IOT_ANALYTICS_FAN_OUT, configuration_received=configuration)

        # Defining Channel
        channel_name = self.prefix + "_" + configuration["channel_name"] + "_channel_" + self.environment_
        self._channel = analytics.CfnChannel(self, id=channel_name, channel_name=channel_name)

        self._datastore_pipes = list()
        for datastore_pipe in configuration["datastore_pipe_definition"]:
            extra_activities = datastore_pipe["extra_activities"]
            base_name = datastore_pipe["name"]

            # Defining Datastore
            datastore_name = self.prefix + "_" + base_name + "_datastore_" + self.environment_
            datastore = analytics.CfnDatastore(self, id=datastore_name, datastore_name=datastore_name)

            # Defining Pipeline Properties
            pipeline_activities = list()

            # Defining Channel Activity Property
            channel_activity_property = analytics.CfnPipeline.ChannelProperty(
                channel_name=self._channel.channel_name, name=self._channel.channel_name, next=datastore.datastore_name,
            )
            pipeline_channel_activity = analytics.CfnPipeline.ActivityProperty(channel=channel_activity_property)
            pipeline_activities.append(pipeline_channel_activity)

            # Defining Datastore Activity Property
            datastore_activity_property = analytics.CfnPipeline.DatastoreProperty(
                datastore_name=datastore.datastore_name, name=datastore.datastore_name
            )
            pipeline_datastore_activity = analytics.CfnPipeline.ActivityProperty(datastore=datastore_activity_property)
            pipeline_activities.append(pipeline_datastore_activity)

            # Appending extra Pipeline Activities
            pipeline_activities.extend(extra_activities)

            # Defining Pipeline
            pipeline_name = self.prefix + "_" + base_name + "_pipeline_" + self.environment_
            pipeline = analytics.CfnPipeline(
                self, id=pipeline_name, pipeline_name=pipeline_name, pipeline_activities=pipeline_activities
            )
            pipeline.add_depends_on(target=datastore)
            pipeline.add_depends_on(target=self._channel)

            self._datastore_pipes.append(dict(datastore=datastore, pipeline=pipeline))

    @property
    def channel(self):
        return self._channel

    @property
    def datastore_pipes(self):
        return self._datastore_pipes