from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import subprocess,sys

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print (form.errors)
        if request.method == 'POST':
            name=request.form['name']
            salutation =request.form['salutation']
            cmd = "C:\\Scripts\\adhoc\\backend\\app\\scripts\\hello.ps1 " + str(salutation)+ " "+str(name)
            print(cmd)	
            p = subprocess.Popen(["powershell.exe",cmd],stdout=sys.stdout)
            p.communicate()

        return (render_template('hello.html', form=form))

if __name__ == "__main__":
    app.run(host='localhost',debug=True)