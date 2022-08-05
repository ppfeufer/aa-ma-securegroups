# Django
from django.urls import include, re_path

# Alliance Auth
from allianceauth import urls

# Alliance auth urls
urlpatterns = [
    re_path(r"", include(urls)),
]
