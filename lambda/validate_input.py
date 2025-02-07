def validate_handler(event, context):
    print("Received event:", event)
    
    if "key1" not in event:
        raise ValueError("Missing key1 in input!")
    return {"status": "validated"}
