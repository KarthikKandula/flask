from flask import Flask, render_template, url_for, request

from source.deploy import runShellScript

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hello/", defaults = {'fname':None,'lname':None})
@app.route("/hello/<fname>/", defaults = {'lname':None})
@app.route("/hello/<fname>/<lname>")
def hello_name(fname,lname):
    return render_template('hello.html',fname=fname,lname=lname)

@app.route("/deploy/", defaults = {'repo':None,'branch':None})
@app.route("/deploy/<repo>/", defaults = {'branch':None})
# @app.route("/deploy/<repo>/<branch>")
def deploy(repo,branch):
    return render_template('deploy.html',repo=repo,branch=branch)

# Define a route for your API endpoint and specify the methods it accepts
@app.route('/deployapi', methods=['GET', 'POST'])
def api():
    # Create a HTML form with the fields you want to send data from in a separate template file
    if request.method == 'GET':
        return render_template('deployapi.html',shelloutput="")
    # Use request.form.to_dict() to access the data submitted by the form as a dictionary
    elif request.method == 'POST':
        data = request.form.to_dict()
        print(data)

        output = runShellScript('./scripts/git.sh',data['repo'],data['branch'])
        print(output)

        # Return a response with the data or an error message
        if data:
            # return output
            return render_template('deployapi.html',shelloutput=output)
        else:
            return {'error': 'No data received!'}

if __name__ == '__main__':
   app.run(debug = True)
   # * debug = True - server will reload itself if the code changes