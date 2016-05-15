#!/bin/bash

cd `dirname $0`
cd sensor_data
mv sensor_data.csv sensor_data_$(date +%Y%m%d).csv
mv sensor_data_humid.png sensor_data_humid_$(date +%Y%m%d).png
mv sensor_data_pressure.png sensor_data_pressure_$(date +%Y%m%d).png
mv sensor_data_temp.png sensor_data_temp_$(date +%Y%m%d).png
mv sensor_data_temp_humid.png sensor_data_temp_humid_$(date +%Y%m%d).png
