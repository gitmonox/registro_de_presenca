# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    mensagens = Presenca.recupera_todas()

    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'menu': menu,
               'mensagens': mensagens
               }

    return render_template('index.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar_mensagem():
    mensagem = Presenca(request.form['email'], request.form['presenca'],
                        request.form['resposta'], request.form['comentario'])
    mensagem.gravar()
    return redirect('/')


@app.route('/presenca')
def presenca():
    menu = [{'active': False,
             'href': '/alunos',
             'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('presenca.html', **context)


@app.route('/alunos')
def alunos():
    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('alunos.html', **context)


@app.route('/wesley')
def wesley():
    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('wesley.html', **context)


@app.route('/bruno')
def bruno():
    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('bruno.html', **context)


@app.route('/rubens')
def rubens():
    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('rubens.html', **context)


@app.route('/rolf')
def rolf():
    menu = [{'active': False,
             'href': '/presenca',
             'texto': 'Presença'}, {'active': False,
                                    'href': '/alunos',
                                    'texto': 'Alunos'}]
    context = {'menu': menu}
    return render_template('rolf.html', **context)


app.run()
