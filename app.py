from flask import Flask, render_template
import os 
from livereload import Server

app = Flask(__name__, template_folder = "templates", static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/callforpolicy')
def callforpolicy():
    return render_template('callforpolicy.html')

@app.route('/ptune')
def ptune():
    return render_template('ptune.html')

@app.route('/blogindex')
def blogindex():
    return render_template('blogindex.html')



#@app.route('/details')
#def details():
#    return render_template('details.html')
#
#@app.route('/projects')
#def projects():
#    return render_template('projects.html')
#
#@app.route('/forums')
#def forums():
#    return render_template('forums.html')
#
#@app.route('/privacy')
#def privacy():
#    return render_template('privacy.html')
#
#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template('404.html'), 404
#

if __name__ == '__main__':
    app.debug = True 
    server = Server(app.wsgi_app)
    # Watch specific paths (optional, default is 'static', 'templates')
    server.watch('static/')
    server.watch('templates/')
    server.watch('static/js/')
    server.watch('static/images/')
    server.watch('static/css/')
    server.serve(port=4000, debug = True)
    server.serve(host='127.0.0.1', port=4000, debug=True)
