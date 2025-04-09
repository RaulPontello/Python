# Import libraries

import json
import boto3
import datetime
import sys

from requests import Session
from awsglue.utils import getResolvedOptions

# Import database libraries

import pymysql   # for MySQL

# Create functions

def extract_data_from_api() -> dict:
    """
    Extracts cryptocurrency data from the CoinMarketCap API.

    Documentation: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap

    Returns:
        dict: The response from the CoinMarketCap API, parsed as a JSON object, containing 
              cryptocurrency listings data.
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    api_key = '83f659b5-cb23-45e9-87f2-733a317f404d'

    parameters = {
        'start': '1',
        'limit': '1000',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    return json.loads(response.text)


def get_secret(secret_name: str, region_name: str) -> dict:
    """
    Retrieves a secret value from AWS Secrets Manager.

    Args:
        secret_name (str): The name of the secret to retrieve from AWS Secrets Manager.
        region_name (str): The AWS region where the secret is stored.

    Returns:
        dict: The value of the secret, parsed as a JSON object.
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except Exception as e:
        raise e

    return json.loads(get_secret_value_response['SecretString'])

# Get input variables

arguments = ['secret_name', 'aws_region', 'database_name', 'database_host']
args = getResolvedOptions(sys.argv, arguments)
print(f'args: {args}')

# Get data from API

print("Get data from API - BEGIN")

data = extract_data_from_api()

print("Get data from API - END")

# Get secret

print("Get secret - BEGIN")

secret_name = args['secret_name']
aws_region = args['aws_region']
secret = get_secret(secret_name, aws_region)

print("Get secret - END")

# Connect to database

print("Connect to database - BEGIN")

connection = pymysql.connect(
      database=args['database_name'],
      host=args['database_host'],
      user=secret['username'],
      password=secret['password'],
      cursorclass=pymysql.cursors.DictCursor
  )

cursor = connection.cursor()

print("Connect to database - END")

# Create table

print("Create table - BEGIN")

query = '''create table if not exists crypto_table (
              id int, 
              name varchar(100), 
              symbol varchar(100), 
              last_updated date,
              circulating_supply float, 
              total_supply float, 
              max_supply float, 
              price float,
              volume_24h float, 
              percent_change_1h float, 
              percent_change_7d float 
              )
              '''

cursor.execute(query)

print("Create table - END")

# Insert data

print("Insert data - BEGIN")

for index, row in enumerate(data['data'], start = 1):
    print(f"Insert data - index: {index}")
    
    query = '''INSERT INTO crypto_table

              (id, name, symbol, last_updated, circulating_supply, total_supply, 
                max_supply, price, volume_24h, percent_change_1h, percent_change_7d) 

              values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    id = row['id']
    name = row['name']
    symbol = row['symbol']
    last_updated = row['last_updated'][0:10]
    last_updated = row['last_updated'] 
    circulating_supply = row['circulating_supply']
    total_supply = row['total_supply']
    max_supply = row['max_supply']
    price = row['quote']['USD']['price']
    volume_24h = row['quote']['USD']['volume_24h']
    percent_change_1h = row['quote']['USD']['percent_change_1h']
    percent_change_7d = row['quote']['USD']['percent_change_7d']

    values = id, name, symbol, last_updated, circulating_supply, total_supply, \
            max_supply, price, volume_24h, percent_change_1h, percent_change_7d 

    cursor.execute(query, values)

connection.commit()

print("Insert data - END")

# Check data inside database

print("Check data inside database - BEGIN")

query = '''SELECT * FROM crypto_table'''
cursor.execute(query)
print(cursor.fetchmany(5))

print("Check data inside database - END")

# Close all database connections

cursor.close()
connection.close()