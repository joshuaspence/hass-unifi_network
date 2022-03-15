import pytest


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):  # type: ignore[no-untyped-def]
    """Enable custom integrations in all tests."""
    yield
