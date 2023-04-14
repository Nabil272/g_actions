# Utilisez l'image officielle de Python 3.9
FROM python:3.9

# Définissez le répertoire de travail à /app
WORKDIR /app

# Copiez les fichiers de votre projet dans le conteneur
COPY . /app

# Installez les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Définissez la commande par défaut pour exécuter votre application
CMD ["python", "dump_to_s3.py"]
