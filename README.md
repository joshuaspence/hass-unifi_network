# UniFi Network for Home Assistant

Connects to a UniFu Network controller to monitor high level health information.

## Configuration

### Example

```yaml
sensor:
  - platform: 'unifi_network'
    host: 'unifi'
    username: 'username'
    password: 'password'
    monitored_conditions:
      - 'alerts'
      - 'firmware'
      - 'wlan'
      - 'www'
```

### Configuration Variables

**username**

  (string)(Required) A user on the controller.

**password**

(string)(Required) The password for the account.

**host**

  (string)(Optional) The hostname or IP address of your controller.
  Default value: `localhost`

**port**

  (integer)(Optional) The port of your controller's web interface - this differs deopending on version - use `443` for `UDMP-unifiOS`.
  Default value: `8443`

**version**

  (string)(Optional) Can also be set to `v4` or `UDMP-unifiOS`.
  Default value: `v5`

**site_id**

  (string)(Optional) For multisite installations, you can specify `site_id` to specify which is used.
  Default value: `default`

**verify_ssl**

  (boolean or filename)(Optional) Whether to do strict validation on SSL certificates of the Unifi controller. This can be `true`/`false` or the path to a locally trusted certificate to use for verification.
  Default value: `false`

**monitored_conditions**

  (list)(Optional) A list of the sensors to monitor.
  Default value: If not defined all sensors are setup.

### Monitored Conditions

The following sensors can be monitored.

  - `alerts`
  - `firmware`
  - `lan`
  - `vpn`
  - `wan`
  - `wlan`
  - `www`
