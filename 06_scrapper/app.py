from flask import Flask, render_template, request
from main import search_incruit

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route("/search")
def search():
	keyword = request.args.get("keyword")
	jobs = search_incruit(keyword)
	# print(keyword)

	return render_template(
		"search.html", 
		keyword=keyword, 
		jobs=enumerate(jobs)
	)

if __name__ == '__main__':
    app.run(debug=True)