import datetime
import logging
from ..src.start import fetch_stock_data

import azure.functions as func


def main(mykickertimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mykickertimer.past_due:
        logging.info('The kicker timer is past due!')

    logging.info(
        'Python kicker timer trigger function ran at %s', utc_timestamp)
