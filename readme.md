# MinuteData function

## Create your own history of 1 minute interval stock and index data

This is an Azure function app, with the purpose of fetching minute stock/index price data from yahoo.finance.com, for futher processing for use in stock analysis.
The data is then stored to Azure table storage, capable of storing large quantities of data at low cost.
The tickers selected based on Nordnet Markets Finland offering of Unlimited Turbos for expense free trading, but you are free to repace the tickers with your own choices.
Yahoo offers minute data only for the past 7 days, therefore this application is continously fetching more data.

## Two triggers are provided

- Timer trigger fetches data every 4 hours.
- Http trigger can be used to force data fetch by just accessing the url with http-get, for example in order to test it. The url is `<host-name>/api/fetch-minute-data`. If this url is extended with parameter ´´´?test=1´´´ then data for only one ticker will be fetched.

## Tickers

The tickers which are fetched are provided in start.py:

- Micro E-mini Nasdaq-100 Index F (MNQ=F)
- Micro E-mini S&P 500 Index Futu (MES=F)
- Micro E-mini Russell 2000 Index (M2K=F)
- DAX PERFORMANCE-INDEX (^GDAXI)
- OMX Helsinki 25 (^OMXH25)
- XCSE:OMX Helsinki GI (^OMXHGI)
- OMX Stockholm 30_GI (^OMXS30GI)
- Nokia Corporation (NOKIA.HE)
- Outokumpu Oyj (OUT1V.HE)
- Neste Oyj (NESTE.HE)
- Fortum Oyj (FORTUM.HE)
- Nokian Renkaat Oyj (TYRES.HE)

## Azure table storage

The data is stored in azure table storage. You need to provide a `.env` file in the `src` folder with the following contents:

```
account_key = '<your_account_key>'
account_name = '<your_account_name>'
table_name = '<existing_table_name_for_storing_the_data>'
```
