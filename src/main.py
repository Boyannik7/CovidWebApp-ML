import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def calculateAfter(days = 500, file = 'data/full_grouped.csv'):

    df=pd.read_csv('data/full_grouped.csv', sep=',',names=['Date','Country/Region','Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered','WHO Region'])
    #bulgaria_records = pd.array()
    data = df.to_numpy()
    bulgaria_data = []
    for row in data:
        if row[1] == 'Bulgaria':
            bulgaria_data.append(row)

    np_bulgaria = np.array(bulgaria_data)
    firstdate = np_bulgaria[:,0][0]
    np_bulgaria[:,0] = np.array(range(0,len(np_bulgaria[:,0])))
    np_bulgaria = np.delete(np_bulgaria, 1,1)

    last_day = len(np_bulgaria) - 1
    new_cases = 0
    new_deaths = 0
    new_recovered = 0

    X = np_bulgaria[:, 0:4]
    y = np_bulgaria[:, 5].transpose()

    predict_arr = [last_day + 1, X[last_day, 1], X[last_day, 2], X[last_day, 3]]

    f = open("result.csv", "w")

    f.write("Date,Country/Region, Confirmed, Deaths, Recovered, Active, New cases, New deaths, New recovered, WHO Region \n")

    for i in range(0, days):

        reg = LinearRegression().fit(X, y)
        reg.score(X, y)


        new_cases = round(reg.predict(np.array([predict_arr]))[0])

        y = np_bulgaria[:, 6].transpose()
        reg = LinearRegression().fit(X, y)
        reg.score(X, y)
        new_deaths = round(reg.predict(np.array([predict_arr]))[0])

        y = np_bulgaria[:, 7].transpose()
        reg = LinearRegression().fit(X, y)
        reg.score(X, y)

        new_recovered = round(reg.predict(np.array([predict_arr]))[0])


        print("--------------------------")
        print("New cases:" + str(new_cases))
        print("New deaths:" + str(new_deaths))
        print("New cases:" + str(new_recovered))
        print("--------------------------")


        last_day += 1
        predict_arr = [last_day, new_cases, new_deaths, new_deaths]

    f.write("{},{},{},{},{},{},{},{},{},{}".format(0,0, 0, 0, 0, 0,predict_arr[1],predict_arr[2], predict_arr[3], 0))
    f.close()
    return [0, 0, 0, 0, 0, 0, predict_arr[1],predict_arr[2], predict_arr[3], 0]

calculateAfter()
