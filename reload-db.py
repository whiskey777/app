from django.db import connection
import requests
import psycopg2
from psycopg2 import Error
from datetime import date, timedelta
import xmltodict  # pip install xmltodict

# Setup timeframe for the request to CBR
dateFrom = (date.today() + timedelta(days=-3)).strftime('%d/%m/%Y')
dateTo = date.today().strftime('%d/%m/%Y')

# Setup url and payload. Obviously.
URL = 'https://www.cbr.ru/scripts/xml_metall.asp'
payload = {
    "date_req1": dateFrom,
    "date_req2": dateTo,
}

# executing request to CBR
response = requests.get(
    URL,
    params = payload
)

# parsing XML response to python dictionary
response_dict = xmltodict.parse(response.content)

# Creating SQL query string
sql = "INSERT INTO metals_metal (date, code, name, buy, sell) VALUES(%s,%s,%s,%s,%s)"
# Trying to establish connection to django database - check connections settings in settings.py
try:
    print("Reloading Metals_metal table with data")
    print("Connecting to postgresDB django")
    connection = psycopg2.connect(user="django",
                                  password="django",
                                  host="database",
                                  port="5432",
                                  database="django")
    # Creating cursor for further work with the DB
    cursor = connection.cursor()
    # Delete all present data in metals table
    cursor.execute("DELETE from metals_metal;")    
    # Parsing dictionary                          
    for response_key in response_dict:
        first_lvl_dict = response_dict[response_key]
        for first_lvl_key in first_lvl_dict:
            if first_lvl_key == 'Record':
                records_dict = first_lvl_dict[first_lvl_key]
                for obj in records_dict:
                    record_date = obj['@Date']
                    metal_code = obj['@Code']
                    match metal_code:
                        case '1':
                            metal_name = 'Gold'
                        case '2':
                            metal_name = 'Silver'
                        case '3':
                            metal_name = 'Platinum'
                        case '4':
                            metal_name = 'Palladium'
                    metal_buy_price = obj['Buy']
                    metal_sell_price = obj['Sell']
                    cursor.execute(sql, (record_date, metal_code, metal_name, metal_buy_price, metal_sell_price))
    connection.commit()
except (Exception, Error) as error:
    print("Error when trying to connect PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection to PostgresSQL closed")


            
                
                


                

                


