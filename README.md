# Jina Flask API

## 1. Create your venv

Make sure you already have Virtualenv installed:

    $ pip install virtualenv

Create a new venv inside the project folder:

    $ virtualenv venv

You ll see a venv folder added to the project.

## 3. Activate the venv

- If you are using Windows, run:

  $ `.\venv\Scripts\activate`

You ll notice a `(venv)` in the beginning of the command prompt.

## 2. Install dependencies

Very simple, just run the following command:

    $ pip install -r requirements.txt

## 4. Run the app

Run the command:

    $ python main.py

## 5. Test the app

### GET

- `/template/`
- `/template/api/<semester>`: this will return variable you used in the path

### POST

- `/template/api/inbody`: add to the body

  {
  "semester": 15248
  }

this will return the number you put in the semester field.
