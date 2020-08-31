from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/list/', views.page_list, name='page-list'),
    path('pages/detail/<int:page_id>/', views.page_detail, name='page-detail'),
]
