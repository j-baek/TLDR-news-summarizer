from flask import Flask, render_template, request
import show_news_flask as show_news
import headline as headline_function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # give headline_url to get today's news
    headline_url = "https://edition.cnn.com/business/tech"
    # call a function to get today's news
    headline_function.check_last_headline_update(headline_url)

    if request.method == 'POST':
        # Get the entered number from the form
        selected_mode = request.form.get("mode")
        # call function from show_news_flask
        result = show_news.news_pick(selected_mode)

        # Render the template with the entered number
        return render_template('index.html', result=result)

    # Render the initial template without the entered number
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)