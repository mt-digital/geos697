"""

"""
import os

from flask import render_template, request
from pandas import read_csv
from numpy import arange
from numpy.random import randn

from . import model

MODEL_RUNS = read_csv(os.path.dirname(__file__) + '/../static/model_data.csv')
# XXX change this to a date when you get a chance-just like this for first go
DEFAULT_PEAK_INFLOW_DATE = 0.1
DEFAULT_SNOWPACK_PERCENT_CHANGE = 0.8
DEFAULT_AG_TO_MUNI_RATIO = 0.3
# todo: use data, eg, D_O = MODEL_RUNS[15].downstream_discharge
DEFAULT_DOWNSTREAM_DISCHARGE = 4.5 + abs(randn(10))*arange(10)


@model.route('/', methods=['GET', 'POST'])
def index():
    "main modeling page with sliders"

    if request.method == 'POST':

        peak_inflow_date = (request.form['peak-inflow-mo'],
                            request.form['peak-inflow-day'])

        snowpack_percent_change = request.form['snowpack-percent-change']
        ag_to_muni_ratio = request.form['ag-to-muni-ratio']

        downstream_discharge = \
            MODEL_RUNS[
                MODEL_RUNS.peak_inflow_date == peak_inflow_date,
                MODEL_RUNS.snowpack_percent_change == snowpack_percent_change,
                MODEL_RUNS.ag_to_muni_ratio == ag_to_muni_ratio
                ].downstream_discharge

    else:

        peak_inflow_date = DEFAULT_PEAK_INFLOW_DATE
        snowpack_percent_change = DEFAULT_SNOWPACK_PERCENT_CHANGE
        ag_to_muni_ratio = DEFAULT_AG_TO_MUNI_RATIO
        downstream_discharge = DEFAULT_DOWNSTREAM_DISCHARGE

    return render_template("model/index.html", peak_inflow_date=peak_inflow_date,
                           snowpack_percent_change=snowpack_percent_change,
                           ag_to_muni_ratio=ag_to_muni_ratio,
                           downstream_discharge=downstream_discharge)
