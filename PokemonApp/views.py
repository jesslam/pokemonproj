from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonType, Evaluation, Review

# Create your views here.
def index(request):
    return render(request, 'PokemonApp/index.html')

def getpokemon(request):
    pokemon_list=Pokemon.objects.all()
    return render(request, 'PokemonApp/pokemon.html', {'pokemon_list': pokemon_list})

def pokemondetail(request, id):
    pokemonname=get_object_or_404(Pokemon, pk=id)
    reviewcount=Review.objects.filter(pokemonname=id).count
    reviews=Review.objects.filter(pokemonname=id)
    context= {
        'pokemonname': pokemonname,
        'reviewcount': reviewcount,
        'reviews': reviews
    }
    return render(request, 'PokemonApp/pokemondetail.html', context=context)
    

def getevaluation(request):
    evaluation_list=Evaluation.objects.all()
    return render(request, 'PokemonApp/evaluation.html', {'evaluation_list': evaluation_list})

