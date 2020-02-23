import datetime
import json

from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    # response = None
    url = "{0}:{1}/estimate".format(app.config['WS_HOST'], app.config['WS_PORT'])
    if request.method == 'POST':
        param = request.form.to_dict()
        if param['uids'] is "" or param['date'] is "":
            return render_template('index.html', result="Error: All fields are mandatory")
        elif not param['uids'].isdigit():
            return render_template('index.html', result="Error: Id must be a number")
        elif not is_valid(param['date']):
            return render_template('index.html',
                                   result="Error: Invalid date format. Also, make sure it's >={0} and <={1}".format(
                                       app.config['START_DATE'], app.config['DUMP_DATE']))
        else:
            json_input = json.dumps({"user_id": param['uids'], "date": param['date']})
            # json_response = requests.post(url, data=json_input,
            #                         headers={'Content-Type': 'application/json'})
            json_response = """ { "1315221": {
                                                "estimated": 35,
                                                "name": "bateman",
                                                "registered": 38
                                              }
                                 } """
            response = dict()
            response[param['uids']] = json.loads(json_response)
            return render_template('results.html', result=response)


def is_valid(date_text):
    valid = True
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        valid = False
    return valid


if __name__ == '__main__':
    app.run(host="0.0.0.0")
