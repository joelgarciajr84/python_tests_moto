from src.app.services.notification_interface import NotificationInterface


class MainService:

    def __init__(self, notifier: NotificationInterface):
        self.notifier = notifier

    def notify(self, message: str, recipient: str) -> None:
        self.notifier.send(message=message, recipient=recipient)
