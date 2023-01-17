#!/bin/bash
#This script downloads covid date and displays it


DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITALIZEDCURRENTLY=$(echo $DATA | jq '.[0].hospitalized')
INICUCURRENTLY=$(echo $DATA | jq '.[0].inIcuCurrently')
ONVENTILATORCURRENTLY=$(echo $DATA | jq '.[0].onVentilatorCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, with $HOSPITALIZEDCURRENTLY people currently in the hospital, $INICUCURRENTLY people currently in ICU, and $ONVENTILATORCURRENTLY people currently on a ventilator."

