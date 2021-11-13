from flask import Flask, jsonify, request

# Initialise the app
app = Flask(__name__)


# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    # response = {"data": "Hello, World"}
    # #return jsonify(response)
    # return response

    # # passing arguments to URL and returning argument in the response:
    # name = request.args.get("name")
    # response = {"data": f"Hello, {name}jan!"}  # this way SQL injection can be done, so next approach is better
    #
    # return jsonify(response)

    # this way if user is sending wrong parameter our code will throw an error:
    # name = request.args.get("name")
    # if not name:
    #     return jsonify({"status": "error"})
    #
    # response = {"data": f"Hello, {name}!!"}
    # return jsonify(response)

    # multi-argument interactive API: takes multiple arguments, in this eg name and lastname
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        # if both first name and last name are missing, return an error
        return jsonify({"status": "error"})

    elif fname and not lname:
        # if first name is present but last name is missing
        response = {"data": f"Hello, {fname}!!"}

    elif not fname and lname:
        # if first name is missing but last name is present
        response = {"data": f"Hello, Mr. {lname}"}

    else:
        # if none of the above is true, then both names must be present
        response = {"data": f"Is your full name {fname} {lname}???"}

    return jsonify(response)


""" just run <flask run> in the terminal and hit end point in the terminal eg:
curl -i -X GET "http://127.0.0.1:5000/greet?fname=Jason&lname=Statham"
"""
