from django.shortcuts import render


def loja(request):
    return render(request, 'livros/marketplace.html')


def livro(request):
    return render(request, 'livros/book.html')
