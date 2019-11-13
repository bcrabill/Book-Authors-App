from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^', views.index),
    url(r'^authors/$', views.authors),
    #url(r'^authors/(?P<id>$)', views.authorspage)
    url(r'^books/(?P<book_id>)$', views.bookspage),
]