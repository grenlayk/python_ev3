#!/usr/bin/env pybricks-micropython

from pybricks.ev3devio import Ev3devSensor

class HTColorSensor(Ev3devSensor):
    _ev3dev_driver_name = 'ht-nxt-color-v2'
    _number_of_values = 4
    def rgb(self):
        self._mode('RGB')
        errors = 0
        while True:
            try:
                return self._value(0), self._value(1), self._value(2)
            except:
                errors += 1 # may give ENODEV error
                if errors > 1:
                    return 0, 0, 0
    def color(self):
        self._mode('COLOR')
        errors = 0
        while True:
            try:
                return self._value(0)
            except:
                errors += 1 # may give ENODEV error
                if errors > 1:
                    return 0

