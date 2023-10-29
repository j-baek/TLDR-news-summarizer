import json

def get_json_format():
    try:
        with open('news_url.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        print("not FOUND!")

    file.close()
    data = {}
    data["id"] = "10"
    data["url"] = "https://edition.cnn.com/2023/10/28/business/cities-curbs-parking-deliveries-bikers/index.html"

    existing_data.append(data)
    with open('news_url.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
        file.close()

get_json_format()