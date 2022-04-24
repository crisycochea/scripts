#!/usr/bin/bash

FILE_TO_CONVERT=$1
IFS=. read file_name file_extension <<< $FILE_TO_CONVERT

if [[ $file_extension != "webm" ]]; then
  echo "Error: Input file(First Argument) must be a webm"
  exit 1
fi

OUTPUT_NAME=$2 || "$file_name.gif"
echo $FILE_TO_CONVERT
echo $OUTPUT_NAME
ffmpeg -i "$FILE_TO_CONVERT" -pix_fmt rgb24 "$OUTPUT_NAME"
