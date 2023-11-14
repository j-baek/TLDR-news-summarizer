from flask import Flask, render_template, request
import show_news_flask as show_news
import headline as headline_function
import os

app = Flask(__name__)

# get the current directory of this file
curr_dir = os.path.dirname(os.path.realpath(__file__)) # __file__ is a path to this current script
# move up one level to the whole directory
whole_dir = os.path.dirname(curr_dir)

# construct the path to the index.html file
template_folder = os.path.join(whole_dir, 'frontend', 'templates')

# tell Flask where to find the template
app.template_folder = template_folder

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