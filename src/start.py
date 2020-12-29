# Reads minute stock data from Yahoo and uploads it to Azure table storage
# (c) 2020 Kelpieracer

import os
from azure.cosmosdb.table.tableservice import TableService
# from .insert_or_replace_minutedata_to_tablestorage
from .insert_or_replace_minutedata_to_tablestorage import insert_or_replace_minutedata_to_tablestorage
from dotenv import load_dotenv
from .get_week_of_minutedata_from_yahoo import get_week_of_minutedata_from_yahoo

# change this to 'HOUR' or 'MINUTE' depending on timespan you want

tickers = ['MES=F', 'MNQ=F', '^GDAXI', '^STOXX50E',
           'NOKIA.HE', 'OUT1V.HE', 'NESTE.HE', 'FORTUM.HE', '^OMXS30GI', 'TYRES.HE',
           'CL=F', 'GC=F', 'BTC=F',
           # Minifutures
           'AMD',
           'BABA',
           'GOOG',
           'AMZN',
           'AAPL',
           'ELISA.HE',
           'FB',
           'INTC',
           'MA',
           'MU',
           'MSFT',
           'NFLX',
           'NVDA',
           'ORNBV.HE',
           'SPOT',
           'TSLA',
           'TWTR',
           'MYM=F',
           'M2K=F',
           # FN25
           'ABSO.ST',
           'ADMCM.HE',
           'AKEL-D.ST',
           'AMAST.ST',
           'AZELIO.ST',
           'CIBUS.ST',
           'CLIME-B.ST',
           'DETEC.HE',
           'EMBRAC-B.ST',
           'EG7.ST',
           'ENZY.ST',
           'FARON.HE',
           'GENO.ST',
           'IMP-A-SDB.ST',
           'KAMBI.ST',
           'MINEST.ST',
           'MNTC.ST',
           'NANOFH.HE',
           'OFFHUS.ST',
           'OVZON.ST',
           'PCELL.ST',
           'PDX.ST',
           'REMEDY.HE',
           'SDIP-B.ST',
           'SEDANA.ST',
           'SIVE.ST',
           'SEYE.ST',
           'SPEC.ST',
           'SF.ST',
           'STORY-B.ST',
           'SUS.ST',
           'SECARE.ST',
           'VEFL-SDB.ST',
           # Interesting
           '^OMXH25',
           '^OMXHGI',
           'BTC=F',
           '18MF.DE',
           'DBPK.DE',
           ]


def fetch_stock_data(just_one_ticker, data_time_span):
    load_dotenv()
    account_key = os.environ.get("account_key")
    account_name = os.environ.get("account_name")
    table_name = os.environ.get(
        "minute_table_name") if data_time_span != 'HOUR' else os.environ.get("hour_table_name")

    table_client = TableService(
        account_name=account_name, account_key=account_key)

    for ticker in tickers:
        minutedata = get_week_of_minutedata_from_yahoo(ticker, data_time_span)
        insert_or_replace_minutedata_to_tablestorage(
            table_client, table_name, ticker, minutedata)
        if just_one_ticker:
            return
