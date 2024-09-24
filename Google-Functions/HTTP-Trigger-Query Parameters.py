# Python
def say_hello(request):
    name = request.args.get('name', 'World')
    return f"Hello, {name}!", 200


#This function demonstrates how to handle query parameters in an HTTP request. It returns a greeting using the name query parameter.