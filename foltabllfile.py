import pandas as pd
import matplotlib.pyplot as plt

ch = input('Enter the Password')
while ch == "y" or ch == "Y":
    print("Welcome To Fifa Database")
    print('Select The numbers to continue')
    print("Press 1 for All available data  ")
    print("press 2 to show player data by age")
    print("Press 3 to add the new palyers data")
    print("Press 4 to deleat the data ")

    lect1 = int(input("Enter the numer here"))
    if lect1 == 1:
        df = pd.read_csv("fifadtata.csv")
        print(df)
    elif lect1==2:
        df = pd.read_csv("fifadtata.csv")
        ag=int(input("Enter Age"))
        if df[df.age==ag].empty:
            print("Record Not Found")
        else :
            print(df[df.age==ag])
    elif lect1 ==3:
        df = pd.read_csv("fifadtata.csv")
        id1=int(input("Enter the Rank of Player"))
        nam1=input("Enter the name of palyer")
        age1=int(input("Eneter the age of Player"))
        oscr2=int(input("Enter the Performance score "))
        club6=input("Entere the name of club ")
        fifs2=int(input("Eneter the Fifa Unique Id"))
        df=df.append({'id':id1 , "name" : nam1 , "age":age1 , 'oscore': oscr2 , "club": club6, "fifaid":fifs2},ignore_index=True)
        print(df)
        print("Record added")
    elif lect1==4:
        df = pd.read_csv("fifadtata.csv")
        id2=int(input("Enter the roll number"))

        if df[df.id ==id2].empty:
            print("Data not found")
        else:
            print(df[df.id ==id2])
            df=df[df['id ']!= id ]
            print("Data deleted ")











