# TTprogress
back-end for TTprogress site

run project:

create virtualvenv -> 
	python3 -m venv venv

 
activate virtualvenv ->
	mac: source venv/bin/activate


 install requirements -> 
 	pip install -r requirements.txt
  

migrations -> 
	python3 manage.py migration


createAdmin -> 
	python3 manage.py createsuperuser


 collectstatic -> 
 	python3 manage.py collectstatic


  runserver -> 
  	python3 manage.py runserver
