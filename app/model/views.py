"""

"""
from flask import render_template, request
from numpy import array
from numpy.random import randn
from pymongo import MongoClient

from . import model

mc = MongoClient()
MODEL_RESULTS = mc.treasure_valley.model_results

# XXX change this to a date when you get a chance-just like this for first go
DEFAULT_SNOWPACK_PERCENT_CHANGE = "0.8"
DEFAULT_AG_TO_MUNI_RATIO = "0.30"


@model.route('/', methods=['GET', 'POST'])
def index():
    "main modeling page with sliders"

    if request.method == 'POST':

        peak_inflow_month, peak_inflow_day = \
            (request.form['peak-inflow-rate-mo'],
             request.form['peak-inflow-rate-day'])

        percent_mountain_snow = request.form['snowpack-percent-change']
        ag_to_muni_ratio = request.form['ag-to-muni-ratio']
        # web form will send back '1'
        if float(percent_mountain_snow) == 1.0:
            percent_mountain_snow = '1.0'

        # web form leaves off trailing zero for fractional
        if len(ag_to_muni_ratio.split('.')[-1]) == 1:
            ag_to_muni_ratio = ag_to_muni_ratio + '0'

        downstream_discharge = \
            get_discharge(peak_inflow_month, peak_inflow_day,
                          percent_mountain_snow, ag_to_muni_ratio)
    else:

        peak_inflow_month = "6"
        peak_inflow_day = "1"
        percent_mountain_snow = DEFAULT_SNOWPACK_PERCENT_CHANGE
        ag_to_muni_ratio = DEFAULT_AG_TO_MUNI_RATIO

        downstream_discharge = \
            get_discharge(peak_inflow_month, peak_inflow_day,
                          percent_mountain_snow, ag_to_muni_ratio)

    return render_template("model/index.html",
                           peak_inflow_date=(peak_inflow_month, peak_inflow_day),
                           percent_mountain_snow=percent_mountain_snow,
                           ag_to_muni_ratio=ag_to_muni_ratio,
                           downstream_discharge=downstream_discharge)


def get_discharge(peak_inflow_month, peak_inflow_day, percent_mountain_snow,
                  ag_to_muni_ratio):

    peak_inflow_month = int(peak_inflow_month)
    peak_inflow_day = int(peak_inflow_day)

    hg_list = MODEL_RESULTS.find_one({'month': peak_inflow_month,
                                      'day': peak_inflow_day,
                                      'percent_mountain_snow': percent_mountain_snow,
                                      'ag_to_muni_ratio': ag_to_muni_ratio},
                                     projection={'hydrograph': True}
                                            )['hydrograph']

    ret = array(hg_list) + (30*randn(len(hg_list)))

    return ret
