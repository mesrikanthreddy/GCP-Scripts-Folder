# Python
def file_deleted(event, context):
    file_name = event['name']
    bucket_name = event['bucket']
    print(f"File {file_name} was deleted from bucket {bucket_name}")

