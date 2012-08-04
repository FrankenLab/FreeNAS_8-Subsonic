from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/subsonic/', include('subsonicUI.freenas.urls')),
)
