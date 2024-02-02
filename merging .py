import pandas as pd
df1=pd.DataFrame({'key':['A','B','C'], 'value':[1,2,3]})
df2=pd.DataFrame({'key':['A','B','D'],'value':[4,5,6]})
print(df1)
print(df2)
res_inner=pd.merge(df1,df2,on='key',how='inner')
print(" Reslut of inner join\n",res_inner)
res_outer=pd.merge(df1,df2,on="key",how='outer')
print("result of outer join\n",res_outer)
res_left=pd.merge(df1,df2,on="key",how="left")
print("result of left join\n",res_left)
res_right=pd.merge(df1,df2,on="key",how="right")
print("result of right join\n",res_right)


df3=pd.DataFrame({"ID": [2,3,4],"Name":["ALice","Joe","Mary"]})
df4=pd.DataFrame({"ID":[3,4,5],"Age":[25,30,26]})
merge_1=pd.merge(df3,df4,on="ID")
print(merge_1)