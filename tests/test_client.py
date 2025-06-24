from stancer_client.client import StancerClient
from stancer_client.exceptions import AuthenticationError, APIRequestError
from stancer_client.config import settings


def main():
    client = StancerClient(settings.dsp2_username, settings.dsp2_password)
    try:
        print("Identity.............................")
        identity = client.get_identity()
        print(identity)

        print("\nAccounts...........................")
        accounts = client.get_accounts()
        for acc in accounts:
            print("\nAccount........................", acc)

            print("\nBalances........................")
            balances = client.get_balances(acc.id)
            for bal in balances:
                print("\nBalance.....................", bal)

            print("\nTransactions.....................")
            transactions = client.get_transactions(acc.id, page=1, count=10)
            for tran in transactions:
                print("\nTransaction.................", tran)

    except AuthenticationError as e:
        print("Authentication failed:", e)
    except APIRequestError as e:
        print("API request failed:", e)
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
