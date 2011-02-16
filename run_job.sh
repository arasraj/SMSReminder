#!/bin/bash

curl http://127.0.0.1:8888/send
echo "Sent out SMS...hopefully: $(date)" >> /home/kip/sms_reminder/sms.log

#*/15 * * * * /home/xxx/sms_reminder/run_job.sh
