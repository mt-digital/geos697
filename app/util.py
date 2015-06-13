from scipy import signal

import numpy as np
#: the water flow always stays above this height (not baseflow b/c of its spec meaning
BASE_HEIGHT = 100
START_HEIGHT = 20
#: total lenght of the "window", a term from signal processing
WINDOW = 80

def create_fake_hydrograph(peak_inflow_mo=5, peak_inflow_day=1,
                           percent_snow_change=0.8, ag_to_muni_ratio=0.7):
    """
    Create some fake hydrographs that change based on the form inputs
    """
    hgraph_peak_loc = peak_inflow_mo*31 + peak_inflow_day + 5

    hgraph_height = BASE_HEIGHT + \
                    800.0 * percent_snow_change * (1.0 - ag_to_muni_ratio)

    hgraph_stddev = 15.0*percent_snow_change

    len_pre_window = hgraph_peak_loc - WINDOW/2.0

    pre_steps = np.linspace(START_HEIGHT, BASE_HEIGHT, len_pre_window)

    len_post_window = 365 - (hgraph_peak_loc + WINDOW/2.0)

    post_steps = np.linspace(BASE_HEIGHT, START_HEIGHT, len_post_window)

    window = (BASE_HEIGHT +
              hgraph_height * signal.gaussian(WINDOW, hgraph_stddev))

    hgraph = np.hstack((pre_steps, window, post_steps))

    return hgraph
