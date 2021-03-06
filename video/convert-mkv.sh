#!/bin/bash

# Convert mkv to mp4 format

for i in *.mkv;
  do name=`echo $i | cut -d'.' -f1`;
  echo $name;
  ffmpeg -ss 00:00:05 -i "$i" -frames:v 1 "./output/$name.png"
  ffmpeg -i "$i" "./output/$name.mp4";
done
