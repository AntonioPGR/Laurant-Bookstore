from django.shortcuts import render


def loja(request):
  data = {
    1: {
      "titulo": "Mil beijos de garoto",
      "autor": "Tillie Cole",
      "preco": "50,00"
    },
    2: {
      "titulo": "Acotar: corte de névoa e fúria",
      "autor": "Sarah J. Maas",
      "preco": "49,90"
    }
  }
    
  return render(request, 'livros/marketplace.html', {"cards": data})


def livro(request):
  return render(request, 'livros/book.html')
