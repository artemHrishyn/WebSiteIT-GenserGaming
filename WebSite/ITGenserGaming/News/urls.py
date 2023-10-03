from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDatailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewDeleteView.as_view(), name='news-delete')
]