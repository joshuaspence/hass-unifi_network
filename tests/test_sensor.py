from custom_components.unifi_network.sensor import (
    DEFAULT_NAME,
    SENSOR_WWW,
    UnifiNetworkSensor,
)
from unittest.mock import MagicMock


async def test_sensor(hass):
    controller = MagicMock()

    sensor = UnifiNetworkSensor(hass, controller, DEFAULT_NAME, SENSOR_WWW)
    sensor.update()

    assert sensor.state is None
