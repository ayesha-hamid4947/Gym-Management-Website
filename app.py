from flask import Flask, render_template

app = Flask(__name__)

# Welcome Route (Welcome page)
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Home Route (Main page)
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/submit', methods=['POST'])
def submit_form():
    # Your form handling logic here
    return redirect(url_for('home'))


# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Membership Route
@app.route('/membership')
def membership():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(debug=True)
