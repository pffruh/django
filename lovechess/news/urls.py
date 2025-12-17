from django.urls import path
from . import views
# from .views import NewsDetailView
# from .views import NewsUpdateView

urlpatterns = [
    path('', views.news, name='news'),
    path('create_news', views.create_news, name='create_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail_view'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update_news'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_news')

]
    
    
