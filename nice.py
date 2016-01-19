from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
DISS = ['poo','a son of a motherless goat', 'a dontomo', 'a Pull me backwards into the bird cage',
        'an accursed snake']  



@app.route('/')
def start_here():
    """Home page."""

    return '<a href="/hello"> Hi! This is the home page.</a>'


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          <select name="compliment">
          <option value="awesome">Awesome
          <option value="coolio">Coolio
          <option value="wowza">Wowza
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    #print  "name is empty"
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():

    # player = request.args.get("person")
    diss = choice(DISS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss:</title>
      </head>
      <body>
        I think you're %s!
      </body>
    </html>
    """ % (diss)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
