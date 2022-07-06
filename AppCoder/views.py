from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre = "Python", camada = "31090")
    curso.save()
    documentoDeTexto = f"----> Curso:    {curso.nombre} <br> Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)