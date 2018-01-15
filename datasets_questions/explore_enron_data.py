#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# 146

# Total POI
t = sum(enron_data[k]["poi"] == 1 for k in enron_data.keys())       # 18
print("Total POI: %d" % t)

# Load total POI names
poi = np.loadtxt("../final_project/poi_names.txt", str, skiprows=2)     # 35

# James Prentice's stock value
search_lambda = lambda prop, search_str: \
    [enron_data[k][prop] for k in enron_data.iterkeys() if re.match(search_str, k) != None]

jpstock = search_lambda("total_stock_value", "^PRENTICE")
print("James Prentice's stock value: %d" % jpstock[0])

# mails from Wesley Colwell to POI  
wc_to_poi = search_lambda('from_this_person_to_poi', "COLWELL WESLEY")
print("mails from Wesley Colwell to POI: %d" % wc_to_poi[0])

# Jeffrey K Skilling 'exercised_stock_options' value
jks_stock = search_lambda('exercised_stock_options', "^SKILLING")
print("Jeffrey K Skilling 'exercised_stock_options' value: %d" % jks_stock[0])

# Records with quantified salary
qs = len([x for x in enron_data.itervalues() if x['salary'] != 'NaN'])    # 95
print("Records with quantified salary: %d" % qs)

# Records with known email address
ea = len([x for x in enron_data.itervalues() if x['email_address'] != 'NaN'])    # 111
print("Records with email addresses: %d" % ea)

# Who took home most money
mm = ''
max_money = 0
total_payments_nan = 0

for kv in enron_data.items():
    current_max = kv[1]['total_payments']

    if current_max == 'NaN':
        total_payments_nan += 1
    elif current_max > max_money and kv[0] != 'TOTAL':
        max_money = current_max
        mm = kv[0]
print("%s took the most money = %d" % (mm, max_money))
# LAY KENNETH L took the most money = 103559793

print("People with NaN for their total payments: %d" % total_payments_nan)
print("Percent people with NaN for their total payments: %f" % (float(total_payments_nan)/len(enron_data)))
#People with NaN for their total payments: 21
#Percent people with NaN for their total payments: 0.143836


total_payments_poi_nan = 0
for p in [("%s %s" % (p[1].strip(','), p[2])).upper() for p in poi]:    # if p[0] == '(y)'
    for k in enron_data.keys():
        if (re.match("^%s" % p, k) != None and enron_data[k]['total_payments'] == 'NaN'):
            total_payments_poi_nan += 1

print("POIs in the E+F dataset have NaN for their total payments: %d" % total_payments_poi_nan)
print("Percentage of total POIs of the above: %f" % (float(total_payments_poi_nan)/len(poi)))
