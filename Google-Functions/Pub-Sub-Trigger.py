# Python
import base64

def process_pubsub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(f"Received message: {pubsub_message}")


#This function is triggered by a Pub/Sub topic. It decodes the Pub/Sub message and logs it.

