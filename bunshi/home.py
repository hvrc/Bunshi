# ?
from bunshi import app
from bunshi.info import getInfo
from flask import flash, render_template, session, request

# TODO This is probably what's causing the recent error
recent = []
recentMax = 5

# route to homepage
@app.route("/", methods = ["POST", "GET"])
def home():
    # default/null values passed when POST method isn't called
    owoEgg = False
    acetateEgg = False
    preferred = True
    error = False
    imageSource = ""
    pageURL = ""
    IUPAC = ""
    formula = ""
    weight = ""

    if request.method == "POST":
        # compound defined as value specified in form
        posts = request.form
        for post in posts.items():
            compound = post[1].lower()

        try:
            info = getInfo(compound)
            imageSource = info[0]
            pageURL = info[1]
            IUPAC = info[2]
            formula = info[3]
            weight = info[4]
            preferred = info[5]

            # conditionals for easter eggs
            if IUPAC == "dioxotungsten":
                owoEgg = True

            if IUPAC == "acetate":
                acetateEgg = True

            if compound in recent:
                recent.remove(compound)
            recent.insert(0, compound)

            if len(recent) > recentMax:
                recent.pop(-1)

        except TypeError as e:
            error = True

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = compound,
                               pageURL = pageURL,
                               IUPAC = IUPAC,
                               formula = formula,
                               weight = weight,
                               owoEgg = owoEgg,
                               acetateEgg = acetateEgg,
                               preferred = preferred,
                               error = error
                               )

    return render_template("home.html")
