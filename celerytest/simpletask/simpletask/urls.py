from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from simpletask import settings

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('sendmessage/', include('sendmessage.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
