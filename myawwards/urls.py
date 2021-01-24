from django.conf.urls import url
from . import views
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^register/', views.registerPage, name="register"),
    url(r'^login/', views.loginPage, name="login"),
    url(r'^logout/', views.logoutUser, name="logout"),
    url(r'^profile/', views.profile, name='profile'),

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    