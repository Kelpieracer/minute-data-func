import yfinance as yf


def get_week_of_minutedata_from_yahoo(ticker, data_time_span):
    interval = '1m'
    period = '7d'
    if data_time_span == 'HOUR':
        interval = '60m'
        period = '730d'
    data = yf.download(ticker, interval=interval,
                       period=period, group_by="ticker")
    return data


# get_week_of_minutedata_from_yahoo('NOKIA.HE', 'HOUR')
# get_week_of_minutedata_from_yahoo('NOKIA.HE', 'MINUTE')
