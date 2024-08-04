import pytest
from unittest.mock import Mock
from src.app.services.main_service import MainService
from src.app.services.notification_interface import NotificationInterface


def test_notify():
    # Arrange
    mock_notifier = Mock(spec=NotificationInterface)
    service = MainService(mock_notifier)

    # Act
    service.notify("Hello", "test@test.com")

    # Assert
    mock_notifier.send.assert_called_once_with(
        message="Hello", recipient="test@test.com")
