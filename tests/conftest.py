from unittest.mock import MagicMock

import pytest
from pyunifi.controller import Controller


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):  # type: ignore[no-untyped-def]
    """Enable custom integrations in all tests."""
    yield


@pytest.fixture
def controller() -> Controller:
    return MagicMock()
