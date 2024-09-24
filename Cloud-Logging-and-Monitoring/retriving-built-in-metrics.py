def list_monitored_resources():
    resource_client = monitoring_v3.MetricServiceClient()
    request = monitoring_v3.ListMonitoredResourceDescriptorsRequest(name=project_name)
    resource_list = resource_client.list_monitored_resource_descriptors(request=request)
    
    for resource in resource_list:
        print(resource.type, resource.display_name)