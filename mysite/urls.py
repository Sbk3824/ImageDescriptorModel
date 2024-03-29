from django.contrib import admin
from django.urls import path, include
from jet_django.urls import jet_urls

from mysite.core import views

from mysite import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/', views.test, name='test'),
    path('analysis/', views.analysis.as_view(), name='analysis'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('faq/',views.faq, name='faq'),
    path('admin/', admin.site.urls),
    path('jet_api/', include(jet_urls)),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
