# Coffee-API

coffee-api is an ecommerce API to clients that have two screens: one screen to display coffee machines and one screen to display coffee pods. On the coffee
machines screen, the user may filter by product type and water line. On the coffee pods screen, the user may filter by product
type, coffee flavor, and pack size.

  - the code is ***tested*** using pytest, mockmongo
  - the code uses flake8 ***linter*** and autopep8 ***formatter***
  - dependencies:   
    * flask
    * flask-mongoengine
  

# Features!

  -Two endpoints to filter products: 
  - for **coffee machine** : ```/coffee/machine/filter```
  -  for **coffee pods** : ```/coffee/pod/filter```
  


#### for example:
"let's assume that mongodb is already populated by some data like in the pdf sent
also there is a script in this repo for importing that data under the name of *insert_docs.py* in the app directory"

filtering works by hitting the endpoing with a *POST* request with JSON body formatted like this ```
{<product attribute>: <value to be filtered with>}```
note: you can add more attributes and more values
so hitting ```/coffee/machine/filter``` with *POST* request body ```{"product_type":"COFFEE_MACHINE_LARGE"}```
would return the list  ```
[
    "CM101",
    "CM102",
    "CM103"
]```


if you used a non valid attribute you would recieve a JSON response with status code *404*:
```{'message': 'use a valid property name'}```
