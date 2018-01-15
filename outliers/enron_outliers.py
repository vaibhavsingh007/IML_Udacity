#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL")

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for k in data_dict.keys():
    sal = data_dict[k]['salary']
    bon = data_dict[k]['bonus']
    if sal != 'NaN' and bon != 'NaN' and sal > 10**5 and bon > 5*10**6:
        print("%s: " % k, sal, bon)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
