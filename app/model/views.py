"""

"""
import os
import json

from flask import render_template, request
from numpy import arange
from numpy.random import randn

from . import model

MODEL_RUNS = json.loads(open(os.path.dirname(__file__)
                            + '/../static/model_data.json').read())

# XXX change this to a date when you get a chance-just like this for first go
DEFAULT_SNOWPACK_PERCENT_CHANGE = "0.8"
DEFAULT_AG_TO_MUNI_RATIO = "0.30"
# todo: use data, eg, D_O = MODEL_RUNS[15].downstream_discharge
DEFAULT_DOWNSTREAM_DISCHARGE = 4.5 + abs(randn(10))*arange(10)


@model.route('/', methods=['GET', 'POST'])
def index():
    "main modeling page with sliders"

    if request.method == 'POST':

        peak_inflow_date = (request.form['peak-inflow-rate-mo'],
                            request.form['peak-inflow-rate-day'])

        snowpack_percent_change = request.form['snowpack-percent-change']
        ag_to_muni_ratio = request.form['ag-to-muni-ratio']

        if len(ag_to_muni_ratio.split('.')[-1]) == 1:
            ag_to_muni_ratio = ag_to_muni_ratio + '0'

        downstream_discharge = \
            MODEL_RUNS[','.join([
                peak_inflow_date[0], peak_inflow_date[1],
                snowpack_percent_change, ag_to_muni_ratio])]

    else:

        month = "6"
        day = "1"
        peak_inflow_date = (month, day)
        snowpack_percent_change = DEFAULT_SNOWPACK_PERCENT_CHANGE
        ag_to_muni_ratio = DEFAULT_AG_TO_MUNI_RATIO
        downstream_discharge = \
            MODEL_RUNS[','.join([month, day,
                                snowpack_percent_change,
                                ag_to_muni_ratio])]

    return render_template("model/index.html",
                           peak_inflow_date=peak_inflow_date,
                           snowpack_percent_change=snowpack_percent_change,
                           ag_to_muni_ratio=ag_to_muni_ratio,
                           downstream_discharge=downstream_discharge)
