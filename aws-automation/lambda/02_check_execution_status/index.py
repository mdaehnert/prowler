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


codebuild = boto3.client("codebuild")


def handler(event, context):
    print(event)

    build_id = event["BuildId"]

    build = codebuild.batch_get_builds(
        ids=[build_id]
    )["builds"][0]

    return {
        "Status": build["buildStatus"]
    }
