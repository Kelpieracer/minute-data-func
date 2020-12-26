# Reads minute stock data from Yahoo and uploads it to Azure table storage
# (c) 2020 Kelpieracer

import os
from azure.cosmosdb.table.tableservice import TableService
from .insert_or_replace_minutedata_to_tablestorage import insert_or_replace_minutedata_to_tablestorage
from dotenv import load_dotenv
from .get_week_of_minutedata_from_yahoo import get_week_of_minutedata_from_yahoo

tickers = ['MES=F', 'M2K=F', '^OMXH25', 'MNQ=F', '^OMXHGI', '^GDAXI',
           'NOKIA.HE', 'OUT1V.HE', 'NESTE.HE', 'FORTUM.HE', '^OMXS30GI', 'TYRES.HE']


def fetch_stock_data(just_one_ticker):
    load_dotenv()
    account_key = os.environ.get("account_key")
    account_name = os.environ.get("account_name")
    table_name = os.environ.get("table_name")

    table_client = TableService(
        account_name=account_name, account_key=account_key)

    for ticker in tickers:
        minutedata = get_week_of_minutedata_from_yahoo(ticker)
        insert_or_replace_minutedata_to_tablestorage(
            table_client, table_name, ticker, minutedata)
        if(just_one_ticker):
            return
