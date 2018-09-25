import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class SecretsManager:

    def __init__(self, aws_region, aws_access_key_id=None, aws_secret_access_key=None):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region = aws_region

    def get_secret_values(self, secret_name):
        try:
            client = boto3.client(
                'secretsmanager',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.aws_region
            )
            resp = client.get_secret_value(SecretId=secret_name)
            secret_values = json.loads(resp['SecretString'])
        except ClientError:
            logger.exception(f'[Secrets Manager botocore.exceptions.ClientError] secret_name={secret_name}')
            raise
        except KeyError:
            logger.exception(f'[Secrets Manager KeyError] incorrect response format. secret_name={secret_name}')
            raise
        except json.JSONDecodeError:
            logger.exception(f'[Secrets Manager ValueError] JSON decoding fails secret_name={secret_name}')
            raise
        else:
            return secret_values

    def get_secret_value(self, secret_key, secret_values):
        try:
            secret = secret_values[secret_key]
        except KeyError:
            logger.exception(f'[Secrets Manager KeyError] secret_key does not exists. secret_key={secret_key}')
            raise
        else:
            return secret
