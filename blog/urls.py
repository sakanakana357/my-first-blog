from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

#post_listというviewを""urlに割り当ててる
urlpatterns = [
    path("", views.post_list, name="post_list")
]