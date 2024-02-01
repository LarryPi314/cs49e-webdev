from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/simple_power")
def power():
    return "More power!"


@app.route('/power')
def handle_power():
    """ small non-templated example
        task for us:  add another parameter ("base")
                      motivate templates!
    """
    exp = 5   # default value of exponent: take the 5th power
    base = 2
    if request.method == 'GET':    # if 'GET' then request.args exists
        parameters = request.args  # it's a dictionary of parameters
        if "exp" in parameters:
            exp = float(parameters["exp"])  # possible error!
        if "base" in parameters:
            base = float(parameters["base"])
    # Get the power!
    result = base ** exp
    # make sure it's a string...
    result = str(result)
    # return result

    # who needs templates? :)
    return f"""
    <font size = "42px" color = "DodgerBlue" > {result} </font>
    """


@app.route('/doubler_input')
def input_form():
    """ loads the HTML template with a small form
    """
    return render_template('doubler_input.html')


@app.route('/doubler', methods=['GET', 'POST'])
def doubler():
    """ loads the HTML template with a small form
    """
    input_string = "Poptarts!"
    output_string = "POPTARTS!!"
    if request.method == 'POST':
        if "input_text" in request.form:
            input_string = request.form["input_text"]
            output_string = input_string + input_string
    return render_template('doubler_output.html',
                           input_to_doubler=input_string,
                           output_of_doubler=output_string)


@app.route('/daystobirthday')
def daystobirthday():
    from datetime import datetime
    current_date = datetime.now()

    next_birthday = datetime(current_date.year, 9, 21)

    if current_date > next_birthday:
        next_birthday = datetime(
            current_date.year + 1, 9, 21)

    # Calculate the time difference
    time_difference = next_birthday - current_date

    return render_template('birthday.html', days_left=time_difference.days)


@app.route('/nonstylish')
def nonstylish():
    ''' loads the HTML template with my "nonstylish", basic self...
    '''
    return render_template('uglyme.html')

@app.route('/stylish')
def stylish():
    """ loads the HTML template with one's "stylish" self...
    """
    return render_template('stylish.html')

@app.route('/gptclone')
def gptclone():
    return render_template('gptclone.html')

import json
import requests
@app.route('/generate_response', methods=['POST'])
def generate_response():
    # Get user input from the form
    user_input = request.form['userInput']

    # Call the OpenAI GPT API

    response = generate_gpt_response(user_input)
    # try:
    #     parsedJSON = json.loads(response)
    #     text = parsedJSON["content"]
    # except:
    #     text = "Error: Response is not in JSON format."
    # Return the response as JSON
    return render_template('gptgeneration.html', your_response=response)
    

def generate_gpt_response(input_text):
    #api_key = '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'
    api_key = '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'
    api_url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'temperature': 1.0,
        'stream': False,
        'n': 1,
        'prompt': input_text,
        'max_tokens': 150,
    }

    # Make a POST request to the OpenAI API
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        return json()['choices'][0]['text']
    else:
        return f"Error: {response.status_code} - {response.text}"

#

if __name__ == "__main__":
    app.run(debug=True)
