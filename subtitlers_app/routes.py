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
            'paragraph' : "About the portal, the story behind it, and overview of its main sections.",
            'link' : 'about'
        },
        {
            'heading' : 'Subtitling',
            'paragraph' : 'Subtitle files with and without timecodes, their structure and insides.',
            'link' : 'subtitling'
        },
        {
            'heading' : 'Translating',
            'paragraph' : 'Film translation essentials, known language issues, and useful resources.',
            'link' : 'translating'
        }
    ]
    h1 = 'Molodist subtitlers'
    description = 'This is an info portal for everyone who translates and subtitles movies for the Molodist film festival.'
    columntwo = [
        {
            'heading' : 'Editing',
            'paragraph' : 'Minimizing the number of errors and typos and the editing checklist.',
            'link' : 'editing'
        },
        {
            'heading' : 'Tools',
            'paragraph' : 'A typical subtitler’s toolset and links to selective tools (offline and online).',
            'link' : 'tools'
        },
        {
            'heading' : 'FAQ',
            'paragraph' : 'Main questions and answers on film subtitling, translation, and editing.',
            'link' : 'faq'
        }
    ]
    background = "bg-dark"
    return render_template('index.html', title='Home', columnone=columnone, columntwo=columntwo, h1=h1, description=description, background=background)

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
            "title" : "(No) timecodes",
            "article" : "article2"
        },
        {
            "title" : "Structure",
            "article" : "article3"
        }
    ]
    return render_template('subtitling.html', title='Subtitling', navbar=navbar, sections=sections)

@app.route('/translating')
def translating():
    sections = [
        {
            "title" : "General",
            "article" : "article1"
        },
        {
            "title" : "Language rules",
            "article" : "article2"
        },
        {
            "title" : "Proofreading",
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
    sections = [
        {
            "title" : "Text editors",
            "article" : "article1"
        },
        {
            "title" : "Spell checkers",
            "article" : "article2"
        },
        {
            "title" : "Subtitling software",
            "article" : "article3"
        },
        {
            "title" : "File/text conversion",
            "article" : "article4"
        },
        {
            "title" : "Custom tools",
            "article" : "article5"
        }
    ]
    return render_template('tools.html', title='Tools', navbar=navbar, sections=sections)

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ', navbar=navbar)

@app.errorhandler(404)
def page_not_found(error):
    background = "bg-dark"
    return render_template('page_not_found.html', title="404", navbar=navbar, background=background), 404

