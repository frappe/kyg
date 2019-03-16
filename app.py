from flask import Flask, render_template, jsonify
import os, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=get_data())

@app.route('/get-data')
def get_data_json():
    return jsonify(get_data())

def get_data():
    data = []
    for name in os.listdir('data'):
        config = os.path.join('data', name, 'config.json')
        if os.path.exists(config):
            with open(config, 'r') as f:
                gov = json.loads(f.read())
                gov["year"] = gov["from"].split()[1]
                data.append(gov)

    return sorted(data, key=lambda d: d['year'])

if __name__ == '__main__':
    app.run()