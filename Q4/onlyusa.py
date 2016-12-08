import pandas as pd
import csv

tempforusa = pd.read_csv('TEMP.csv')
usa = tempforusa[tempforusa.Country == "United States"]
print usa.head()

usa.to_csv('usa.csv')
