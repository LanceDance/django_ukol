# Django ukol pro Whys

Zadani a endpointy:

[POST] `/import` - tento endpoint bude příjímat data a parsovat data
[GET] `/detail/<nazev modelu>/` - seznam záznamů na základě názvu modelu
[GET] `/detail/<nazev modelu>/<id>` - všechna data ke konkrétnímu záznamu

Na zaklade zadani jsem vytvoril endpointy, POST import bere cely json a parsuje jej do danych modelu

`/detail/<nazev modelu>/` ukazuje vsechna data v modelu (DB)

`/detail/<nazev modelu>/<id>` na zaklade modelu a daneho id ukaze vsechna data o zaznamu

Ze zadani mi vyplynulo, ze foreign klice u modelu nejsou jasne dana. Tudiz jsem s nimi nepracoval.

Spusteni:
vsechny balicky jsou v requirements.txt
* `cd django_ukol`
* `cd whys_project`
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`

Endpointy by mely vypadat nejak takto:

POST - `http://127.0.0.1:8000/ukol/import/`

GET model - `http://127.0.0.1:8000/ukol/detail/<model>`

GET detail zaznamu - `http://127.0.0.1:8000/ukol/detail/<model>/<id>`

TODO: 
* Swagger pro lepsi dokumentaci endpointu
* Unit testy
