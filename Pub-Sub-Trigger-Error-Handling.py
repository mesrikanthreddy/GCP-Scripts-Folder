# Python
import base64

def handle_pubsub(event, context):
    try:
        message = base64.b64decode(event['data']).decode('utf-8')
        print(f"Processing message: {message}")
        # Process the message here
    except Exception as e:
        print(f"Error processing message: {e}")
        raise e
# This function is triggered by a Pub/Sub topic. It decodes the Pub/Sub message and processes it. If an error occurs, it logs the error and re-raises it.