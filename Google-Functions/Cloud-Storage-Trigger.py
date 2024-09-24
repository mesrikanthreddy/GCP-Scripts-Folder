# Python
def file_uploaded(event, context):
    file_name = event['name']
    bucket_name = event['bucket']
    print(f"File {file_name} uploaded to bucket {bucket_name}")

# This function is triggered by a Cloud Storage bucket. It logs the name of the uploaded file and the bucket it was uploaded to.