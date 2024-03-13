# decorators.py

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from functools import wraps

def login_required_ajax(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check for the AJAX header instead of using request.is_ajax()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if not request.user.is_authenticated:
                return JsonResponse({'login_required': True}, status=403)
        else:
            # For non-AJAX requests, use the standard login_required decorator
            return login_required(view_func)(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return _wrapped_view