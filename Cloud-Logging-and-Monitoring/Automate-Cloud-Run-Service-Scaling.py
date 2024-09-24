import time
from google.cloud import monitoring_v3
from googleapiclient import discovery

PROJECT_ID = "your-project-id"
REGION = "your-region"
CLOUD_RUN_SERVICE = "your-cloud-run-service-name"

# Initialize the Cloud Run and Monitoring clients
monitoring_client = monitoring_v3.MetricServiceClient()
cloud_run_client = discovery.build('run', 'v1')

# Function to check if the Cloud Run service has received traffic in the last 30 days
def check_service_traffic(service_name, project_id):
    now = time.time()
    one_month_ago = now - (30 * 24 * 60 * 60)  # 30 days ago
    project_name = f"projects/{project_id}"

    interval = monitoring_v3.TimeInterval(
        end_time={"seconds": int(now)},
        start_time={"seconds": int(one_month_ago)},
    )
    
    results = monitoring_client.list_time_series(
        request={
            "name": project_name,
            "filter": 'metric.type="run.googleapis.com/request_count" AND '
                      f'resource.labels.service_name="{service_name}"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
    )
    
    traffic_received = False
    for result in results:
        if result.points:
            traffic_received = True
            break
    
    return traffic_received

# Function to scale Cloud Run service to zero
def scale_cloud_run_service_to_zero(service_name, project_id, region):
    service_path = f"projects/{project_id}/locations/{region}/services/{service_name}"
    # Patch the service to set "minInstanceCount" to 0
    request = cloud_run_client.projects().locations().services().patch(
        name=service_path,
        body={"spec": {"template": {"metadata": {"annotations": {"autoscaling.knative.dev/minScale": "0"}}}}},
        updateMask="spec.template.metadata.annotations"
    )
    response = request.execute()
    print(f"Scaled down service {service_name} to zero instances")
    return response

if __name__ == "__main__":
    # Check if the service has received traffic in the last 30 days
    has_traffic = check_service_traffic(CLOUD_RUN_SERVICE, PROJECT_ID)
    
    if not has_traffic:
        print(f"No traffic detected for service {CLOUD_RUN_SERVICE} in the last 30 days. Scaling down...")
        scale_cloud_run_service_to_zero(CLOUD_RUN_SERVICE, PROJECT_ID, REGION)
    else:
        print(f"Service {CLOUD_RUN_SERVICE} is still receiving traffic. No scaling action taken.")