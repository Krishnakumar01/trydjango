from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'trydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include('leaderboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
]