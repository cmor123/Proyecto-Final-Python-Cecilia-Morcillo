# Create your views here.
from django.shortcuts import render, HttpResponse 
from django.http import HttpResponse
from AppEntrega3.models import Hospedaje, Destino, Alquiler_Coches, Avatar, Opiniones_Viajeros
from AppEntrega3.forms import HospedajeFormulario, Alquiler_CochesFormulario, Opiniones_ViajerosFormulario, UserEditForm, UserRegisterForm, DestinoFormulario


          # Create your views here.

def iniciar(request):
      return render(
            request = request,
            template_name='AppEntrega3/bienvenido.html',
      )

def destinos(request):
      destino = destino(pais="Argentina", ciudad="Santa Fe")
      destino.save()
      documentoDeTexto = f"--->Pais: {destino.pais}   Ciudad: {destino.ciudad}"
      

      return HttpResponse(documentoDeTexto)

def hospedajes(request):

      hospedaje = hospedaje(Hoteles="Hoteles", Zona="Centro", Personas=" 4 adultos" )
      hospedaje.save()
      documentoDeTexto = f"--->Hoteles: {hospedaje.Hoteles}   Zona: {hospedaje.Zona} Personas: {hospedaje.Personas}"

      return HttpResponse(documentoDeTexto)

def alquiler_coches(request):

      alquiler_coches = alquiler_coches(Alta_Gama="Toyota Corolla", Media_Gama="Siena", Compacto="Fiat up" )
      alquiler_coches.save()
      documentoDeTexto = f"--->Alta_Gama: {alquiler_coches.Alta_Gama}   Meia_Gama: {alquiler_coches.Media_Gama} Compacto: {alquiler_coches.Compacto}"

      return HttpResponse(documentoDeTexto)

def opiniones_viajeros(request):
      opiniones_viajeros = opiniones_viajeros(Nombre ="Juan", Nacionalidad = "Peru", Opiniones="Estuvo todo Excelente")
      opiniones_viajeros.save()
      documentoDeTexto = f"--->Nombre: {opiniones_viajeros.Nombre}   Nacionalidad: {opiniones_viajeros.Nacionalidad} Opiniones: {opiniones_viajeros.Opiniones}"
      return HttpResponse(documentoDeTexto)


def inicio(request): 

      return render(request, "AppEntrega3/inicio.html")

def destino(request):

      return render(request, "AppEntrega3/destino.html")

def hospedaje(request):

      return render(request, "AppEntrega3/hospedaje.html")


def alquiler_coches(request):

      return render(request, "AppEntrega3/alquiler_coches.html")

def opiniones_viajeros(request):
     
      return render(request,"AppEntrega3/opiniones_viajeros.html")


def destinos(request):

      if request.method == "POST":

            miFormulario = DestinoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)


            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  destino = Destino (pais=informacion["pais"], ciudad=informacion["ciudad"])
                  destino.save()
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = DestinoFormulario()
            
      return render(request, "AppEntrega3/destino.html", {"miFormulario": miFormulario})

def hospedaje(request):

      if request.method == "POST":

            miFormulario = HospedajeFormulario(request.POST) # Aqui me llega la informacion del html
            
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                 
                  hospedaje = Hospedaje(Tipo_Hospedaje=informacion["Tipo_Hospedaje"], Zona=informacion["Zona"], Cantidad_Personas=informacion["Cantidad_Personas"] )
                 
                  hospedaje.save()
                 
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = HospedajeFormulario()

      return render(request, "AppEntrega3/hospedaje.html", {"miFormulario": miFormulario})

def alquiler_coches(request):

      if request.method == "POST":

            miFormulario = Alquiler_CochesFormulario(request.POST) # Aqui me llega la informacion del html
            
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                 
                  alquiler_coches = Alquiler_Coches(Alta_Gama=informacion["Alta_Gama"], Media_Gama=informacion["Media_Gama"], Compacto=informacion["Compacto"])
                 
                  alquiler_coches.save()
                 
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = Alquiler_CochesFormulario()

      return render(request, "AppEntrega3/alquiler_coches.html", {"miFormulario": miFormulario})

def opiniones_viajeros(request):

      if request.method == "POST":

            miFormulario = Opiniones_ViajerosFormulario(request.POST) # Aqui me llega la informacion del html
            
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                 
                  opiniones_viajeros = Opiniones_Viajeros(Nombre=informacion["Nombre"], Nacionalidad=informacion["Nacionalidad"], Opiniones=informacion["Opiniones"])
                 
                  opiniones_viajeros.save()
                 
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = Opiniones_ViajerosFormulario()

      return render(request, "AppEntrega3/opiniones_viajeros.html", {"miFormulario": miFormulario})



def busquedaCiudad(request):
      return render(request, "AppEntrega3/busquedaCiudad.html")

def buscar(request):
     
      respuesta = f"Estoy buscando la Ciudad: {request.GET['ciudad']}"

      #No olvidar from django.http import HttpResponsereturn HttpResponse(respuesta)
      
      return HttpResponse(respuesta)

def leerDestinos(request):
      destinos = Destino.objects.all() #trae todos
      contexto= {"destinos":destinos}
      return render(request, "AppEntrega3/leerDestinos.html",contexto)

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse

class OpinionesList(ListView):
      model = Opiniones_Viajeros
      template_name = "AppEntrega3/opiniones_list.html"

class OpinionesDetalle(DetailView):
      model= Opiniones_Viajeros
      template_name = "AppEntrega3/opiniones_detalle.html"

class OpinionesCreacion(CreateView):
      model= Opiniones_Viajeros
      success_url= "/AppEntrega3/opiniones/list"
      fields = ['Nombre', 'Nacionalidad', 'Opiniones']

class OpinionesUpdate(UpdateView):
      model= Opiniones_Viajeros
      fields = ['Nombre', 'Nacionalidad', 'Opiniones']
      def get_success_url(self):
            return reverse('List')

class OpinionesDelete(DeleteView):
      model = Opiniones_Viajeros
      success_url= "/AppEntrega3/opiniones/list"




#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
      
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                             
                return render(request, "AppEntrega3/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppEntrega3/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppEntrega3/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppEntrega3/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppEntrega3/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            #form = UserRegisterForm()     

      return render(request,"AppEntrega3/registro.html" ,  {"form":form})


def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppEntrega3/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppEntrega3/registro.html" ,  {"form":form})




from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "AppEntrega3/inicio.html")


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppEntrega3/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppEntrega3/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
