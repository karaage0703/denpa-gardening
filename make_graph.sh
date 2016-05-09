#!/bin/sh

set -eu

INFILE=$1
OUT_TEMP_HUMID="${INFILE%.*}_temp_humid.png"
OUT_TEMP="${INFILE%.*}_temp.png"
OUT_HUMID="${INFILE%.*}_humid.png"
OUT_PRESSURE="${INFILE%.*}_pressure.png"
TITLE="sensor data"
TIME_LABEL="time"
TEMP_LABEL="temperature[C]"
HUMID_LABEL="humidity[%]"
PRESSURE_LABEL="pressure[hPa]"

gnuplot <<EOF
set datafile separator ','
set xdata time
set timefmt '%Y/%m/%d %H:%M:%S'
set format x '%H:%M'
#set format x '%M:%S'
set mxtics 2
set mytics 2
set grid xtics ytics mxtics mytics
set key outside
# second ax
set y2tics
set title '$TITLE'
set term png size 800,480
#set xrange ['2016/01/01 10:00:00':'2016/12/31 12:00:00']
set yrange [-10:40]
set y2range [0:100]
set xlabel '$TIME_LABEL'
set ylabel '$TEMP_LABEL'
set y2label '$HUMID_LABEL'
set output '$OUT_TEMP_HUMID'
p '$INFILE' u 1:2 w l ti 'temperature','$INFILE' u 1:3 w l axes x1y2 ti 'humidity'
set output

unset y2tics
unset y2label

set yrange [-10:40]
set xlabel '$TIME_LABEL'
set ylabel '$TEMP_LABEL'
set output '$OUT_TEMP'
p '$INFILE' u 1:2 w l ti 'temperature'
set output

set yrange [0:100]
set xlabel '$TIME_LABEL'
set ylabel '$HUMID_LABEL'
set output '$OUT_HUMID'
p '$INFILE' u 1:3 w l ti 'humidity'
set output

set yrange [940:1040]
set xlabel '$TIME_LABEL'
set ylabel '$PRESSURE_LABEL'
set output '$OUT_PRESSURE'
p '$INFILE' u 1:4 w l ti 'pressure'
set output

EOF
