from flask import Flask, request
from flask.json import jsonify
import json
import os

FILENAME = 'bookings.json'

app = Flask(__name__)
# Stop the json response to get sorted
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def api_doc():
    response_data = {
        "status": 200,
        "message": "Up and Running",
        "api doc": "https://documenter.getpostman.com/view/12174054/TW6xnngp",
        "developed by": "Ashutosh Krishna",
        "github repo": "https://github.com/ashutoshkrris/VityasaIH",
        "github profile": "https://github.com/ashutoshkrris",
        "portfolio": "https://ashutoshkrris.tk"
    }
    return response_data


# Question 1
@app.route('/items', methods=['POST'])
def question_one():
    # Get json data from POST request
    data = request.get_json('items')
    # Get the list items from json data
    list_items = data["items"]
    # Create a new list and append all the positive numbers only
    new_list = []
    for element in list_items:
        try:
            element = int(element)
            if element > 0:
                new_list.append(element)
        except ValueError:
            pass
    response_data = {
        "valid_entries": len(new_list),
        "invalid_entries": len(list_items)-len(new_list),
        "min": min(new_list),
        "max": max(new_list),
        "average": sum(new_list)/len(new_list)
    }
    return response_data


# Question 2
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Getting json data from request
        request_data = request.get_json()
        # Extracting slot number and name
        slot_number = request_data['slot']
        name = request_data['name']
        # Check if a bookings.json file exists
        if os.path.isfile(FILENAME):
            # Load the json data from the file if it exists
            with open(FILENAME) as file:
                file_data = json.load(file)
                for data in file_data:
                    # Iterate over the json data and match the slot number with the requested slot number
                    if data["slot"] == slot_number:
                        # if there is already 2 bookings
                        if len(data["name"]) >= 2:
                            return {"status": f"slot full, unable to save booking for {name} in slot {slot_number}"}
                        # if there is less than 2 bookings, append the name in that slot
                        else:
                            data["name"].append(name)
                            with open(FILENAME, "w") as file:
                                json.dump(file_data, file, indent=4)
                            return {"status": "confirmed"}
                # if there is no booking in that slot
                else:
                    temp = {
                        "slot": slot_number,
                        "name": [name]
                    }
                    file_data.append(temp)
                    with open(FILENAME, "w") as file:
                        json.dump(file_data, file, indent=4)
                    return {"status": "confirmed"}
        # if file doesn't exist, create a file and dump the data
        else:
            new_dict = {
                "slot": slot_number,
                "name": [name]
            }
            with open(FILENAME, "w") as file:
                json.dump([new_dict], file, indent=4)
            return {"status": "confirmed"}
    # if GET request is made, return all the bookings from bookings.json
    else:
        with open(FILENAME) as file:
            data = json.load(file)
            for d in data:
                if len(d["name"]) == 1:
                    d["name"] = d["name"][0]
        return jsonify(data)


@app.route('/cancel', methods=['POST'])
def cancel_booking():
    # get the json data from request
    request_data = request.get_json()
    slot_number = request_data["slot"]
    name = request_data["name"]
    # open the bookings.json file and load the data
    with open(FILENAME) as file:
        file_data = json.load(file)

    # iterate over the data
    for data in file_data:
        # if there is a slot with the slot in request slot
        if data["slot"] == slot_number:
            # if name is in the slot booking
            if name in data["name"]:
                data["name"].remove(name)
                with open(FILENAME, "w") as file:
                    json.dump(file_data, file, indent=4)
                return {"status": f"canceled booking for {name} in slot {slot_number}"}
    # if no such slot or no such name
    return {"status": f"no booking for the name {name} in slot {slot_number}"}


# @app.route('/plot', methods=['POST'])
# def check_square():
#     request_data = request.get_json()
#     x, y = request_data["x"], request_data["y"]
#     points.append((x,y))
#     print(points)
#     return jsonify(points)


if __name__ == '__main__':
    # points = []
    app.run(debug=False)
