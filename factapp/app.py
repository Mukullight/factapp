from flask import Flask, render_template
import os 

app = Flask(__name__, template_folder = "templates", static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/data')
#def data():
#    return render_template('data.html')
#
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
    app.run(debug=True)