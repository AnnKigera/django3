# decorators.py

#from django.http import JsonResponse
#from functools import wraps

# Example decorator for authentication
#def requires_authentication(view_func):
#    @wraps(view_func)
#    def _wrapped_view(request, *args, **kwargs):
#        if request.user.is_authenticated:
#            return view_func(request, *args, **kwargs)
#        else:
#            return JsonResponse({"message": "Authentication required"}, status=401)

#    return _wrapped_view

# Example decorator for logging
#def log_request(view_func):
#    @wraps(view_func)
#    def _wrapped_view(request, *args, **kwargs):
#        # Log information about the request
#        print(f"Received request to {request.path} with data: {request.body.decode('utf-8')}")
#        return view_func(request, *args, **kwargs)

#    return _wrapped_view
