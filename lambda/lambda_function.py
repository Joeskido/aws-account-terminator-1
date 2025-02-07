BLOCKED_ACCOUNTS = ["account1", "account2", "account3"]

def validate_handler(event, context):
    account_id = event.get("accountId")
    if not account_id:
        raise Exception("Account ID is required.")
    
    if account_id in BLOCKED_ACCOUNTS:
        raise Exception(f"Account {account_id} is permanently blocked from deletion.")
    
    print(f"Account {account_id} passed validation.")
