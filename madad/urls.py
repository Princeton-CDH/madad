"""
URL configuration for madad project.
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

]

# urls that should be available in multiple languages
urlpatterns += i18n_patterns(
    path("", include("geniza.common.urls", namespace="common")),
    path("", include("geniza.corpus.urls", namespace="corpus")),
)
