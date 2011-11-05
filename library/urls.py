from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource

from books.handlers import BookHandler

book_resource = Resource(BookHandler)

urlpatterns = patterns('',
    (r'^book/(?P<id>[^/.])', book_resource)
)
