# Bunshi

Description

## Run locally

Clone
```
$ git clone "https://github.com/hvrc/Bunshi.git"
$ cd Bunshi
```

Create a virtualenv & activate it
```
$ python3 -m venv venv
$ . venv/bin/activate
```
...on Windows cmd
```
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

Install requirements
```
$ pip install -r requirements.txt
```

Run
```
$ export FLASK_APP=bunshi
$ export FLASK_ENV=development
$ flask run
```

... on Windows cmd
```
> set FLASK_APP=bunshi
> set FLASK_ENV=development
> flask run
```

Open [localhost:5000](http://127.0.0.1:5000) in a browser
