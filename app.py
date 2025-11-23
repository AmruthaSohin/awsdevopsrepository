#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_hands_on.cdk_hands_on_stack import CdkHandsOnStack

app = cdk.App()

CdkHandsOnStack(
    app,
    "CdkHandsOnStack",
    env=cdk.Environment(
        account="061051234712",
        region="us-east-1"
    )
)

app.synth()
