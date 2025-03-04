#!/bin/bash

END_DATE="${BLOCK_INSTANCE}"

URGENT_VALUE=86400

if [[ "${END_DATE}" = "" ]]; then
  END_DATE=$(date --date "next Friday" "+%m/%d/%Y %H:%M:%S")
fi

END_DATE=$(date --date="${END_DATE}" '+%s')
CUR_DATE=$(date "+%s")
DIFF_DATE=$((END_DATE - CUR_DATE))
DIFF=""

if [[ "${DIFF_DATE}" -le 0 ]]; then
  echo "${END_DATE}"
  echo "${END_DATE}"
  echo ""
  exit 33
fi

if [[ "${DIFF_DATE}" -ge 86400 ]]; then
  DIFF="[$((DIFF_DATE / 86400))] "
  #DIFF_DATE=$((DIFF_DATE % 86400))
fi

DIFF+=$(date -u -d "@${DIFF_DATE}" +"%H:%M:%S")

echo "${DIFF}"
echo "${DIFF}"

if [[ "${DIFF_DATE}" -le "${URGENT_VALUE}" ]]; then
  exit 33
fi
