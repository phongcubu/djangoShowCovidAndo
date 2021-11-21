from django.shortcuts import render
import json
from urllib.request import urlopen

def home(request):
    url = 'https://data.covid19india.org/data.json'
    res = urlopen(url)
    data = json.loads(res.read())
    labels=[]
    chartdata=[]
    for state in data['statewise']:
        labels.append(state['state'])
        chartdata.append(state['deaths'])
    return render(request, 'home.html', {'data':data,'labels':labels,'chartdata':chartdata})




