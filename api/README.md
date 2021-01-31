

# package notes
- Flask: The flask framwork
- Flask-RESTful: Used to build RESTful api
- Flask-SQLAlchemy: An ORM framwork
- Flask-Script: Used to manage flask project
- Flask-Migrate: Used to manage database
- python-dotenv: Used to manage `.env` file
- uwsgi: The product server

# run uwsgi

```sh
$ uwsgi --ini uwsgi.ini
```
> Note: You will change uwsgi.ini like this:
> uncomment `http=0.0.0.0:80` and comment `socket = myproject.sock` when you don't use nginx
> comment `http=0.0.0.0:80` and uncomment `socket = myproject.sock` when you use nginx
> 

# build docker image
docker build -t sophia-api:0.0.1 .