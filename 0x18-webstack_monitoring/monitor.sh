#!/bin/bash
# Replace the API and APP keys below
# with the ones for your account

api_key=api_key
app_key=app_key

curl -X POST -H "Content-type: application/json" \
     -d '{
      "type": "metric alert",
      "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
      "name": "Bytes received on host0",
      "message": "We may need to add web hosts if this is consistently high.",
      "tags": ["app:webserver", "frontend"],
      "options": {
      "notify_no_data": true,
      "no_data_timeframe": 20
      }
}' \
     "https://api.datadoghq.com/api/v1/monitor?api_key=${api_key}&application_key=${app_key}"
