from django.conf.urls import include, url
from django.contrib import admin

import blog.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^user/', include('blog.urls', namespace="users")),

]
