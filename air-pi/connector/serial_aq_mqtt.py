#!/usr/bin/env python3

import logging
from lib.input.serial import SerialWrap
from lib.parse.air import AirParse
from lib.output.mqtt import MqttBroker

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-10s) %(levelname)s %(message)s")

serial = SerialWrap("/dev/serial0", 9600, timeout=0.2)
aq = AirParse()
mqtt = MqttBroker()
domain = "home"


def main():
    logging.info("ser2mqtt starting")

    while True:
        line = serial.try_readline_decode()
        if not line:
            continue
        logging.debug("RECV: " + line)

        for (key, value) in aq.parse_packet(line):
                logging.info("Pub %s/%s: %s" % (domain, key, value))
                mqtt.publish("%s/%s" % (domain, key), value)


if __name__ == '__main__':
    main()
