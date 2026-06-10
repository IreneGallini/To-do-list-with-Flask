from flask import Flask

app= Flask(__name__) #referencing this file

# set up routes
@app.route('/') #pass in URL string for your route
def index(): #define function for route
    return "Hello World"

if __name__=="__main__": #this code runs only if you execute or import name directly
    app.run(debug=True) #errors will pop up on web page
