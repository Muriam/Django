from django.urls import path
from . import views


urlpatterns = [
    path('', views.func_get, name='func_get'), # GET запрос
    path('submit/', views.func_post, name='func_post'), # POST запрос (куда будет отправляться форма)
    path('test-db/', views.test_db, name='test_db'),    # при клике на ссылку открывается новая страница для тестов БД
]
