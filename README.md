**Clone repository:**
```
  $ git clone https://github.com/gabrielastrezea/MedicalApp.git
```

**Install virtualenv:**
```
  $ pip install virtualenv
```

**Create virtual environment:** 
```
  $ cd MedicalApp 
  $ virtualenv sandbox
```

**Activate environment:**
```
  $ source sandbox/bin/activate
```

**Install Django:**
```
  $ pip install Django
```

**Apply migrations:**
```
  $ ./manage.py migrate
```

**Load data into app:**
```
  $ ./manage.py loaddata users.json
  $ ./manage.py loaddata doctors.json
  $ ./manage.py loaddata patients.json
  $ ./manage.py loaddata medicine.json
```

**Run development server:** 
```
  $ ./manage.py runserver
```

**Access project on:**
```
  http://127.0.0.1:8000/
```

**Link-uri disponibile:**
  * /admin -> dashbord-ul de administrare al Django
  * /medicines -> lista de medicamente
  * /patients -> lista de pacienti
  * /doctors -> lista de doctori
  * /add_medicine -> adauga un medicament
  * /edit_medicine/<id_medicine> -> editeaza un medicament
  
Ai si login. Poti sa te logezi cu oricare dintre utilizatorii din json-ul users.json. Toti au parola *parola1234*
Login-ul te redirecteaza momentan la lista de medicamente si poti face logout doar din dashboard.

