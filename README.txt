Questo è il progetto di Applicazioni Data Intensive di Cichetti Federico e Sponziello Nicolò.
Si tratta della risoluzione di una competition originariamente presentata su kaggle ( https://www.kaggle.com/c/whats-cooking/ )
La cartella contiene:
- Progetto.ipynb: il notebook jupyter contenente il progetto e la relazione
- test.json e train.json: i due file forniti con la competition: il primo contiene il training set (poi scomposto in training e validation all'interno del notebook) e il secondo è il test set da inviare su kaggle per ottenere la valutazione.
- what's_cooking_website: una cartella contenente il sito web sviluppato con Flask. Il sito web utilizza modelli costruiti nel notebook jupyter salvati nella cartella "models". Per avviarlo si possono utilizzare i due launcher presenti nella cartella stessa o lanciare i seguenti comandi da terminale:

su Windows:
set FLASK_APP=flask_web
set FLASK_DEBUG=true
python -m flask run

su Linux:
export FLASK_APP=flask_web.py
export FLASK_ENV=development
flask run
