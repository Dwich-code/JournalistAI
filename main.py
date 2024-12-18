import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Charger le contenu du fichier .env

# Votre clé API
API_KEY = os.getenv("API_KEY")

# URL de base de l'API
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Paramètres pour la requête
params = {
    'country': 'fr',  # Pays (ici France)
    'launguage': 'fr',
    'category': 'technology',  # Catégorie (ex. technology, business, etc.)
    'apiKey': API_KEY  # Votre clé API
}

# Faire une requête GET
response = requests.get(BASE_URL, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Décoder le JSON de la réponse
    data = response.json()
    articles = data.get('articles', [])
    
    # Afficher les titres des articles
    for idx, article in enumerate(articles):
        print(f"{idx + 1}. {article['title']}")
else:
    # Gérer les erreurs
    print(f"Erreur: {response.status_code}")
    print(response.text)
