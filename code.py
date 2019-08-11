# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print (data.head(10))
#Code starts here



# --------------
#Code starts here





data['Better_Event'] = np.where (data['Total_Summer']==data['Total_Winter'],'Both',(np.where (data['Total_Summer']>data['Total_Winter'],'Summer',(np.where (data['Total_Summer']<data['Total_Winter'],'Winter','None')))))
print (data.head(10))
better_event = data['Better_Event'].value_counts().idxmax()
print (better_event)
#abc = data[data['Better_Event']=='Winter']['Country_Name']
#print (abc)
#abc = data[data['Better_Event']=='Both']['Country_Name']
#print (abc)


# --------------
#Code starts here




top_countries = pd.DataFrame(data,columns=['Country_Name','Total_Summer','Total_Winter','Total_Medals'])
#print (top_countries.head())
top_countries.drop(top_countries.tail(1).index,inplace=True)
#print (top_countries.tail())
def top_ten(df,column):
    Top_10 = df.nlargest(10,column)
    #print (Top_10)
    country_list = list(Top_10['Country_Name'])
    return (country_list)

top_10_summer = top_ten(top_countries,'Total_Summer')
print (top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
print (top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
print (top_10)
common = list(set(top_10_summer).intersection(set(top_10_winter),set(top_10)))
print (common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#plt.figure(figsize=(20,15))
summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer', legend=False)
plt.title('Summer Olympic Analysis')
plt.xlabel('Country Name')
plt.ylabel('Total Summer Medals')
plt.show()
#plt.figure(figsize=(20,15))
winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter', legend=False)
plt.title('Winter Olympic Analysis')
plt.xlabel('Country Name')
plt.ylabel('Total Winter Medals')
plt.show()
#plt.figure(figsize=(20,15))
top_df.plot(kind='bar',x='Country_Name',y='Total_Medals', legend=False)
plt.title('Summer & Winter Olympic Analysis')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.show()


# --------------
#Code starts here
#Summer
summer_df['Golden_Ratio'] = np.where(summer_df['Gold_Summer']==0,0,summer_df['Gold_Summer']/summer_df['Total_Summer'])
summer_max_ratio = np.max(summer_df['Golden_Ratio'])
print (summer_max_ratio)
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].to_string(index=False)
print (summer_country_gold)
#Winter
winter_df['Golden_Ratio'] = np.where(winter_df['Gold_Winter']==0,0,winter_df['Gold_Winter']/winter_df['Total_Winter'])
winter_max_ratio = np.max(winter_df['Golden_Ratio'])
print (winter_max_ratio)
winter_country_gold = winter_df[(winter_df['Golden_Ratio']==winter_max_ratio)]['Country_Name'].to_string(index=False)
print (winter_country_gold)
#Overall
top_df['Golden_Ratio'] = np.where(top_df['Gold_Total']==0,0,top_df['Gold_Total']/top_df['Total_Medals'])
top_max_ratio = np.max(top_df['Golden_Ratio'])
print (top_max_ratio)
top_country_gold = top_df[(top_df['Golden_Ratio']==top_max_ratio)]['Country_Name'].to_string(index=False)
print (top_country_gold)


# --------------
#Code starts here
data_1 = pd.DataFrame(data)
print (data_1.shape)
data_1.drop(data_1.tail(1).index,inplace=True)
print (data_1.shape)
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total']*1)
most_points = np.max(data_1['Total_Points'])
print (most_points)
best_country = data_1[(data_1['Total_Points']==most_points)]['Country_Name'].to_string(index=False)
print (best_country)


# --------------
#Code starts here




best = pd.DataFrame(data[data['Country_Name']==best_country],columns=['Gold_Total','Silver_Total','Bronze_Total'])
print (best)

best.plot(kind='bar',stacked=True,figsize=(10,8))
# Plot stacked bar chart
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
# Display plot
plt.show()


