from src.app.services.email_notification import EmailNotification
from moto import mock_aws
import boto3
from unittest.mock import patch
from botocore.exceptions import ClientError


@mock_aws
def test_email_notification():
    # Arrange
    ses = boto3.client("ses", region_name="us-east-1")
    ses.verify_email_identity(EmailAddress="test@example.com")

    emailNotification = EmailNotification()

    # Act
    result = emailNotification.send("Hello", "test@example.com")

    # Assert
    assert result == True