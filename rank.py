content = f.read()
k = [ i.split(',') for i in content.split(';\n')]

import csv

filename = "F:\\Skydrive\\Python\\playerData.csv"

def writeToCsv(fileName, listOfBowlers):
    with open(fileName,'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in listOfBowlers: writer.writerow(i)       


import scipy.stats as ss

#[float(i[2]) for i in l[1:]]

#Rank
    newlist = list()
    if order==0 : 
            if float(i[index])==0: newlist.append(10000)
            else: newlist.append(float(i[index]))
    rank = ss.rankdata(newlist,method='min')
    j=0
        i.append(rank[j])
        j=j+1


