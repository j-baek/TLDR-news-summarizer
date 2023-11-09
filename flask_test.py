from flask import Flask, render_template, request
import show_news_flask as show_news

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the entered number from the form
        entered_number = request.form['number']

        # call function from show_news_flask
        result = show_news.news_pick(entered_number)

        # Render the template with the entered number
        return render_template('index.html', entered_number=entered_number, result=result)

    # Render the initial template without the entered number
    return render_template('index.html', entered_number=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)