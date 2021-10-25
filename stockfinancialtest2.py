import requests
import lxml.html as lh
import pandas as pd

url='https://www.wsj.com/market-data/quotes/YEWB/financials/quarter/income-statement'
dfs = pd.read_html(url)
df = dfs[0]
df.iloc[:3]
df.to_excel('python.xlsx')


#source: https://pythonbasics.org/pandas-web-scraping/

#urllib.error.HTTPError: HTTP Error 403: Forbidden - WSJ dont allow this