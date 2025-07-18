from django.urls import path
from . import views
urlpatterns = [
    path('', views.edit_quote_view, name='edit_start'),
    path('/edit/<int:pk>', views.EditQuoteView.as_view(), name='editquote'),
    path('/addquote/<int:pk>', views.AddQuoteView.as_view(), name='addquote'),
    path('/deletequote/<int:pk>', views.delete_quote, name='deletequote'),
    path('/addsource', views.AddSourceView.as_view(), name='addsource'),
    path('/deletesource/<int:pk>', views.delete_source, name='deletesource')
]