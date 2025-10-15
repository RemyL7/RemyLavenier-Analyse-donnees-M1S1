#Dockerfile
#Par défaut, ce fichier installe la dernière version de Python. Pour changer de version, remplacer le numéro de version et sa mineure, comme 3.6, 3.7, 3.8, 3.9, 3.10, 3.11 ou 3.12, ou encore par latest pour avoir la dernière version. Toutefois, certains paquets ne fonctionnement pas sur une version supérieure à celle retenue.
FROM python:3.6

# create app directory and set it as working dir
RUN mkdir /application
WORKDIR /application

# Upgrade pip
RUN pip install --upgrade pip

# Update apt lists and clean cache
RUN apt-get update && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*


# Copy requirements and install
COPY requirements.txt /application/
RUN pip install -r /application/requirements.txt

# Copy application source into the image
COPY src/ /application/

# Default command
CMD [ "python", "main.py" ]
