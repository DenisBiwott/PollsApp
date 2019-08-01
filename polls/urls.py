from django.urls import path
#from django.views.decorators.cache import cache_page

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
#    path('<int:question_id>/vote/', cache_page(60*20)(views.vote), name='vote'),  #Cached vote view with timeout of 1200 seconds
]

