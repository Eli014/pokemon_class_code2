'''
class Pokemon(object):
    def __init__(self,index,Name,Type_1,Total,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed,Generation):

        self.index= index
        self.Name= Name
        self.Type_1= Type_1
        self.Total =Total
        self.HP= HP
        self.Attack= Attack
        self.Defense= Defense
        self.Sp_Atk=Sp_Atk
        self.Sp_Def=Sp_Def
        self.Speed=Speed
        self.Generation=Generation
'''

'''
np.random.seed()

Type_1 = np.random.normal(100, 10, 200)
Speed = np.random.normal(90, 20, 200)
Attack = np.random.normal(80, 30, 200)
Generation = np.random.normal(70, 40, 200)
data = [Type_1, Speed, Attack, Generation]

fig = plt.figure(figsize =(10, 10))

ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(data)
plt.show()
'''
'''
x = ['Name']
y = ['Total']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()
'''
# A pokemon's total accounts for: HP, Attack, Defense,Sp. Atk, and Sp. Def and Speed
#groupby_sum1 = df.groupby(['Total' and 'Name']).sum()
#groupby_count1 = df.groupby(['Total' and 'Name']).count()
#print ('Sum of values, grouped by the Total and Name: ' + str(groupby_sum1))
#print ('Count of values, grouped by the Total and Name: ' + str(groupby_count1))
#I've taken my favorite two pokemon from each generation
# def select_columns(df):
#     new_frame = df.loc[df.Name=='Bulbasaur', :]
#     return new_frame
# print(select_columns)
#df=df.loc[df.Name =='Bulbasaur', :]
#df=df.loc[df['Name'] =='Wartortle', :]

# df=df.loc[df.Name =='Igglybuff', :]
# df=df.loc[df.Name =='Ho-oh', :]
# df=df.loc[df.Name =='Zigzagoon', :]

# #Total vs Generation:
# sample_data= df
# Total=sample_data['Total']
# sample_data_2=df
# Generation= sample_data_2['HP']
# x =Generation
# y =Total
#
# plt.subplot(1, 1, 1)
# plt.plot(x,y)
# plt.show()
