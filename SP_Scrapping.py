##############################################################################
# Scrapping the S&P 500 Components with weights

# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# read HTML URL from Wikipedia

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# read html data table
html_table = soup.find("table", attrs={"class":"wikitable"})

# read the table lines added between <tr> tags
html_table_data = html_table.tbody.find_all("tr")

# extract the table headers
table_head = []

for a in html_table_data[0].find_all('th'):
    table_head.append(a.text.replace('\n',''))

#extract data from the table

table_data = []
for a in html_table_data:
    row = []
    for b in a.find_all('td'):
        row.append(b.text.replace('\n',''))
    table_data.append(row)

# join the header and data into a pandas DataFrame
df = pd.DataFrame.from_records(table_data[1:len(table_data)], columns = table_head)


df.to_csv("data/SP500_Components.csv")

### Alternative way of pulling the data into a pandas dataframe directly:
# read_html will provide a list of dataframes from tables
# the second step is to convert list to dataframe

# df_ini = pd.read_html(str(html_table))
# df = pd.DataFrame(df_ini[0])

