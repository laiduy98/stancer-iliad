import logging
from stancer_client.client import StancerClient
from stancer_client.exceptions import AuthenticationError, APIRequestError
from stancer_client.config import settings

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    client = StancerClient(settings.dsp2_username, settings.dsp2_password)
    try:
        logger.info("Identity.............................")
        identity = client.get_identity()
        logger.info(identity)

        logger.info("Accounts...........................")
        accounts = client.get_accounts()
        logger.info(accounts)
        for acc in accounts:
            logger.info("Account........................ %s", acc)

            logger.info("Balances........................")
            balances = client.get_balances(acc.id)
            for bal in balances:
                logger.info("Balance..................... %s", bal)

            logger.info("Transactions.....................")
            transactions = client.get_transactions(acc.id, page=1, count=10)
            for tran in transactions:
                logger.info("Transaction................. %s", tran)

    except AuthenticationError as e:
        logger.error("Authentication failed: %s", str(e))
    except APIRequestError as e:
        logger.error("API request failed: %s", str(e))
    except Exception as e:
        logger.error("Unexpected error: %s", str(e))

if __name__ == "__main__":
    main()
