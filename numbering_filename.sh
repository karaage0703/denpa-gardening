#!/bin/bash
i=1
for f in *.jpg

do g=00000$i.jpg
	mv $f ${g:(-10)}
	i=$((i+1))
done
