#!/bin/bash
cd `dirname $0`
cd work
for f in *.jpg
do
	python ../photo-exif-date-print.py $f
done
