from flask import Flask, render_template, url_for
from subtitlers_app import app

navbar = [
    {
        'navtext' : 'Головна',
        'navlink' : '/index'
    },
    {
        'navtext' : 'Проєкт',
        'navlink' : '/about'
    },
    {
        'navtext' : 'Субтитрування',
        'navlink' : '/subtitling'
    },
    {
        'navtext' : 'Переклад',
        'navlink' : '/translating'
    },
    {
        'navtext' : 'Редагування',
        'navlink' : '/editing'
    },
    {
        'navtext' : 'Інструментарій',
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
            'heading' : 'Про проєкт',
            'paragraph' : "Про проєкт: передісторія сайту та огляд його основних розділів.",
            'link' : 'about'
        },
        {
            'heading' : 'Субтитрування',
            'paragraph' : 'Субтитри з таймкодами і «під клацання», їхня структура тощо.',
            'link' : 'subtitling'
        },
        {
            'heading' : 'Переклад',
            'paragraph' : 'Загальні рекомендації щодо перекладу, правопис та корисні посилання.',
            'link' : 'translating'
        }
    ]
    h1 = 'Molodist subtitlers'
    description = 'Інфомайданчик для перекладачів і субтитрувальників кінофестивалю «Молодість».'
    columntwo = [
        {
            'heading' : 'Редагування',
            'paragraph' : 'Поради щодо зведення кількості помилок і одруківок до мінімуму.',
            'link' : 'editing'
        },
        {
            'heading' : 'Інструментарій',
            'paragraph' : 'Арсенал перекладачів-субтитрувальників та додаткові ресурси.',
            'link' : 'tools'
        },
        {
            'heading' : 'FAQ',
            'paragraph' : 'Запитання та відповіді щодо перекладу, субтитрування та редагування.',
            'link' : 'faq'
        }
    ]
    background = "bg-dark"
    return render_template('index.html', title='Головна', columnone=columnone, columntwo=columntwo, h1=h1, description=description, background=background)

@app.route('/about')
def about():
    sections = [
        {
            "title" : "Про проєкт",
            "article" : "article1"
        },
        {
            "title" : "Розділи",
            "article" : "article2"
        }
    ]
    return render_template('about.html', title='Про проєкт', navbar=navbar, sections=sections)

@app.route('/subtitling')
def subtitling():
    sections = [
        {
            "title" : "Cубтитри",
            "article" : "article1"
        },
        {
            "title" : "Таймкоди: з та без",
            "article" : "article2"
        },
        {
            "title" : "Структура",
            "article" : "article3"
        }
    ]
    return render_template('subtitling.html', title='Субтитрування', navbar=navbar, sections=sections)

@app.route('/translating')
def translating():
    sections = [
        {
            "title" : "Загальне",
            "article" : "article1"
        },
        {
            "title" : "Правопис",
            "article" : "article2"
        },
        {
            "title" : "Перевірка тексту",
            "article" : "article3"
        }
    ]
    return render_template('translating.html', title='Переклад', navbar=navbar, sections=sections)

@app.route('/editing')
def editing():
    sections = [
        {
            "title" : "Поради",
            "article" : "article1"
        },
        {
            "title" : "Чекліст",
            "article" : "article2"
        }
    ]
    return render_template('editing.html', title='Редагування', navbar=navbar, sections=sections)

@app.route('/tools')
def tools():
    sections = [
        {
            "title" : "Текстові редактори",
            "article" : "article1"
        },
        {
            "title" : "Перевірка правопису",
            "article" : "article2"
        },
        {
            "title" : "Для субтитрування",
            "article" : "article3"
        },
        {
            "title" : "Конвертація",
            "article" : "article4"
        },
        {
            "title" : "Ще інструменти",
            "article" : "article5"
        }
    ]
    return render_template('tools.html', title='Інструментарій', navbar=navbar, sections=sections)

@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ', navbar=navbar)

@app.errorhandler(404)
def page_not_found(error):
    background = "bg-dark"
    return render_template('page_not_found.html', title="404", navbar=navbar, background=background), 404

