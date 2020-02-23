import datetime
import json

import requests
from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    # response = None
    url = "http://{0}:{1}/estimate".format(app.config['WS_HOST'], app.config['WS_PORT'])
    if request.method == 'POST':
        result = dict()
        param = request.form.to_dict()
        if not param['uids'].isdigit():
            result['uids'] = param['uids']
            result['date'] = param['date']
            result['error'] = "Error: Id must be a number"
            return render_template('index.html', result=result)
        elif not is_valid(param['date']):
            result['uids'] = param['uids']
            result['date'] = param['date']
            result['error'] = "Error: Invalid date format. Also, make sure it's >={0} and <={1}".format(
                app.config['START_DATE'], app.config['DUMP_DATE'])
            return render_template('index.html', result=result)
        else:
            json_input = json.dumps({"user_id": param['uids'], "date": param['date']})
            response = requests.post(url, data=json_input,
                                     headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                result[param['uids']] = json.loads(response.text)
                return render_template('results.html', result=result)

                # json_response = """ { "1315221": {
                #                                     "estimated": 35,
                #                                     "name": "bateman",
                #                                     "registered": 38
                #                                   }
                #                      } """
            else:
                return render_template('index.html', result="Error: {0}".format(response.status_code))


def is_valid(date_text):
    valid = True
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        valid = False
    return valid


if __name__ == '__main__':
    app.run(host="0.0.0.0")
