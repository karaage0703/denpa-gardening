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

#### Install tweet library
```sh
$ sudo pip install twython
```

#### Install video encoder
```sh
$ sudo apt-get install libav-tool
```

### Usage

#### Clone software

```sh
$ cd
$ git clone https://github.com/karaage0703/denpa-gardening.git
```

#### Taking photo
Execute following command:
```sh
$ python ~/denpa-gardening/shutter.py
```

add photo file to `photo_data` directory.


#### Getting sensor data
Execute following command:
```sh
$ python ~/denpa-gardening/get_sensor_data.py
```

display sensor data. Data format is below

`data`, `temperature`, `humidity`, `pressure`


If you want to export sensor data to csv file, execute following command:
```sh
$ python ~/denpa-gardening/get_sensor_data.py >> ~/denpa-gardening/sensor_data/sensor_data.csv
```

If you want to create graph of sensor data, execute following command:
```sh
$ ~/denpa-gardening/make-graph.sh ~/denpa-gardening/sensor_data/sensor_data.csv
```

#### Adding timestamp to photo
For example, execute following command:
```sh
$ python ~/denpa-gardening/photo-exif-date-print.py 000001.jpg
```

Timestamp is added to `000001.jpg` by using exif data of photo.

#### Tweet sensor data
Edit `.twitter_config` according to your twitter KEY.  
Then execute following command:
```sh
$ python ~/denpa-gardening/tweet_sensor_data.py
```

#### Setup auto logging
```sh
$ crontab ~/denpa-gardening/cron.txt
```

# Special Thanks
http://iwajyuku.hatenablog.com/entry/2016/12/15/181256 (send_mail.py)

# License
This software is released under the MIT License, see LICENSE.
