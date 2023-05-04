from flask import render_template, send_file, request, jsonify
import connexion
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml", options={
        'swagger_ui': False
    })

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/api/')
def endpoints():
    return jsonify({'characters': 'https://www.archerapi.com/api/characters',
    'episodes':'https://www.archerapi.com/api/episodes',
    'quotes':'https://www.archerapi.com/api/quotes'
    })

@app.route('/about/')
def about():
    return render_template('about.html', title='Home')
    
@app.route("/documentation/")
def documentation():
    return render_template("documentation.html")

@app.route("/documentation.yml")
def swagger():
    return render_template("documentation.yml")

@app.route('/logo.png')
def serve_image():
    filename = './static/images/logo.png'  
    return send_file(filename, mimetype='image/png')

@app.route('/archer_favicon.png')
def serve_favicon_image():
    filename = './static/images/archer_favicon.png'
    return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run()
    #app.run(host="0.0.0.0", port=8000, debug=True)
