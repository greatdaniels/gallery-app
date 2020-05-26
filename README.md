# gallery-app

## Author

[Dan_Njoroge](https://github.com/greatdaniels)

# Description
A personal gallery application that displays my photos for others to view.

## User Story

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

### Cloning
* In your terminal:
        
        $ git clone https://github.com/greatdaniels/gallery-app.git
        $ cd gallery-app

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations grid
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests :

        $ python3.6 manage.py test 


## Technology used

* [Python3.6](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)


## Known Bugs
* Pull requests are allowed incase you spot a bug.

## License
[MIT LICENSE](./license)