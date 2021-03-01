
from django.http import JsonResponse

class JsonResponseMixin(object):
    def render_to_json_respone(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context