from typing import Generator
from unittest.mock import MagicMock

import pytest
from pyunifi.controller import Controller


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations: None) -> Generator:
    """Enable custom integrations in all tests."""
    yield


@pytest.fixture
def controller() -> Controller:
    return MagicMock()
