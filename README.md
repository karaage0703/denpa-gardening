# denpa-gardening


# Setup

## Hardware
### Parts list

- Raspberry Pi 3 (maybe RPi 2 is Ok but I don't check it)
- BME280 Sensor module (AE-BME280 Akizuki denshi is recommended)
- RPi Camera Module



## Software

### Install OS
- Install Raspbian Jessie (Release date:2016-03-18)
- Enable Camera and I2C by using Raspi-config setup tool of Raspbian

### Install I2C tools and I2C python library
```sh
$ sudo apt-get update
$ sudo apt-get install i2c-tools
$ sudo apt-get install python-smbus 
```

### Install gnuplot
```sh
$ sudo apt-get update
$ sudo apt-get install gnuplot
```

### Setup denpa-gardening software
```sh
$ cd
$ git clone https://github.com/karaage0703/denpa-gardening
$ crontab ~/denpa-gardening/cron.txt
```


# Special Thanks



# License
This software is released under the MIT License, see LICENSE.
