import os
from google.cloud import container_v1
from google.auth import default

# Set up Google Cloud credentials
credentials, project = default()

# Set your desired cluster configuration
cluster_name = "my-gke-cluster"
zone = "us-central1-a"
node_count = 5

# Initialize the GKE client
client = container_v1.ClusterManagerClient(credentials=credentials)

# Construct the parent resource
parent = f"projects/{project}/locations/{zone}"

# Define the cluster configuration
cluster = {
    "name": cluster_name,
    "initial_node_count": node_count,
    "node_config": {
        "machine_type": "e2-medium",
        "disk_size_gb": 100,
        "oauth_scopes": [
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
            "https://www.googleapis.com/auth/service.management.readonly",
            "https://www.googleapis.com/auth/servicecontrol",
            "https://www.googleapis.com/auth/trace.append",
        ],
    },
}

# Create the cluster
print(f"Creating cluster {cluster_name} in {zone}...")
operation = client.create_cluster(parent=parent, cluster=cluster)

# Wait for the operation to complete
response = operation.result()

print(f"Cluster {cluster_name} created successfully!")
print(f"Cluster endpoint: {response.endpoint}")
print(f"Cluster status: {response.status}")