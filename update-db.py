import requests
import psycopg2
import json
from datetime import date, timedelta
import xmltodict  # pip install xmltodict

dateFrom = (date.today() + timedelta(days=-3)).strftime('%d/%m/%Y')
dateTo = date.today().strftime('%d/%m/%Y')

URL = 'https://www.cbr.ru/scripts/xml_metall.asp'
payload = {
    "date_req1": dateFrom,
    "date_req2": dateTo,
}

xmlresponse = requests.get(
    URL,
    params = payload
)
dictresponse =  xmltodict.parse(xmlresponse.text)
json_in=json.dumps(dictresponse)

print (json_in)