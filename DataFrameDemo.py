import pandas as pd

df1=pd.DataFrame(
    {'name':['amol','amol','vishal','rajesh','suraj','amit'],
     'maths':[67,78,56,77,89,66]
     },
    index=list('abcdef')
    )

#print(df1)

# print(df1.columns)
# use of dtypes is to get the col names with data type
#print(df1.dtypes)

#print(df1.info())

# head() -> first 5 records  & tail() - last 5 records 
# print('----head()----')
# print(df1.head(3))

# print("-----tail()---")
# print(df1.tail(2))

# to read a specific col, that is added in []
#print(df1['maths'])

# iloc  --> index based
# loc  --> lable based

# print(df1.loc['d','maths'])

# print(df1.loc['d',['name','maths']])

# print(df1.loc[['d','e'],['name','maths']])

df1['eng']=[78,56,99,64,71,79]
df1['sci']=90
#print(df1)

# print(df1.describe())

# print(df1.maths.describe())


# rename the col name
# df1.rename(columns={'name':'stud_name','maths':'new'},inplace=True)

# df1.rename(index={'a':'A'},inplace=True)
# print(df1)

# add total as a col & perform sum for each stud

#df1['total']=df1['maths']+df1['eng']+df1['sci']
df1['total']=df1.loc[:,'maths':'sci'].sum(axis=1)
# print(df1)

# display grade based on condition
df1['grade']=df1['total'].apply(lambda x:'A+' if x>235 else 'A')


#print(df1.sort_values('name',ascending=False))

print(df1.sort_values(['name','total'],ascending=[False,True]))

# group by
print(df1.groupby('grade')['grade'].count())

print(df1.groupby('grade')['maths'].min())

df1.to_excel("student.xlsx")
# df1.to_excel('student_data.xlsx')

# df1.to_csv('stud.csv')





