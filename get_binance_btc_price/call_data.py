from binance.client import Client
import pandas as pd
import csv

from dotenv import load_dotenv
import os
os.chdir("..")
load_dotenv()

import pytz
import tzlocal


#  Time scale variables
min01 = '1m'
min05 = '5m'
min15 = '15m'
min30 = '30m'
min60 = '1h'
min1440 = '1d'

# Time period
day = '1 day ago'
week = '1 week ago'
month = '1 month ago'
year = '1 year ago'


def timezone_converter(fecha, zona_horaria):
    # Gets the right time zone.
    if zona_horaria == "M":
        zona_horaria_loca = tzlocal.get_localzone()
        return fecha.replace(tzinfo=pytz.utc).astimezone(zona_horaria_loca)
    elif zona_horaria == "N":
        # This is my time zone
        zona_horaria_loca = pytz.timezone('America/New_York')
        return fecha.replace(tzinfo=pytz.utc).astimezone(zona_horaria_loca)
    else:
        return 0


def colnames_and_timezone(nombre_archivo):
    # Transforms open_time and close_time columns into a readable format (original format in miliseconds) and returns a file with OHLCV columns.
    df = pd.read_csv(nombre_archivo)

    df.columns = ['o_time', 'open', 'high', 'low', 'close', 'volume', 'c_time', 'qa_time',
                  'number_trades', 'tbav', 'tbav2', 'ignored']

    df['o_time'] = pd.to_datetime(df['o_time'].astype(float)*1000000)
    df['o_time'] = df['o_time'].apply(timezone_converter, args=('M'))
    df['c_time'] = pd.to_datetime(df['c_time'].astype(float)*1000000)
    df['c_time'] = df['c_time'].apply(timezone_converter, args=('M'))

    df.to_csv(nombre_archivo, index = False)

    return df

def api_call_set_csv(key, secret, time_scale, time_period, nombre_archivo, futures, ticker):
    # This function makes a call to binance for downloading the BTC prices.
    client = Client(api_key=key, api_secret=secret)
    if futures == True:
        list_from_api = client.futures_klines(symbol=ticker, interval=time_scale, start_str=time_period)
    else:
        list_from_api = client.get_historical_klines(symbol=ticker, interval=time_scale, start_str=time_period)


    csv_file = open(nombre_archivo, 'w', newline='')
    line_writer = csv.writer(csv_file, delimiter=',')
    for indice in list_from_api:
        line_writer.writerow(indice)
    csv_file.close()
    df = colnames_and_timezone(nombre_archivo)
    return df


## Example: Save and display the data.
os.chdir(os.getenv("CRYPTO"))
data_base_name = 'btc_price'

db = api_call_set_csv(os.getenv("API_KEY"), os.getenv("SECRET_KEY"), min60, year, data_base_name + ".csv", False, "BTCUSDT")
print(db)
