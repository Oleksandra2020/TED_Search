"""
Runs flask app
"""
from flask import Flask, render_template, request
import ssl
from search import SearchADT


app = Flask(__name__)
app.config["DEBUG"] = True
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/results", methods=['POST'])
def show_search_results():
    variable = request.form['acc']
    search = SearchADT(variable)
    talks = search.add_details()
    if talks == []:
        return render_template('no_response.html')
    talk = talks[0]
    return render_template('main.html', video_title=talk.get_title(),
                           ted_link=talk.get_ted_link(),
                           video_id=talk.get_id()[:-5], views=talk.get_views(),
                           num_translator=search.get_same_translator(
                               talk.get_id()),
                           description=talk.get_description(), t=talks[1:])

@app.route("/new_video", methods=['POST'])
def video_play():
    variable = request.form['acc']

if __name__ == "__main__":
    app.run(debug=True)
