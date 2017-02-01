from . import models


class ActivityMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        if request.user.is_authenticated():
            user = models.Registration.objects.get(user=request.user)
            entry = models.Activity(
                    user_responsible=user,
                    description="Accessed: " + request.path,
                    activity_type=models.Activity.RECORD
                )
            entry.save()
