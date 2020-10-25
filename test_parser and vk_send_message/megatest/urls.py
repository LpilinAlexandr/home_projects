from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('getnames', views.pooling),
    path(r'<str:slug>/', views.NamesDetails.as_view(), name='name_url')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





