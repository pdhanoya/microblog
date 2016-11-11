from application import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/login', methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", rembmer_me=%s' % (form.openid.data, str(form.remeber_me.data)))
        return redirect('/index')
    return render_template('login.html',title='SignIn', form=form, providers = app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Param'}
    posts = [{
        'author' : {'nickname' : 'Param'},
        'body' : 'Beautiful day in Toronto'
    },
    {
        'author' : {'nickname' : 'Gagan'},
        'body' : ' Avengers was a cool movie '
    }]
    return render_template("index.html", title = 'Home', user = user, posts = posts)
