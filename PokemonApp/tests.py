from django.test import TestCase
from .models import Pokemon, PokemonType, Review, Evaluation
from .views import index, getpokemon, pokemondetail, getevaluation
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import EvaluationForm

# Create your tests here.

class PokemonTest(TestCase):
    def setUp(self):
        name=Pokemon(pokemonname="Pikachu", pokemonbase="Pikachu", cp=416, hp=65, level=18.0)
        return name

    def test_string(self):
        monname=self.setUp()
        self.assertEqual(str(monname), monname.pokemonname)

    def test_table(self):
        self.assertEqual(str(Pokemon._meta.db_table), 'pokemon')

class PokemonTypeTest(TestCase):
    def setUp(self):
        type=PokemonType(pokemontype="Pikachu Mouse Pokemon [Flower Crown]")
        self.assertEqual(str(type), type.pokemontype)

class IVEvalTest(TestCase):
    def setUp(self):
        evalu=Evaluation(IVpercent=40, IVname="Adequate")
        return evalu

    def test_string(self):
        name=self.setUp()
        self.assertEqual(str(name), (name.IVname + " " + str(name.IVpercent) + "%"))

#Tests for Views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class PokemonURLTest(TestCase):  
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('pokemon'))
        self.assertEqual(response.status_code, 200)

class GetPokemonTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='Ron')
        self.type=PokemonType.objects.create(pokemontype='Leafeon Verdant Pokemon', 
            typedescription='It gets its nutrition from photosynthesis.  It lives a quiet life deep in forests where clean rivers flow.')
        self.newmon=Pokemon.objects.create(pokemonname='Leafeon', pokemonbase='Eevee', pokemontype=self.type, user=self.u, cp=1915, hp=112, level=23.0)
        
        self.rev1=Review.objects.create(reviewtitle='Special lure, special grass-type Eevolution', reviewdate='2019-06-01', pokemonname=self.newmon, 
            reviewtext='Leafeon is a newly released Eevee evolution available near grass lures only and is quite a pretty addition.')
        self.rev1.user.add(self.u)
        self.rev2=Review.objects.create(reviewtitle='Leafeon, cute but not useful (yet)', reviewdate='2019-06-10', pokemonname=self.newmon, 
            reviewtext='Not yet a recommended opponent for current raids, Leafeon may still be an inferior attacker to its Vaporeon and Jolteon siblings.')
        self.rev2.user.add(self.u)

    def test_pokemon_detail_success(self):
        response=self.client.get(reverse('pokemondetail', args=(self.type.id,)))
        self.assertEqual(response.status_code, 200)

    def test_number_of_reviews(self):
        reviews=Review.objects.filter(pokemonname=self.newmon).count()
        self.assertEqual(reviews, 2)

class New_Evaluation_Test(TestCase):
    def setUp(self):
        self.type=PokemonType.objects.create(pokemontype='Leafeon Verdant Pokemon', typedescription='It gets its nutrition from photosynthesis.  It lives a quiet life deep in forests where clean rivers flow.')
        self.user=User.objects.create(username='Donna')
        self.newmon=Pokemon.objects.create(pokemonname='Leafeon', pokemonbase='Eevee', pokemontype=self.type, user=self.user, cp=1915, hp=112, level=23.0)


    def test_evalForm(self):
        data={
            'pokemonname' : self.newmon,
            'attacknum' : 14,
            'defensenum' : 13,
            'staminanum' : 13,
            'IVpercent' : 92,
            'IVname' : 'Excellent',
            
        }
        form=EvaluationForm(data=data)
        self.assertTrue(form.is_valid)

