def cloud_function(request):
    """Google Cloud Function handler."""
    print(request.json)
    return 'Hello, World!', 200
