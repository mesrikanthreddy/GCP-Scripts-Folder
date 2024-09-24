# Python
def parse_json(request):
    request_json = request.get_json()
    name = request_json.get('name', 'World')
    return f"Hello, {name}!", 200

# This function demonstrates how to parse JSON input from an HTTP request. It returns a greeting using the name field from the JSON payload.