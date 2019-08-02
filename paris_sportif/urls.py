from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name='first_bet'
urlpatterns = [
   path('',index , name='index'),
   path('creat/', post, name='creat'),
   path('bet_views/',my_bet , name='mon_pari'),
   path('creat/login/',auth , name='login'),
   path('result/',scores, name='result'),
   path('bet_now/', retrait_post, name='retrait'),
path('creat/login/account/', connecting, name='my_count'),
path('creat/login/account/logout', logout_views, name='logout'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)