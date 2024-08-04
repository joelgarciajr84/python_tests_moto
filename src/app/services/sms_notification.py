import boto3
from src.app.services.notification_interface import NotificationInterface
from botocore.exceptions import ClientError


class SMSNotification(NotificationInterface):

    def __init__(self):
        self.client = boto3.client('sns', region_name='us-east-1')

    def send(self, message: str, recipient: str) -> None:
        try:
            response = self.client.publish(
                PhoneNumber=recipient,
                Message=message
            )
            print(f"SMS sent! Message ID: {response['MessageId']}")

            return True
        except ClientError as e:
            print(f"Failed to send SMS: {e}")
            return False
