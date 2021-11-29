# import modules
from aws_cdk import (
    core,
    aws_ec2 as ec2,
)
from constants import constants

class VpcStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create the vpc
        self.kafka_vpc = ec2.Vpc(self, "kafka_vpc", max_azs=3,)
        core.Tag.add(self.kafka_vpc, "project", constants["PROJECT_TAG"])
        # add s3 endpoint
        self.kafka_vpc.add_gateway_endpoint(
            "e6ad3311-f566-426e-8291-6937101db6a1",
            service=ec2.GatewayVpcEndpointAwsService.S3,
        )

    # properties to share with other stacks ...
    @property
    def get_vpc(self):
        return self.kafka_vpc

    @property
    def get_vpc_public_subnet_ids(self):
        return self.kafka_vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnet_ids

    @property
    def get_vpc_private_subnet_ids(self):
        return self.kafka_vpc.select_subnets(
            subnet_type=ec2.SubnetType.PRIVATE
        ).subnet_ids