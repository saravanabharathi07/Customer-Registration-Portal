import pandas as pd
#USING DATAFRAME
'''data={
    'cars':["BMW","Benz","Audi"],
    'passings':[3,7,5]
}
var=pandas.DataFrame(data)
print(var)'''
#TO SEE A PANDAS VERSION
'''print(pandas.__version__)'''

#RENAMING A INDEX VALUES
'''a=[1,2,3,4]
myvar=pd.Series(a,index=['x','y','z','a'])
print(myvar)'''

#USING DICTIONARY KEY AND VALUES
'''calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)'''

#PRINT AN EXACT ROW and naming the LABEL
'''data={
    'calories':[420,300,680],
    'duration':[10,20,30]
}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df.loc["day1"])'''