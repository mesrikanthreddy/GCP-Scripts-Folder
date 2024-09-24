from google.cloud import monitoring_v3
from google.api import metric_pb2 as ga_metric
from google.api import label_pb2 as ga_label
import time

# Set up Monitoring client
client = monitoring_v3.MetricServiceClient()
project_name = f"projects/YOUR_PROJECT_ID"

# Function to create a custom metric
def create_custom_metric():
    descriptor = ga_metric.MetricDescriptor()
    descriptor.type = 'custom.googleapis.com/my_custom_metric'
    descriptor.metric_kind = ga_metric.MetricDescriptor.MetricKind.GAUGE
    descriptor.value_type = ga_metric.MetricDescriptor.ValueType.DOUBLE
    descriptor.description = 'This is a custom metric for monitoring usage.'

    descriptor = client.create_metric_descriptor(name=project_name, metric_descriptor=descriptor)
    print(f'Created {descriptor.name}')

# Function to write custom metric data
def write_custom_metric(value):
    series = monitoring_v3.TimeSeries()
    series.metric.type = 'custom.googleapis.com/my_custom_metric'
    
    # Add a label to the metric
    series.resource.type = 'global'
    
    point = series.points.add()
    point.value.double_value = value
    point.interval.end_time.seconds = int(time.time())
    
    client.create_time_series(name=project_name, time_series=[series])
    print(f"Custom metric data point {value} written.")

if __name__ == "__main__":
    create_custom_metric()
    for i in range(5):
        write_custom_metric(i * 10)
        time.sleep(60)  # Sleep for 1 minute
