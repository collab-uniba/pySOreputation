#!/usr/bin/env bash

# - the script is ran via anaconda python
#source /anaconda3/etc/profile.d/conda.sh
conda activate .venv37
# - stdout & stderr are redirected to a log file
uwsgi --ini app.ini >> /var/log/pyso-ws.log 2>&1
