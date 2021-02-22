from django.shortcuts import redirect

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
