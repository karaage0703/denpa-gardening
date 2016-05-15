#!/bin/bash

# setting
OUTFILE=`date "+../output_%Y%m%d.mp4"`
FPS=10
VIDEO_SIZE='1980x1080'
ASPECT=16:9
PRINT_DATE=0    # 0:date printed 1:date not printed

cd `dirname $0`

# copy photo files to work space
echo copy photo files to work space...
cp ./photo_data/*.jpg ./work

cd work

# printing date
if [ $PRINT_DATE -eq 0 ] ; then
	echo printing date
	for f in *.jpg
	do
		python ../photo-exif-date-print.py $f
	done
else
	echo date is not printed
fi

# encoding video
avconv -y -f image2 -r $FPS -i %6d.jpg -aspect $ASPECT -s $VIDEO_SIZE $OUTFILE

# clean up work space
rm *.jpg
