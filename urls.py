from django.conf.urls import url
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^product/$',views.productApi),
    url(r'^product/([0-9]+)$',views.productApi),

    url(r'^employee/$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
