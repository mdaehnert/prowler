# Install prowler role inside account(s)

```sh
aws cloudformation deploy \
  --template-file prowler-audit-role.template.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --stack-name prowler-access \
  --parameter-overrides \
      AutomationAccountId=123456789012 \
      ProwlerAuditRoleName=prowler-audit-role
```


# Setup prowler automation

```sh
aws cloudformation package \
  --template-file automation.template.yml \
  --s3-bucket LAMBDA_ARTIFACT_BUCKETNAME \
  --output-template-file .packaged-automation.template.yml \
&& \
aws cloudformation deploy \
  --template-file .packaged-automation.template.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --stack-name prowler-automation \
  --parameter-overrides \
      ProwlerCrossAccountAuditRoleName=prowler-audit-role \
      DoRunProwlerRegularly=true|false \
      ProwlerRunCronExpression=...

```



# Execution

## via CodeBuild

Execution of a single prowler run can be started via CodeBuild.
Parameters are:
* RUNNING_ACCOUNT_ID - Default is current account. Can be changed to run prowler inside any account where it's allowed to. (@see next parameter)
* PROWLER_ROLE_NAME - Role name to assume by prowler. It can be either setup in the CodeBuild's account or another via cross-account access. 

[](./_doc/)

## via Step Functions
```json
{
  "Accounts": [{
    "AccountId": "123456789012"
  }, {
    "AccountId": "999999999999"
  }]
}
 ```

## via CloudWatch Scheduled Event

Execution of a Prowler on a regular (scheduled) basis is also possible. Activate this feature you need to:
1. Define DoRunProwlerRegularly=true on the prowler automation CFN stack
2. Define ProwlerRunCronExpression for the schedule
3. Go into the CloudWatch event an define the inpupt text as you would do with the Step Function itself.

After that, CloudWatch Event rule will trigger prowler runs on the scheduled basis automatically.