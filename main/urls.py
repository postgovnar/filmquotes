from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_quote_view, name="main"),
    path('quote/<int:qid>/vote/', views.vote, name='vote'),
]
