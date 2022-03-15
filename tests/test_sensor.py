from unittest.mock import MagicMock

from custom_components.unifi_network.sensor import (
    DEFAULT_NAME,
    SENSOR_WWW,
    UnifiNetworkSensor,
)


async def test_sensor(hass):  # type: ignore[no-untyped-def]
    controller = MagicMock()

    sensor = UnifiNetworkSensor(hass, controller, DEFAULT_NAME, SENSOR_WWW)
    sensor.update()

    assert sensor.state is None
