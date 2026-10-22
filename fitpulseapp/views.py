from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'fitpulseapp/listar_clientes.html', {'clientes': clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'fitpulseapp/agregar_cliente.html', {'form': form})


def editar_cliente(request, rut):
    cliente = get_object_or_404(Cliente, pk=rut)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'fitpulseapp/agregar_cliente.html', {'form': form})


def eliminar_cliente(request, rut):
    cliente = get_object_or_404(Cliente, pk=rut)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'fitpulseapp/confirmar_eliminar.html', {'cliente': cliente})