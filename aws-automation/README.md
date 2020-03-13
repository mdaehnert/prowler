# Setup

```sh
aws cloudformation deploy \
  --template-file template.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --stack-name prowler
```