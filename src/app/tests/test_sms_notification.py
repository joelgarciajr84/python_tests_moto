from moto import mock_aws
from src.app.services.sms_notification import SMSNotification


@mock_aws
def test_sms_notification():

    # Arrange
    notifier = SMSNotification()

    # Act
    result = notifier.send("Hello", "+1234567890")

    # Assert

    assert result is True
