from flask import Flask, request, jsonify, render_template

#######################################################################################
from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED

@app.route('/')
def hello():
    user = 'Egor'

    return render_template('main.html', user= user)

@app.route('/api')
def api():
    user = 'Egor'

    return render_template('api.html', user= user)

@app.route('/docs')
def docs():
    user = 'Egor'

    return render_template('main.html', user= user)

@app.route('/settings')
def settings():
    user = 'Egor'

    return render_template('settings.html', user= user)

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        data = request.args

        return ''

def main():
    app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)

if __name__ == '__main__':
    main()