# Python
def firestore_trigger(event, context):
    new_value = event['value']['fields']
    print(f"New document created: {context.resource['name']}")
    print(f"Document content: {new_value}")

#This function is triggered when a document is created in Firestore. It logs the document ID and content.