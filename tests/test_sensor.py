from homeassistant.core import HomeAssistant
from pyunifi.controller import Controller

from custom_components.unifi_network.sensor import (
    DEFAULT_NAME,
    SENSOR_WWW,
    SENSORS,
    UnifiNetworkSensor,
)


async def test_sensor(hass: HomeAssistant, controller: Controller) -> None:
    sensor = UnifiNetworkSensor(hass, controller, DEFAULT_NAME, SENSOR_WWW)
    sensor.update()

    assert sensor.state is None


async def test_sensor_properties(hass: HomeAssistant, controller: Controller) -> None:
    type = SENSOR_WWW
    name = "Sensor Name"

    sensor = UnifiNetworkSensor(hass, controller, name, type)

    assert sensor.name == name + " " + SENSORS[type][0]
    assert sensor.icon == SENSORS[type][2]
