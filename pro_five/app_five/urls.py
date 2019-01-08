from django.conf.urls import url
from app_five import views

app_name = 'app_five'

urlpatterns = [
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name='user_login'),

]
