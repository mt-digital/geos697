#! venv/bin/python
import time

from numpy import arange
from pymongo import MongoClient, ASCENDING
from subprocess import Popen

from app import create_app
from app.util import create_fake_hydrograph

app = create_app('default')

# connect to treasure_valley database and the model_results
mc = MongoClient()
db = mc.treasure_valley
model_results = db.model_results

if model_results.count() == 0:

    # create an index for improved
    model_results.create_index([('month', ASCENDING), ('day', ASCENDING),
        ('percent_mountain_snow', ASCENDING), ('ag_to_muni_ratio', ASCENDING)])

    # insert synthetic data to collection
    model_results.insert_many([
        {'month': mo, 'day': day,
         'percent_mountain_snow': "%.1f" % pcs,
         'ag_to_muni_ratio': "%.2f" % atm,
         'hydrograph': list(create_fake_hydrograph(mo, day, pcs, atm))}
             for mo in range(1, 7)
             for day in range(1, 32)
             for pcs in arange(0.1, 2.1, 0.1)
             for atm in arange(0.1, 1.05, 0.05)])

print "\n*** starting web app server at http://localhost:4000 ***\n"
md_p = Popen("python manage.py runserver --port=4000", shell=True)

while True:
    time.sleep(1)
