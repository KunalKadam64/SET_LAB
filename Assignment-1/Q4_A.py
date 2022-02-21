import pandas as pd
data = pd.read_csv('C:\\Users\Pragati Kadam\Downloads\Toyota.csv')
data.plot.scatter(x="Age",y="Price")