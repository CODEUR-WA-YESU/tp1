from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib



# Create your views here.
def index(request):
    donnees = {
        'etudiant1':{
            'nom' : 'Bienfait',
            'postNom' : 'Luvako',
            'sexe':'masculin'
        },
        'etudiant2':{
            'nom' : 'Jacob',
            'postNom' : 'Motana',
            'sexe':'masculin'
        }
    }

    template=loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))



def voix(request):
    template=loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def predire(request):
    #template=loader.get_template('predire.html')
    if request.method=='POST':
        partiPolitique=int(request.POST['partiPolitique'])
        casierJudicaire=int(request.POST['casierJudicaire'])
        nbrePopulation=int(request.POST['nbrePopulation'])
        ancienetePolitique=int(request.POST['ancienetePolitique'])

        tableau=[[partiPolitique,casierJudicaire,nbrePopulation,ancienetePolitique]]
        regresseur=joblib.load('./modele_ml/mesanomod.pkl')

        return HttpResponse(regresseur.predict(tableau))
    print("ok")

