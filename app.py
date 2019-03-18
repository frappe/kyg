from flask import Flask, render_template, jsonify, send_from_directory, send_file
import os, json

template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dist'))
app = Flask(__name__,
    static_folder='./dist',
    template_folder='./dist')

@app.route('/')
def index():
    return render_template('index.html', data=get_data())

@app.route('/app.js')
def send_static_from_home():
    return send_file('dist/app.js')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('dist/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('dist/css', path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('dist/assets', path)

@app.route('/get-data')
def send_get_data():
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