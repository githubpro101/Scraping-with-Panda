import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]
df = first_table
symbols = df['Symbol'].values.tolist()
print(symbols)


#source:https://tcoil.info/how-to-get-list-of-companies-in-sp-500-with-python/
#https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org