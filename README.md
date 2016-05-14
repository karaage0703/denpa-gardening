# denpa-gardening


# Setup

## Hardware
### Parts list

- Raspberry Pi 3 (maybe RPi 2 is Ok but I don't check it)
- BME280 Sensor module (AE-BME280 Akizuki denshi is recommended)
- RPi Camera Module

### Hardware Setup
t.b.d.

### Hardware Check
t.b.d.


## Software
### Preparation
#### Install OS
- Install Raspbian Jessie (Release date:2016-03-18)
- Enable Camera and I2C by using Raspi-config setup tool of Raspbian

#### Install I2C tools and I2C python library
```sh
$ sudo apt-get update
$ sudo apt-get install i2c-tools
$ sudo apt-get install python-smbus 
```

#### Install gnuplot
```sh
$ sudo apt-get update
$ sudo apt-get install gnuplot
```


### Usage

#### Clone software

```sh
$ cd
$ git clone https://github.com/karaage0703/denpa-gardening.git
```

#### Taking photo test
Execute following command:
```sh
$ python ~/denpa-gardening/shutter.py
```

add photo file to `photo_data` directory.


#### Getting sensor data test
Execute following command:
```sh
$ python ~/denpa-gardening/temp_pres_humid_sensor.py
```

display sensor data. Data format is below

`data`, `temperature`, `humidity`, `pressure`


If you want to export sensor data to csv file, execute following command:
```sh
$ python ~/denpa-gardening/temp_pres_humid_sensor.py >> ~/denpa-gardening/sensor_data/sensor_data.csv
```

If you want to create graph of sensor data, execute following command:
```sh
$ ~/denpa-gardening/make_graph.sh ~/denpa-gardening/sensor_data/sensor_data.csv
```

#### Adding timestamp to photo
For example, execute following command:
```sh
$ python ~/denpa-gardening/photo-exif-date-print.py 000001.jpg
```

Timestamp is added to `000001.jpg` by using exif data of photo.

#### Setup auto logging
```sh
$ cd
$ git clone https://github.com/karaage0703/denpa-gardening
$ crontab ~/denpa-gardening/cron.txt
```


# Special Thanks



# License
This software is released under the MIT License, see LICENSE.
