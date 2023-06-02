from django.http import Http404, HttpRequest
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class RestrictStaffToAdminMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> None:
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated:
                if not request.user.is_staff:
                    raise Http404
            else:
                raise Http404
