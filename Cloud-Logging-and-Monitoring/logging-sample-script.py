from google.cloud import logging
import logging as python_logging

# Instantiates a client
client = logging.Client()

# Sets up a Cloud Logging handler
cloud_handler = client.get_default_handler()
cloud_logger = python_logging.getLogger('cloudLogger')

# Add the Cloud Logging handler to Python's logger
cloud_logger.setLevel(python_logging.INFO)
cloud_logger.addHandler(cloud_handler)

# Example log message
def log_message():
    cloud_logger.info("This is an info message sent to Google Cloud Logging!")
    cloud_logger.warning("This is a warning message.")
    cloud_logger.error("This is an error message.")
    
if __name__ == "__main__":
    log_message()