import json

import boto3
import pytest
from botocore.exceptions import ClientError

from aws_sm import SecretsManager


class TestSecretsManager:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.secret_name = "secret_name"
        self.secretsmanager = SecretsManager(
            "ap-northeast-1", "aws_acccess_key_id", "aws_secrets_key"
        )

    def test_basic_case_get_secret_value(self):
        data = {"SECRET_KEY": "secret_value", "ACCESS_KEY": "access_key"}

        res = self.secretsmanager.get_secret_value("SECRET_KEY", data)
        assert res == "secret_value"

    def test_nonexistent_secret_key_case_get_secret_value(self):
        data = {"SECRET_KEY": "secret_value", "ACCESS_KEY": "access_key"}

        with pytest.raises(KeyError):
            self.secretsmanager.get_secret_value("XXXXXXX", data)

    def test_basic_case_get_secret_values(self, mocker):
        data = {"SECRET_KEY": "secret_value"}
        mock_client = mocker.patch.object(boto3, "client")
        mock_client().get_secret_value.return_value = {"SecretString": json.dumps(data)}

        res = self.secretsmanager.get_secret_values(self.secret_name)
        assert res == data

    def test_different_secret_access_key_case_get_secret_values(self):
        secretsmanager = SecretsManager(
            "ap-northeast-1", "aws_acccess_key_id", "different_aws_secrets_key"
        )
        with pytest.raises(ClientError):
            secretsmanager.get_secret_values(self.secret_name)

    def test_incorrect_response_format_case_get_secret_values(self, mocker):
        mock_client = mocker.patch.object(boto3, "client")
        mock_client().get_secret_value.return_value = {
            "non-SecretString": {"SECRET_KEY": "secret_value"}
        }
        with pytest.raises(KeyError):
            self.secretsmanager.get_secret_values(self.secret_name)

    def test_json_decoding_fails_case_get_secret_values(self, mocker):
        data = "string response"
        mock_client = mocker.patch.object(boto3, "client")
        mock_client().get_secret_value.return_value = {"SecretString": data}

        with pytest.raises(json.JSONDecodeError):
            self.secretsmanager.get_secret_values(self.secret_name)
