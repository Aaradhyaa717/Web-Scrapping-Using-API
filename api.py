import requests
import requests_cache
import json
import pandas as pd

'''
website_used = 'https://currencylayer.com/'
'''
headers = {
    'user-agent': 'Data',
}

payload = {
     'access_key':'7ce5dc30383fa31a5a9cc8fa85162c06',
    'format': 'json'
}


r= requests.get('http://apilayer.net/api/historical?date=2020-12-05',headers=headers,params=payload)

#date parameter can be changed


print(r.status_code)

def json_result(obj):
  # create a formatted string of the Python JSON object
  result = json.dumps(obj, sort_keys=True, indent=4)
  return result

output = json_result(r.json()['quotes'])

output = json.loads(output)

#print(output)


def getKey(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key) 
          
    return list

def getValue(dict):
  val=[]
  for value in dict.values():
    val.append(value)
  return val  

currencies = getKey(output)
rate = getValue(output)

country=[]
for currency in currencies:
  currrency=currency[3:]
  country.append(currency)

#print(currencies)
#print(rate)

currencies_rate_dict= {
  'country': country,
  'rate':rate
}
#print(currencies_rate_dict)

df= pd.DataFrame.from_dict(currencies_rate_dict)

df.index += 1
print(df)

