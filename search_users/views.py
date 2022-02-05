import json

from django.http import JsonResponse

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseFormView

from search_users.models import User


class UserTV(TemplateView):
    template_name = "search_users/user_index.html"


class UseridDV(BaseFormView):
    def get_object(self, queryset=None):
        if self.kwargs["pk"] != "":
            return User.objects.filter(user_id=self.kwargs["pk"]).values()
        else:
            return User.objects.none()

    def get(self, request, *args, **kwargs):
        user_info = self.get_object()
        if not user_info:
            return JsonResponse(data={})
        return JsonResponse(data=user_info[0])

    def post(self, request, *args, **kwargs):
        user_info = self.get_object()[0]
        if not user_info:
            return JsonResponse(data={})
        new_item = json.loads(self.request.body)
        ((new_key, new_value),) = new_item.items()
        if new_key != "inventory":
            new_item = {new_key: int(new_value)}
        User.objects.filter(pk=user_info["user_id"]).update(**new_item)
        return JsonResponse(data=user_info)
