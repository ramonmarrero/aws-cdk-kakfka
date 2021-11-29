#!/usr/bin/env python3
import os

from aws_cdk import core

from vpc.vpc_stack import VpcStack
from kafka.kafka_stack import KafkaStack

app = core.App()
vpc_stack = VpcStack(
    app,
    "kafka-vpc",
    env=core.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

# Kafka stack
kafka_stack = KafkaStack(
    app,
    "kafka-cluster",
    vpc_stack,
    client=True,
    env=core.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)
kafka_stack.add_dependency(vpc_stack)


app.synth()
