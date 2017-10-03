from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html')

@app.route('/echo', methods=['GET'])
def echo():
    return "<h1>Hello, " + request.args['firstname'] + "!</h1>"
    

if __name__ == ('__main__'):
    app.debug = True
    app.run()
        
