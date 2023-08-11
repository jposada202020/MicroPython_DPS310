# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_dps310 import dps310

i2c = I2C(sda=Pin(8), scl=Pin(9))  # Correct I2C pins for UM FeatherS2
dps = dps310.DPS310(i2c)

while True:
    print(f"Pressure: {dps.pressure}HPa")
    print()
    time.sleep(1)
