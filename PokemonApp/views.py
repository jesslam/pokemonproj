from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonType, Evaluation, Review
from .forms import EvaluationForm, ReviewForm
from django.contrib.auth.decorators import login_required

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

#Create forms
@login_required
def newEvaluation(request):
    form=EvaluationForm
    if request.method=='POST':
        form=EvaluationForm(request.POST)
        if form.is_valid():
            posted=form.save(commit=True)
            posted.save()
            form=EvaluationForm()
    else:
        form=EvaluationForm() 
    return render(request, 'PokemonApp/neweval.html', {'form': form})   

@login_required
def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            posted=form.save(commit=True)
            posted.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'PokemonApp/newreview.html', {'form': form})

def loginMessage(request):
    return render(request, 'PokemonApp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'PokemonApp/logoutmessage.html')
