from flask import Flask, render_template, url_for
from subtitlers_app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    columnone = [
        {
            'heading' : 'About',
            'paragraph' : 'About the portal and its structure overview'
        },
        {
            'heading' : 'Subtitling',
            'paragraph' : 'How to create subtitles, file types, software'
        },
        {
            'heading' : 'Translating',
            'paragraph' : 'Film translation essentials, UA language resources'
        }
    ]
    h1 = 'Molodist subtitlers'
    description = 'This is an info portal for everyone who translates and subtitles for the Molodist film festival.'
    columntwo = [
        {
            'heading' : 'Editing',
            'paragraph' : 'Working with text files, editing, converting, etc.'
        },
        {
            'heading' : 'Tools',
            'paragraph' : 'Links to useful tools (online and downloadable)'
        },
        {
            'heading' : 'FAQ',
            'paragraph' : 'Questions & answers on film subtitling & translation'
        }
    ]
    return render_template('index.html', title='Home', columnone=columnone, columntwo=columntwo, h1=h1, description=description)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/subtitling')
def subtitling():
    return render_template('subtitling.html', title='Subtitling')

@app.route('/translating')
def translating():
    return render_template('translating.html', title='Translating')

@app.route('/editing')
def editing():
    return render_template('editing.html', title='Editing')

@app.route('/tools')
def tools():
    return render_template('tools.html', title='Tools')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')



