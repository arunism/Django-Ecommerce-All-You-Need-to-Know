##### How to run the program?

To run the program first download the zip file of this repository and unzip it or clone this repository using the command: install all the required dependencies and libraries by using the command:

    * git clone https://github.com/arunism/Django-Ecommerce-All-You-Need-to-Know

Now install all the required dependencies and libraries by using the command:

    * pip install requirements.txt
    * OR
    * pip3 install requirements.txt

Now run the migrations and fit the migrations to the database using the commands:

    * python manage.py makemigrations
    * python manage.py migrate
    * OR
    * python3 manage.py makemigrations
    * python3 manage.py migrate

Finally lunch the server using the below command:

    * python manage.py runserver
    * OR
    * python3 manage.py runserver

Now run the following address in the browser:

    * http://127.0.0.1:8000/

To check the admin interface, you first need to create an admin user:

    * django-admin createsuperuser

Provide all the required crediantials and leave the other fields blank.
After the admin superuser is created you can access the admin panel by hitting the following route in the browser:

    * http://127.0.0.1:8000/admin/
