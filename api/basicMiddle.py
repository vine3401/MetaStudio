import base64

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from account.models import User


class PermissionMiddleware(object):

    def is_permit(self, permissions, request):
        METHOD = request.method
        URI = request.path
        for permission in permissions:
            if permission.uri == URI and permission.method == METHOD:
                return True
        return False

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method is not "GET":
            if request.META.get("HTTP_AUTHORIZATION", None) is None:
                return HttpResponse(status=401)