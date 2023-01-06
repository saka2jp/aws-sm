[![test](https://github.com/saka2jp/aws-sm/actions/workflows/test.yml/badge.svg)](https://github.com/saka2jp/aws-sm/actions/workflows/test.yml) [![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT) [![Downloads](https://pepy.tech/badge/aws-sm)](https://pepy.tech/project/aws-sm)

# aws-sm

A Python wrapper around [AWS Secrets Manager](https://aws.amazon.com/jp/secrets-manager/) using Boto3.

# Installation

Installing from PyPI is as easy as doing:

```sh
$ pip install aws-sm
```

# Usage

```python
from aws_sm import SecretsManager

AWS_ACCESS_KEY_ID = ***************
AWS_SECRET_ACCESS_KEY = ***************

secretsmanager = SecretsManager('us-east-1', AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
secrets = secretsmanager.get_secret_values('tutorials/MyFristTutorialSecret')

USER_NAME = secretsmanager.get_secret_value('USER_NAME', secrets)
PASSWORD = secretsmanager.get_secret_value('PASSWORD', secrets)
```

This is sample code using aws-sm to get `USER_NAME` and `PASSWORD` from `tutorials/MyFristTutorialSecret`.

`USER_NAME` and `PASSWORD` are `Secret value`.  
`tutorials/MyFristTutorialSecret` is `Secret name`.

<img width="990" alt="0030-09-25 22 32 21" src="https://user-images.githubusercontent.com/24784855/46020218-d4e5b580-c118-11e8-9aa7-69edbecb8de2.png">

This is AWS Console of Secrets Manager.

`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are unnecessary when attaching the appropriate IAM Role. The default policy is [SecretsManagerReadWrite](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_identity-based-policies.html).

# Set Up Loacally

Make sure you have [Docker Compose](https://docs.docker.com/compose/install/).

```sh
$ docker-compose up
```

## Run test

```sh
$ docker-compose exec app bash
root@d5d52d6765d9:/app# py.test -v
```
