#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    from math import fabs
    n = int(0.1 * len(ages))     # points to pare
    top_n_outliers = [(0.0, 0)]     # (error, data_index)

    # Perform sequential insertion of records with top 10% residual errors
    for i in range(len(predictions)):
        p = predictions[i]
        e = fabs(p - net_worths[i])

        for j in range(n):
            if e > top_n_outliers[j][0]:
                top_n_outliers.insert(j, (e, i))
                break
    
    indices_to_clean = []
    for i in range(n):
        indices_to_clean.append(top_n_outliers[i][1])

    for i in range(len(ages)):
        if i not in indices_to_clean:
            cleaned_data.append((ages[i], net_worths[i], (predictions[i] - net_worths[i])))
    
    return cleaned_data

