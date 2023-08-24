# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Shyam" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/dad")
def home1():

    name = "Kuga" # write your name
    age = "47" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mom")
def home2():

    name = "Meera" # write your name
    age = "40" # write your age

    return render_template('index.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/jack")
def home3():

    name = "jack" # write your name
    age = "4" # write your age

    return render_template('index.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
