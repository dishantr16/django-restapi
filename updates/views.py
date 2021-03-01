import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from restapi.mixins import JsonResponseMixin
from .models import Update

# def detail_view(request):
#     return HttpResponse(get_template().render({}))

def json_example_view(request):
    data = {
        "count":100,
        "content":"Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

def JsonCBV(View):
    
    def get(self,request,*args, **kwargs):
        data = {
            "count":1000,
            "content":"Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        data = {
            "count":1000,
            "content":"Some new content"
        }
        return self.render_to_json_respone(data)



