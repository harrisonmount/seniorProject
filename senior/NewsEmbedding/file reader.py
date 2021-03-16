import csv
import pandas as pd
import json
import os
import re
import numpy as np

def readDB(database):

    origpath = "/Users/harrisonmount/Desktop/School/Senior Project/Repo/SeniorPrj/pheme-rumour-scheme-dataset/threads/en/"
    path = "{opath}{db}".format(opath=origpath, db=database)
    newpath = os.path.join(path, "user_matrix.csv")
    dict = {} #dictionary of users : [list of who they follow]

    #MAKE A NON REPEATING LIST OF ALL USERS

    for subdir, dirs, files in os.walk(path):
        for filename in files:#loop down each tweet directory
            if filename.endswith("who-follows-whom.txt"):
                fpath = os.path.join(subdir, "who-follows-whom.dat")
                npath = os.path.join(subdir, "who-follows-whom.txt")
                #os.rename(fpath, npath) #USE IF who-follows-whom are still .dat files, change above to endswith("who-follows-whom.dat")
                f = open(npath, "r")
                for line in f:
                    x = line.split()#separate the line into two integers
                    if x[0] in dict:#if key already exists, add user theyre following to [], if not make new key with that value
                        dict[x[0]].append(x[1])
                    else:
                        dict[x[0]] = [x[1]]

                f.close()

    individualusers = dict.keys()
    print("individual user list created...\nmaking csv file with size diffusers/diffusers")
    df = pd.DataFrame(columns=individualusers)
    df.insert(0,0,individualusers)
    print('adding values to matrix')
    for itemno in individualusers:
        list = dict[itemno]
        for following in list:
            df.at[itemno, following] = 1
            print("adding 1 to: [" + itemno + ", "+ following +"]")
    print("done")
    #print(df)
    return 0


if __name__ == "__main__":
    readDB("charliehebdo")
