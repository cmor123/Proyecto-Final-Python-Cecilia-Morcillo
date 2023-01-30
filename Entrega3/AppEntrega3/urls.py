
from AppEntrega3 import views
 
from django.urls import path

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('destinos', views.destinos, name="Destinos"),
    path('hospedaje', views.hospedaje, name="Hospedaje"),
    path('alquiler_coches', views.alquiler_coches, name="Alquiler_Coches"),
    path('opiniones_viajeros', views.opiniones_viajeros, name='Opiniones_Viajeros'),
    path('opiniones/list', views.OpinionesList.as_view(), name = 'List'),
    path(r'^nuevo$', views.OpinionesCreacion.as_view(), name='New'),
    path(r'^(?P<pk>\d+)$',views.OpinionesDetalle.as_view(), name= "Detail"),
    path(r'^editar/(?P<pk>\d+)$', views.OpinionesUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.OpinionesDelete.as_view(), name ='Delete'),
    path('busquedaCiudad', views.busquedaCiudad, name="BusquedaCiudad"),
    path('buscar/', views.buscar),
    path('leerDestinos', views.leerDestinos, name='leerDestinos'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppEntrega3/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 

 ]
