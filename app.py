from flask import Flask, render_template, request, jsonify
from ice_breaker_linkedin import ice_break
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_and_facts, profile_pic_url = ice_break(
        name=name
    )
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
