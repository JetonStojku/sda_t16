# sda_t16
hollymovies

## Adding Python to the Windows PATH
is a way to make Python accessible from the command prompt, so you can run Python scripts and programs without typing the full path to the Python executable. To add Python to the Windows PATH, you need to follow these steps:

- Locate the directory where your Python executable is installed. It is usually in a folder like `C:\Python27` or `C:\Users\<USER>\AppData\Local\Programs\Python`, where `<USER>` is your user name. You can also use a tool like [Everything](^1^) to search for `python.exe` on your system.
  - Open the System Properties window by pressing `Win + Pause` or typing `System Properties` in the Start menu.
  - Switch to the Advanced tab and click Environment Variables.
  - Under the System variables section, select the Path variable and click Edit.
  - Click the New button and paste the full path to your Python folder in the text box that appears. Make sure there are no spaces before or after the path, and that it is separated from other paths by a semicolon (`;`).
  - Click OK to save the changes and close all the windows.
  - Restart the command prompt and test if Python is working by typing `python --version`. You should see the version of Python that you have installed.


#### Python virtual environment 
- Create a virtual environment
    `python -m venv venv`
- Activate the virtual environment by running the command on Windows
    `venv\Scripts\activate`
or
    `source venv/bin/activate`
on Linux or Mac. You should see a (venv) prefix in your command prompt, indicating that you are in the virtual environment.

#### Django

- The first thing to get started with Django is to prepare your local environment by installing Django.

    `pip install django==4.2`

- Install all requirements
    
    `pip install -r requirements.txt`

- Generate a Django directory tree for our project:
    
    `django-admin startproject hollymovies .`

- To start the application server, run the command:
    
    `python manage.py runserver`

- add application:

    `python manage.py startapp viewer`

- create migration file:

    `python manage.py makemigrations`

- create tables in DB:

    `python manage.py migrate`


##### SHELL

  `python manage.py shell`
  
Play with shell:

- from viewer.models import Genre
- Genre.objects.all()
- Genre.objects.create(name='Horror')
- genre = Genre(name='Thriller') genre.save()
- Genre.objects.all()
- horror = Genre.objects.get(name='Horror')
- horror.name
- horror.id


Administrator:

`python manage.py createsuperuser`

Export data:

`python manage.py dumpdata viewer --output fixtures.json`

import data:

`python manage.pyloaddata fixtures.json`


##### ORM
```python
Movie.objects.filter(rating=8)
horror = Genre.objects.get(name='Horror')
Movie.objects.filter(genre=horror)
Movie.objects.filter(genre__name='Horror')
Movie.objects.filter(rating__gt=8)
Movie.objects.filter(title__contains='Godfather') 
Movie.objects.filter(title__icontains='godfather').filter(released__year__gt=1973)
Movie.objects.filter(title='Avatar').exists()
Movie.objects.filter(title__contains=’Godfather’).order_by('released')
Movie.objects.filter(title__contains=’Godfather’).order_by('-released')
Genre.objects.create(name='Documentary')# no access to the object before write
genre =Genre(name='Comedy')
genre.save()
Movie.objects.filter(released__year=2000).update(rating=5)# sets movie ratings from year 2000 to 5
pulp_fiction = Movie.objects.get(title='Pulp Fiction')
pulp_fiction.rating =7
pulp_fiction.save()
Movie.objects.filter(title__contains='Godfather').delete()
```