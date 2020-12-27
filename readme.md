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

The tickers which are fetched are listed in `start.py`:

### Unlimited turbos, index

- Micro E-mini Nasdaq-100 Index F (MNQ=F)
- Micro E-mini S&P 500 Index Futu (MES=F)
- DAX PERFORMANCE-INDEX (^GDAXI)
- ESTX 50 PR.EUR (^STOXX50E)
- OMX Stockholm 30_GI (^OMXS30GI)

### Unlimited turbos, stock

- Nokia Corporation (NOKIA.HE)
- Outokumpu Oyj (OUT1V.HE)
- Neste Oyj (NESTE.HE)
- Fortum Oyj (FORTUM.HE)
- Nokian Renkaat Oyj (TYRES.HE)

### Unlimited turbos, commodities

- Crude Oil Feb 21 (CL=F)
- Gold Feb 21 (GC=F)

### Minifutures, stock (in addition to turbos)

- Advanced Micro Devices, Inc. (AMD)
- Alibaba Group Holding Limited (BABA)
- Alphabet Inc. (GOOG)
- Amazon.com, Inc. (AMZN)
- Apple Inc. (AAPL)
- Elisa Oyj (ELISA.HE)
- Facebook, Inc. (FB)
- Intel Corporation (INTC)
- Mastercard Incorporated (MA)
- Micron Technology, Inc. (MU)
- Microsoft Corporation (MSFT)
- Netflix, Inc. (NFLX)
- NVIDIA Corporation (NVDA)
- Orion Oyj (ORNBV.HE)
- Smart Eye AB (publ) (SEYE.ST)
- Spotify Technology S.A. (SPOT)
- Tesla, Inc. (TSLA)
- Twitter, Inc. (TWTR)

### Minifutures, indexes (in addition to turbos)

- Dow Jones Industrial Average (^DJI)
- Micro E-mini Russell 2000 Index (M2K=F)

### Minifutures, commodities (in addition to turbos)

- E-mini Silver Futures,Mar-2021 (QI=F)

### First North 25

- Absolent Group AB (publ) (ABSO.ST) - removed jan-2021
- Admicom Oyj (ADMCM.HE)
- Akelius Residential Property AB (publ) (AKEL-D.ST)
- Amasten Fastighets AB (publ) (AMAST.ST)
- Azelio AB (publ) (AZELIO.ST) - added jan-2021
- Cibus Nordic Real Estate AB (publ) (CIBUS.ST)
- Climeon AB (publ) (CLIME-B.ST) - removed jan-2021
- Detection Technology Oyj (DETEC.HE) - removed jan-2021
- Embracer Group AB (publ) (EMBRAC-B.ST)
- Enad Global 7 AB (publ) (EG7.ST) - added jan-2021
- Enzymatica AB (ENZY.ST) - removed jan-2021
- Faron Pharmaceuticals Oy (FARON.HE) - removed jan-2021
- Genovis AB (publ.) (GENO.ST) - removed jan-2021
- Implantica AG (IMP-A-SDB.ST) - added jan-2021
- Kambi Group plc (KAMBI.ST)
- Minesto AB (publ) (MINEST.ST)
- Mentice AB (publ) (MNTC.ST) - removed jan-2021
- Nanoform Finland Oyj (NANOFH.HE) - added jan-2021
- Offentliga Hus i Norden AB (publ) (OFFHUS.ST) - added jan-2021
- Ovzon AB (publ) (OVZON.ST) - removed jan-2021
- PowerCell Sweden AB (publ) (PCELL.ST)
- Paradox Interactive AB (publ) (PDX.ST)
- Remedy Entertainment Oyj (REMEDY.HE)
- Sdiptech AB (publ) (SDIP-B.ST)
- Sedana Medical AB (publ) (SEDANA.ST)
- Sivers Semiconductors AB (SIVE.ST) - added jan-2021
- Smart Eye AB (publ) (SEYE.ST) - added jan-2021
- SpectraCure AB (publ) (SPEC.ST) - removed jan-2021
- Stillfront Group AB (publ) (SF.ST)
- Storytel AB (publ) (STORY-B.ST)
- Surgical Science Sweden AB (publ) (SUS.ST)
- Swedencare AB (publ) (SECARE.ST) - added jan-2021
- VEF Ltd. (VEFL-SDB.ST)

### Other interesting

- OMX Helsinki 25 (^OMXH25)
- XCSE:OMX Helsinki GI (^OMXHGI)
- Bitcoin Futures,Jan-2021 (BTC=F)
- Amundi ETF Leveraged MSCI USA Daily UCITS ETF (18MF.DE)
- Xtrackers S&P 500 2x Inverse Daily Swap UCITS ETF 1C (DBPK.DE)

## Azure table storage

The data is stored in azure table storage. You need to provide a `.env` file in the `src` folder with the following contents:

```
account_key = '<your_account_key>'
account_name = '<your_account_name>'
table_name = '<existing_table_name_for_storing_the_data>'
```
