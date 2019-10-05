


W panelu admina ja dałem dokument pdf i to jak został podzielony na części. 
I to jak wygląda pdf w postaci strony HTML do edycji.

No jak odczytasz pdf i wiesz z jakich część się składa 
to zapisujesz to sobie do bazy.

Mam formularz na stronie, robię upload pdf, przetwarzan pdf 
i w wyniku mam że w środku jest tekst na górze i zdjęcie na dole, więc zapisuję do bazy to info,
 a potem tworzę na tej podstawie widok z jakaś analizą typu znaleziono tekst X i zdjęcie Y



# PDF Splitter
Simple Flask app. Display output from PDFMiner.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
* Load PDF document
* Split it with PDFMiner
* Save to database
* Display splitted PDF content.

## Technologies
Project is created with:
* flask
* flask-sqlalchemy
* flask-admin
* pdfminer

## Setup
```
pip3 install -r requirements.txt
python app.py
```

Tests:
 ```
python test.py
```
