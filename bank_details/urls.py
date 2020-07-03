
from django.conf.urls import url, include
from django.contrib import admin
from api.views import UploadView  

urlpatterns = [
    url('admin/', admin.site.urls),
    url('upload/', UploadView.as_view(), name='upload'),
    url('api/', include('api.urls'))
]

