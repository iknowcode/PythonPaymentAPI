import requests
#Please change the date to the current date to get the response

#Expensive Payment Gateway has a probability of 30% so expect to get 400 as a response
r1 = requests.post('http://127.0.0.1:5000/', json={ "CreditCardNumber":987654321,
    "CardHolder":"Xyzname",
    "ExpirationDate":"2021-01-21",
    "SecurityCode":900,
    "Amount":5000.00}) #Amount -> Float and grater than 500

r2 = requests.post('http://127.0.0.1:5000/', json={ "CreditCardNumber":987654321,
    "CardHolder":"Xyzname",
    "ExpirationDate":"2021-01-21",
    "SecurityCode":900,
    "Amount":500.00})# Amount is 500


r3 = requests.post('http://127.0.0.1:5000/', json={ "CreditCardNumber":987654321,
    "CardHolder":"Xyzname",
    "ExpirationDate":"2021-01-21",
    "SecurityCode":900,
    "Amount":15.00})# Amount is less than 20

r4 = requests.post('http://127.0.0.1:5000/', json={ "CreditCardNumber":987654321,
    "CardHolder":"Xyzname",
    "ExpirationDate":"2021-01-21",
    "SecurityCode":900,
    "Amount":-300})#Amount is -ve

r5 = requests.post('http://127.0.0.1:5000/', json={ "CreditCardNumber":987654321,
    "CardHolder":"Xyzname",
    "ExpirationDate":"2021-01-21",
    "SecurityCode":900,
    "Amount":60.00}) # Amount 50 


print(r1.status_code,r2.status_code,r3.status_code,r4.status_code,r5.status_code)
