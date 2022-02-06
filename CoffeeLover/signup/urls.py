from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("signup", views.signup, name="signup"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("login", views.login, name='login')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)