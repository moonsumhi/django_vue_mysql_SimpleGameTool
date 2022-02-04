from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from search_users.models import User


class UserTV(TemplateView):
    template_name = "search_users/user_index.html"


class UseridLV(BaseDetailView):
    def get_queryset(self):
        if self.kwargs != "":
            return User.objects.filter(user_id=self.kwargs["user_id"])
        else:
            return User.objects.none()

    def render_to_response(self, context, **response_kwargs):
        user_info = list(context["object_list"].values())
        return JsonResponse(data=user_info, safe=False)

    # model.objects.get()
    # try:
    #     cursor = connection.cursor()
    #
    #     strSql = "SELECT code, name, author FROM bookstore_book"
    #     result = cursor.execute(strSql)
    #     books = cursor.fetchall()
    #
    #     connection.commit()
    #     connection.close()
    #
    # except:
    #     connection.rollback()
    #     print("Failed selecting in BookListView")
    #
    # return render(request, "book_list.html", {"books": books})
