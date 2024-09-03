from flask import Flask, render_template

app = Flask(__name__)
#print("hello, world")
@app.route("/")  # this means whenever root gets called then print hello_world
def home():
  return render_template('home.html')

@app.route("/contact")
def contact():
  return render_template('contactus.html')

@app.route("/order")
def order():
  return render_template("ordernow.html")

@app.route("/menu")
def menu():
  return render_template("ourmenu.html")
@app.route("/pies")
def pies():
  return render_template("pies.html")

@app.route("/rolls")
def rolls():
  return render_template("rolls.html")

@app.route("/sweets")
def sweets():
  return render_template("sweets.html")

@app.route("/drinks")
def drinks():
  return render_template("drinks.html")







if __name__ == "__main__":
  app.run(host = '0.0.0.0')