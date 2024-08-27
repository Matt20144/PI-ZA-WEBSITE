from flask import Flask, render_template

app = Flask(__name__)
#print("hello, world")
@app.route("/")  # this means whenever root gets called then print hello_world

def home():
  return render_template('ordernow.html')

@app.route("/contact")
def contact():
  return render_template('contactus.html')






if __name__ == "__main__":
  app.run(host = '0.0.0.0')