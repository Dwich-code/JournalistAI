import os
import requests
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk

load_dotenv()  # Charger le contenu du fichier .env

API_KEY = os.getenv("API_KEY") # API KEY
BASE_URL = 'https://newsapi.org/v2/top-headlines' # URL

# Paramètres pour la requête
params = {
    
    'apiKey': API_KEY  # API Key
}

# Faire une requête GET
response = requests.get(BASE_URL, params=params)

if response:
    data = response.json()
    articles = data.get('articles', [])
    number = 0
    
    # Récupérer uniquement les titres et descriptions
    with open('articles.txt', 'w', encoding='utf-8') as file:
        for idx, article in enumerate(articles):
            title = article.get('title', 'Title not found')
            author = article.get('author', 'author not found')
            description = article.get('description', 'Description not found')
            publishedAt = article.get('publishedAt', 'publishedAt not found')
            url = article.get('url', 'url not found')
            file.write(f"{idx + 1}. Titre: {title}\n")
            number = number + 1
            file.write(f"   Author: {author}\n")
            file.write(f"   Description: {description}\n")
            file.write(f"   Published at: {publishedAt}\n")
            file.write(f"   Url: {url}\n\n")
    
    print(f"{number} articles found")
    
else:
    print(f"Error{response.status_code}")