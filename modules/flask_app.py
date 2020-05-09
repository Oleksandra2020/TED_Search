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
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <style>
        div {
                height: 975px;
                background: url(https://s17736.pcdn.co/wp-content/uploads/2016/05/shutterstock_161594762.jpg) 100% 100% no-repeat;
                background-size: cover;
            }
        </style>
    </head>
    <body  style="text-align: center;">
    <div>
        <h1 style="color: white; position: absolute; left: 5%; top: 5%; font-size: px;font-style:inherit;">
        <form method="post" action="/">
            <center><input 
                value="TED ПОШУК" 
                style="text-align: center; font-size: xx-large; color: brown; margin-bottom: 7 em" 
                type="submit">
            </center>
        </form>
        </h1>
        <h1 style="color: white; position: absolute; left: 29%; top: 14%; font-size:25px;font-style:inherit;">
        Результат пошуку: """ + \
        talk.next.data + \
        f"""
        <a href="{talk.next.next.next.data}" "style="color: white"change hyperlink color>ted link</a>
        </h1>
        <h1 style="color: white; position: absolute; left: 30%; top: 20%; font-size:25px;font-style:inherit;">
        <bottom><iframe width="700" height="455" src=https://www.youtube.com/embed/{talk.data[:-5]} 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </bottom>
        </h1>
        <h1  style="color: white; position: absolute; left: 30%; top: 70%; font-size:20px;font-style:inherit;">
        {talk.next.next.data} переглядів
        </h1>
        <h1  style="color: white; position: absolute; left: 10%; right: 10%; top: 80%; font-size:20px;font-style:inherit;">
        {talk.tail(talk).data}
        </h1>
        """
    i = 30
    for talk in talks[1:]:
        print(talk.tail(talk).data)
        result += \
            f"""
            <h1  style="color: white; position: absolute; left: 73%; top: {i}%; font-size:19px;font-style:inherit;">
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
