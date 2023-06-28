from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import send_mail

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            send_mail(
                "Mensaje desde App Django",
                "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
                "",
                ["vmarialuzm@gmail.com"],
                fail_silently=False,
            )

            return redirect("/contacto/?valido")

    return render(request,'contacto/contacto.html',{"miFormulario":formulario_contacto})
