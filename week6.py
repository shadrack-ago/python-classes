import pandas as pd
data=pd.read_csv('todays_data.csv')
print(data);
data.describe();
data['Gender'].value_counts();

data2=data.value_counts('Academic Level');
data2.plot()
data2.plot.pie()
data3 = data[(data['Country'] == 'Kenya') & (data['Academic Level'] == 'Diploma')]
print(data3)

