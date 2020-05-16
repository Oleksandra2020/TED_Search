"""
Runs flask app
"""
from flask import Flask, render_template, request
import ssl
from search import Search


app = Flask(__name__)
app.config["DEBUG"] = True
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/results", methods = ['POST'])
def show_search_results():
    variable = request.form['acc']
    talks = Search(variable).node_pusher()
    if talks == []:
        return render_template('no_response.html')
    talk = talks[0]
    result = """
    <html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width, height=device-height">
        <style>
        div {
            position: absolute;
            min-height: 1000px;
            min-width: 1700px;
            background: url(https://s17736.pcdn.co/wp-content/uploads/2016/05/shutterstock_161594762.jpg) repeat-x;
            background-size:cover;
            }
        </style>
    </head>
    <body>
    <div>
        <h1 style="color: white; position: absolute; margin-left: 5%; margin-top: 5%; font-size: px;font-style:inherit;">
        <form method="post" action="/">
            <center><input 
                value="TED ПОШУК" 
                style="text-align: center; font-size: xx-large; color: brown; margin-bottom: 7 em; margin-left: 2em" 
                type="submit">
            </center>
        </form>
        <h1 style="color: white; text-align:center; margin-top: 5em; font-size:25px;font-style:inherit;">
        Результат пошуку: """ + \
        talk.next.data + \
        f"""
        <a href="{talk.tail().previous.data}" "style="color: white"change hyperlink color>ted link</a>
        </h1>
        <h1 style="color: white; text-align:center; font-size:25px;font-style:inherit;">
        <bottom><iframe width="700" height="455" src=https://www.youtube.com/embed/{talk.data[:-5]} 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </bottom>
        </h1>
        <h1  style="color: white; position: absolute; margin-top: 4em; margin-left: 25em; font-size:20px;font-style:inherit;">
        {talk.next.next.data} переглядів
        </h1>
        <h1  style="color: white; position: absolute; margin-left: 10em; margin-right: 10em; text-align:center; font-size:20px;font-style:inherit;">
        {talk.tail().data}
        </h1>
        """
    i = 22
    for talk in talks[1:]:
        result += \
            f"""
            <h1  style="color: white; position: absolute; margin-left: 55em; margin-top: 2 em; top: {i}%; font-size:22px;font-style:inherit;">
            <a href="https://www.youtube.com/watch?v={talk.data[:-5]}"style="color: white"change hyperlink color>{talk.next.data}</a>
            """
        i += 5
    end = """
    </div>
    </body>
</html>
"""
    return result


if __name__ == "__main__":
    app.run(debug=True)
