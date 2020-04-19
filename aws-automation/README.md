# Install prowler role inside account(s)

```sh
aws cloudformation deploy \
  --template-file prowler-audit-role.template.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --stack-name prowler-audit-role \
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
      ProwlerCrossAccountAuditRoleName=prowler-audit-role
```