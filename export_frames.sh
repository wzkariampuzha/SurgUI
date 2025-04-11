#!/bin/bash

mkdir -p extracted_frames

for video in *.mp4; do
  base=$(basename "$video" .mp4)
  mkdir -p "extracted_frames/${base}.mp4"

  # Extract every 14th frame
  ffmpeg -loglevel error -i "$video" \
    -vf "select='not(mod(n\,14))'" -vsync vfr \
    "extracted_frames/${base}.mp4/tmp_frame_%04d.png"

  # Rename frames based on real frame numbers: 0, 14, 28, ...
  i=0
  for file in extracted_frames/${base}.mp4/tmp_frame_*.png; do
    newname=$(printf "extracted_frames/${base}.mp4/frame_%d.png" "$i")
    mv "$file" "$newname"
    ((i+=14))
  done
done
