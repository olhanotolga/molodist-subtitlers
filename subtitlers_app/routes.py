from flask import Flask, render_template, url_for
from subtitlers_app import app

navbar = [
    {
        'navtext' : 'Home',
        'navlink' : '/index'
    },
    {
        'navtext' : 'About',
        'navlink' : '/about'
    },
    {
        'navtext' : 'Subtitling',
        'navlink' : '/subtitling'
    },
    {
        'navtext' : 'Translating',
        'navlink' : '/translating'
    },
    {
        'navtext' : 'Editing',
        'navlink' : '/editing'
    },
    {
        'navtext' : 'Tools',
        'navlink' : '/tools'
    },
    {
        'navtext' : 'FAQ',
        'navlink' : '/faq'
    }
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    columnone = [
        {
            'heading' : 'About',
            'paragraph' : "About the portal, its story, and sections' overview",
            'link' : 'about'
        },
        {
            'heading' : 'Subtitling',
            'paragraph' : 'How to create subtitles, file types, and structure',
            'link' : 'subtitling'
        },
        {
            'heading' : 'Translating',
            'paragraph' : 'Film translation essentials, UA language resources',
            'link' : 'translating'
        }
    ]
    h1 = 'Molodist subtitlers'
    description = 'This is an info portal for everyone who translates and subtitles for the Molodist film festival.'
    columntwo = [
        {
            'heading' : 'Editing',
            'paragraph' : 'Working with text files, editing, converting, etc.',
            'link' : 'editing'
        },
        {
            'heading' : 'Tools',
            'paragraph' : 'Links to useful tools (online and downloadable)',
            'link' : 'tools'
        },
        {
            'heading' : 'FAQ',
            'paragraph' : 'Questions & answers on film subtitling & translation',
            'link' : 'faq'
        }
    ]
    return render_template('index.html', title='Home', columnone=columnone, columntwo=columntwo, h1=h1, description=description)

@app.route('/about')
def about():
    sections = [
        {
            "title" : "About the project",
            "article" : "article1"
        },
        {
            "title" : "How to navigate",
            "article" : "article2"
        }
    ]
    return render_template('about.html', title='About', navbar=navbar, sections=sections)

@app.route('/subtitling')
def subtitling():
    sections = [
        {
            "title" : "Subtitles",
            "article" : "article1"
        },
        {
            "title" : "Timecodes vs. no timecodes",
            "article" : "article2"
        },
        {
            "title" : "Structure and rules",
            "article" : "article3"
        }
    ]
    return render_template('subtitling.html', title='Subtitling', navbar=navbar, sections=sections)

@app.route('/translating')
def translating():
    sections = [
        {
            "title" : "General guidelines",
            "article" : "article1"
        },
        {
            "title" : "Some language rules",
            "article" : "article2"
        },
        {
            "title" : "Proofreading and resources",
            "article" : "article3"
        }
    ]
    return render_template('translating.html', title='Translating', navbar=navbar, sections=sections)

@app.route('/editing')
def editing():
    sections = [
        {
            "title" : "Tips",
            "article" : "article1"
        },
        {
            "title" : "Checklist",
            "article" : "article2"
        }
    ]
    return render_template('editing.html', title='Editing', navbar=navbar, sections=sections)

@app.route('/tools')
def tools():
    return render_template('tools.html', title='Tools')

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title="404"), 404

