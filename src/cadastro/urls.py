
from django.urls import path, include

from .views import login_view, logout_view, pagina_cadastro_view

app_name = 'cadastro'


urlpatterns = [

    path('cadastro/', pagina_cadastro_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

]


