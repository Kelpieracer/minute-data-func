import logging
import azure.functions as func
from ..src.start import fetch_stock_data


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processinf a request.')

    test = req.params.get('test')
    if test:
        fetch_stock_data(just_one_ticker=True)
        logging.info('1 ticker processed.')
        return func.HttpResponse("Fetched data for 1 ticker.")
    else:
        fetch_stock_data(just_one_ticker=False)
        logging.info('All tickers processed.')
    return func.HttpResponse("Fetched data for all tickers.")
