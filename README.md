# Air Quality monitor
Implementation of an affordable indoor air quality monitor using various sensors connected to a microcontroller and streaming the data to a Raspberry PI for analysis using [Node-RED](http://nodered.org/).

## Sensing Unit
In the sensing unit a [Teensy](https://www.pjrc.com/teensy/) microcontroller reads the sensor data from the connected sensors and sends it over the attached Bluetooth BLE module.

### Hardware
The following sensors were used:

| Category            | Name                                                                                                  | Provides                             | Price   |
|---------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|--------:|
| Core                | [Teensy 3.2](https://www.pjrc.com/teensy/)                                                            | Processing                           | ~24€ |
| Core                | [HM-11 BLE Module](http://wiki.seeed.cc/Bluetooth_V4.0_HM_11_BLE_Module/)                             | Bluethooth                           |  ~5€ |
| Sensors             | [BME280](https://www.bosch-sensortec.com/bst/products/all_products/bme280)                            | Temperature, Pressure, Humidity      | ~14€ |
| Sensors             | [iAQ-core C](http://ams.com/eng/Products/Environmental-Sensors/Air-Quality-Sensors/iAQ-core-C)        | VOC Sensor                           | ~33€ |
| Sensors (optional)  | [MQ135](https://www.olimex.com/Products/Components/Sensors/SNS-MQ135/)                                | Gas                                  |  ~2€ |
| Sensors (optional)  | [SM-PWM-01C](http://www.amphenol-sensors.com/en/component/edocman/3-co2/4-co2-modules/194-sm-pwm-01c) | Dust Sensor                          | ~14€ |
| Sensors (NA) | [BME680](https://www.bosch-sensortec.com/bst/products/all_products/bme680)                                   | Temperature, Pressure, Humidity, VOC |        NA |

### Wiring
A Fritzing sketch showing the layout of the current hardware prototype is included in the air-monitor folder.

## Processing unit
This unit was installed and tested on a Raspberry PI 3 (model B) device, running Debian Jessie. The purpose of this unit is to process all the data received via Bluetooth from the sensing unit and compute the current air quality index, based on the latest measurements. This unit is also configured to display the current status, as well as triggering real-time notifications in case the air quality gets worse.

### Hardware
In the processing unit, a Teensy microcontroller reads the data sent from the sensing unit using an additional Bluetooth BLE module. This data is then forwarded to the Raspberry PI.

| Category | Name                                                                           | Price |
|----------|--------------------------------------------------------------------------------|------:|
| Core     | [Raspberry PI 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) | ~40€  |
| Core     | [Teensy 3.2](https://www.pjrc.com/teensy/)                                     | ~24€  |
| Core     | [HM-11 BLE Module](http://wiki.seeed.cc/Bluetooth_V4.0_HM_11_BLE_Module/)      |  ~5€  |
| LED      | [Neopixel WS2812 RGB Ring - 8](http://www.watterott.com/de/WS2812B-RGB-Ring-8) |  ~7€  |

The Neopixel LED needs to be connected to the Raspberry PI board using the following pins:
- VCC (any)
- GND (any)
- [BCM 18](https://pinout.xyz/pinout/pin12_gpio18) (pin 12) for providing input to the LED


### Installation
Raspberry PI 3 comes with a pre-installed version of Node-Red. Additionally, it is necessary to install the following modules:
- [node-red-node-sqlite](https://www.npmjs.com/package/node-red-node-sqlite)
- [node-red-contrib-telegrambot](https://github.com/windkh/node-red-contrib-telegrambot)
- [node-red-dashboard](https://github.com/node-red/node-red-dashboard)
- [node-red-node-pi-neopixel](https://www.npmjs.com/package/node-red-node-pi-neopixel)
(for controlling the neopixel LEDs, an additional library needs to be installed. This can be done by following the instructions on the npmjs or github page of this module)

All the required flows needed for running the application can be found inside the node-red folder of this project. These flows can be easily imported via the web-based GUI provided by Node-Red.
