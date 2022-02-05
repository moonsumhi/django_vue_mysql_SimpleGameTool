from django.db import connection
from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from search_users.models import User


class UserTV(TemplateView):
    template_name = "search_users/user_index.html"


class UseridDV(BaseDetailView):
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


class UserinfoDV(BaseDetailView):
    pass
