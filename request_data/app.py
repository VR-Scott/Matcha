from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website') #None

    return '''<h1>The language is : {}</h1>
        <h1>The framework is : {}</h1>
        <h1>The website is : {}</h1>
    '''.format(language, framework, website)

@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    
    if request.method == 'POST':
        language = request.form.get('languages')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}.</h1>'.format(language, framework)

    return '''<form method="POST">
        Language <input type="text" name="language">
        Framework <input type="text" name="framework">
        <input type="submit">
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)