"""
URL configuration for orm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.orm, name='orm'),
    path('author/<int:author_id>/', views.specific_author, name='specific_author'),  #find details for specific authhor
]  


AUTHOR_URLS = [
    path("list-author", views.list_author, name="list-author"),
    path("get-author/<int:author_id>", views.get_author, name="get-author"),
    path("create-author", views.create_author, name="create-author"),
    path("update-author/<int:author_id>", views.update_author, name="update-author"),
    path("patch-author/<int:author_id>", views.patch_author, name="patch-author"),
    path("delete-author/<int:author_id>", views.delete_author, name="delete-author"),
]



BOOK_URLS = [
    path("list-book", views.list_book, name="list-book"),
    path("get-book/<int:book_id>", views.get_book, name="get-book"),
    path("create-book", views.create_book, name="create-book"),
    path("update-book/<int:book_id>", views.update_book, name="update-book"),
    path("patch-book/<int:book_id>", views.patch_book, name="patch-book"),
    path("delete-book/<int:book_id>", views.delete_book, name="delete-book"),
]

urlpatterns.extend(AUTHOR_URLS)
urlpatterns.extend(BOOK_URLS)

