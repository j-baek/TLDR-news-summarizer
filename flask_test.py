from flask import Flask, render_template
import json
import textSoup as data_function
app = Flask(__name__)

@app.route('/')

def news_summary():
    try:
        with open('news_data.json', 'r') as file:
            news_data = json.load(file)
            file.close()
    except FileNotFoundError:
        print("json file not FOUND")
    
    summary = news_data[14]["title"] + "\n" + "\n" + news_data[14]["summary"]
    return summary
    
    
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')