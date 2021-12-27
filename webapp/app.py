from flask import Flask, render_template
from flask import request, url_for
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
import pandas as pd
import json
import argparse
import os
from wsgiref import simple_server
from src.custom_function import *
app = Flask(__name__)
dashboard.bind(app)
CORS(app)
# CORS(app)
def minmax_columns(config_path):
    config = read_params(config_path)
    data_dir = config["flask"]["data_dirr"]
    data = config["flask"]["data"]
    data_fp = os.path.join(data_dir, data)
    print(data_fp)
    output_fn = os.path.join('webapp','static', 'data', 'minmax.json')

    if not os.path.isfile(output_fn):
        print('JSON not present')
        print('Generating Min Max JSON')
        data = pd.read_csv(data_fp)
        minmaxcols = ['duration', 'amount', 'age']
        with open(output_fn, 'w') as json_file:
            data_dict = dict()
            for col in minmaxcols:
                _min = data[col].min()
                _max = data[col].max()
                data_dict[col] = { 'min': int(_min), 'max': int(_max) }
            json.dump(data_dict, json_file)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', message="Hello Flask!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    minmax_columns(config_path= parsed_args.config)


