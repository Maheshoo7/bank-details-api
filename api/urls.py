from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import bank_detail_view, banks_list_view

urlpatterns = {
    url('(?P<ifsc>[A-Za-z]{4}\w{7})/$', bank_detail_view),
    url('(?P<city>.*)/(?P<bank>.*)/$', banks_list_view)
}

urlpatterns = format_suffix_patterns(urlpatterns)