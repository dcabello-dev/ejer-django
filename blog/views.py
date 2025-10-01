
from django.shortcuts import render
"""
# Create your views here.
def ejer1(request):
    resultado = ''
    if request.method == 'POST':
        texto = request.POST.get('texto', '')
        resultado= texto.upper()

    return render(request, 'ejer1.html', {'resultado': resultado})
"""
def ejercicios(request):
    resultado1 = None
    resultado2 = None

    if request.method == 'POST':
        # Verificar qué ejercicio se envió
        if 'ejercicio1' in request.POST:
            texto = request.POST.get('texto', '')
            resultado1 = texto.upper()
        elif 'ejercicio2' in request.POST:
            texto = request.POST.get('texto2', '')
            # Contar palabras: split por espacios y contar
            palabras = texto.split()
            resultado2 = f"El texto tiene {len(palabras)} palabras."

    return render(request, 'ejer1b.html', {
        'resultado1': resultado1,
        'resultado2': resultado2
    })
