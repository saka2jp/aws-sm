import json
import unittest
from unittest.mock import patch

from botocore.exceptions import ClientError

from aws_sm import SecretsManager


class SecretsManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.secret_name = 'secret_name'
        self.secretsmanager = SecretsManager('ap-northeast-1', 'aws_acccess_key_id', 'aws_secrets_key')

    def test_basic_case_get_secret_value(self):
        data = {'SECRET_KEY': 'secret_value', 'ACCESS_KEY': 'access_key'}

        res = self.secretsmanager.get_secret_value('SECRET_KEY', data)
        self.assertEqual(res, 'secret_value')

    def test_nonexistent_secret_key_case_get_secret_value(self):
        data = {'SECRET_KEY': 'secret_value', 'ACCESS_KEY': 'access_key'}

        with self.assertRaises(KeyError):
            self.secretsmanager.get_secret_value('XXXXXXX', data)

    @patch('boto3.client')
    def test_basic_case_get_secret_values(self, mock_client):
        data = {'SECRET_KEY': 'secret_value'}
        mock_client().get_secret_value.return_value = {'SecretString': json.dumps(data)}
        res = self.secretsmanager.get_secret_values(self.secret_name)
        self.assertEqual(res, data)

    def test_different_secret_access_key_case_get_secret_values(self):
        secretsmanager = SecretsManager('ap-northeast-1', 'aws_acccess_key_id', 'different_aws_secrets_key')
        with self.assertRaises(ClientError):
            secretsmanager.get_secret_values(self.secret_name)

    @patch('boto3.client')
    def test_incorrect_response_format_case_get_secret_values(self, mock_client):
        mock_client().get_secret_value.return_value = {'non-SecretString': {'SECRET_KEY': 'secret_value'}}
        with self.assertRaises(KeyError):
            self.secretsmanager.get_secret_values(self.secret_name)

    @patch('boto3.client')
    def test_json_decoding_fails_case_get_secret_values(self, mock_client):
        data = 'string response'
        mock_client().get_secret_value.return_value = {'SecretString': data}

        with self.assertRaises(json.JSONDecodeError):
            self.secretsmanager.get_secret_values(self.secret_name)
