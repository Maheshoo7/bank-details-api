# bank-details-api

1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

The api is built using django-rest-framework

## Installation

* clone the repository
* create virtualenv

```

$ pip install -r requirements.txt
$ python manage.py runserver

```

open below links
* Find by IFSC 
* http://127.0.0.1:8000/api/<ifsc code>
* eg: http://127.0.0.1:8000/api/KARB0000091/


* Find by city and bank name:
* http://127.0.0.1:8000/api/<city>/<bank name >
* eg: http://127.0.0.1:8000/api/bangalore/canara/

## Heroku links
#### Find by IFSC
- https://bank-ifsc-api.herokuapp.com/api/UTIB0001145/
- https://bank-ifsc-api.herokuapp.com/api/SYNB0000864/
- https://bank-ifsc-api.herokuapp.com/api/UBIN0572837/


#### Find by city and bank name:
* https://bank-ifsc-api.herokuapp.com/api/bangalore/yes/
* https://bank-ifsc-api.herokuapp.com/api/bangalore/hdfc/
* https://bank-ifsc-api.herokuapp.com/api/delhi/hdfc/

I have uploaded around 40,000 indian bank details, so you might not find every bank.

