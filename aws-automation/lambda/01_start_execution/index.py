#
# Any code, applications, scripts, templates, proofs of concept, documentation
# and other items provided by AWS under this SOW are "AWS Content," as defined
# in the Agreement, and are provided for illustration purposes only. All such
# AWS Content is provided solely at the option of AWS, and is subject to the
# terms of the Addendum and the Agreement. Customer is solely responsible for
# using, deploying, testing, and supporting any code and applications provided
# by AWS under this SOW
#
import boto3
import os


codebuild = boto3.client("codebuild")


def handler(event, context):
    account_id = event["AccountId"]

    build_reponse = codebuild.start_build(
        projectName=os.environ["CodeBuildProjectName"],
        environmentVariablesOverride=[{
            "name": "RUNNING_ACCOUNT_ID",
            "value": account_id
        }]
    )

    return {
        "BuildId": build_reponse["build"]["id"]
    }