from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<p>About Page</p>"

if __name__ == '__main__':
    app.run(debug=True)


# create aa function 