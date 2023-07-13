from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests

headers = {
        "Ocp-Apim-Subscription-Key" : "552c83439c874e4c9a5c735c57cd8edc"
    }


def home(request):
     return render(request,'home.html')
def get_website_data(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=159ff78131704ec8846ad9f5237c8834')
    response = requests.get(url)
    data = response.json()
    articles = data['articles'][:3]  # Select the first 3 articles from the data
    return render(request, 'template.html', {'country': 'US','articles': articles})

def get_website_data_country(request):
        country = request.GET.get('country', 'us')  # Default value is 'us'
        api_key = '159ff78131704ec8846ad9f5237c8834'
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles'][:3]  # Select the first 3 articles from the data
        return render(request, 'template.html', {'country': country, 'articles': articles})

def category(request):
        category = request.GET.get('category', 'general')  # Default value is 'us'
        api_key = '159ff78131704ec8846ad9f5237c8834'
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles'][:3]  # Select the first 3 articles from the data
        return render(request, 'category.html', {'country': category, 'articles': articles})

def source(request):
        source = request.GET.get('source', 'bbc-news')  # Default value is 'us'
        api_key = '159ff78131704ec8846ad9f5237c8834'
        url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles'][:3]  # Select the first 3 articles from the data
        return render(request, 'sources.html', {'source': source, 'articles': articles})
