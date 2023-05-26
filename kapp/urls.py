from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.indexPage),
    path('index/',views.indexPage),
    path('getintouch/',views.contactPage),
    path('website/',views.websitePage),
    path('about/',views.aboutPage),
    path('digital/', views.DigitalPage),
    path('software/', views.SoftwarePage),
    path('client/',views.ClientPage),
    path('savedata/',views.SaveData,name="savedata")
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
