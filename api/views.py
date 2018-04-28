from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import View
# Create your views here.

class Test(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super(Test, self).dispatch(request, *args, **kwargs)

  def get(self, request):
    return JsonResponse("OK", safe=False)