from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def resume():
    
    title = "Моє резюме"
    return render_template('resume.html', title=title)


@app.route('/contact')
def contact():
    title = "Контакти"
    return render_template('contact.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)