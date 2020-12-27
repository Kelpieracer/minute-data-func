import datetime
import logging
from ..src.start import fetch_stock_data

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    fetch_stock_data(just_one_ticker=False)
    logging.info('All tickers processed.')
