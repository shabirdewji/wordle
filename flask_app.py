from flask import Flask, request
from processing import do_calculation
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])

def adder_page():
    errors = ""

    if request.method == "POST":
        word = None
        nword = None
        must = None
        sword = None

        try:
            word = (request.form["word"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["word"])
        try:
            nword = (request.form["nword"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["nword"])
        try:
            must = (request.form["must"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["must"])
        try:
            sword = (request.form["sword"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["sword"])
        if word is not None :

            result = do_calculation(word, nword, must, sword)
            mod_info = result
            mod_info = str(mod_info).replace("', '", "")
            mod_info = str(mod_info).replace("(['", "")
            mod_info = str(mod_info).replace("']", "")
            mod_info = str(mod_info).replace(")", "")
            mod_info = str(mod_info).replace("'", "")
            mod_info = str(mod_info).replace(",", "")
            return '''
                <html>
                    <body>
                        <p style="font-size:24px;">The result are : </p>
                        <p style="font-size:18px;">{mod_info}</style></p>
                        <p><a href="/">
                           <input style="font-weight: bold;font-size:24px; color:black" type="submit" value="Start another search" /></p></a>                    </body>
                </html>
            '''.format(mod_info=mod_info)
    return '''
        <html>
            <head>
                <title>WORDLE HELPER</title>
            </head>
            <body bgcolor="#F0F8FF">
            <h1><font color="green">W<font color="black">O<font color="green">R<font color="black">D<font color="green">L<font color="black">E HELPER</h1>
                <form method="post" action=".">
                    <p style="font-size:24px;">1. Type in <font color=”green”>GREEN</font> letter(s) e.g *LO** :</p>
                    <p style="font-size:24px;"><input style="font-size:24px;" type="text" id="text" name="word" />
                    <p style="font-size:24px;">2. Type in <strong>BLACK</strong> letters :</p>
                    <p style="font-size:24px;"><input style="font-size:24px;" type="text" name="nword" /></p>
                    <p style="font-size:24px;">3. Type in the YELLOW letters :</p>
                    <p style="font-size:24px;"><input style="font-size:24px;" type="text" name="must" /></p>
                    <p style="font-size:24px;">4. OPTIONAL: Type in the YELLOW letters and their poistion.
                    For example, you have an R in the 3rd place, then enter <strong>r3</strong>.
                    Another example, you have R in the 3rd and M in the 5th (both YELLOW), enter <strong>r3m5</strong> :</p>

                    <p style="font-size:24px;"><input style="font-size:24px;" type="text" name="sword" /></p>
                    <p style="font-size:34px;"><input style="font-weight: bold;font-size:30px; color:green" type="submit" value="Start the search" /></p>
                </form>


            </body>
        </html>
    '''.format(errors=errors)