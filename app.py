from __future__ import print_function
import sys
import json
import logging
from flask import Flask, flash, request, url_for, redirect, render_template
from Project import get_nearest_station, check_accessibility

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ 
    Create a results page for the user to get an answer after submitting their location
    request.

    Gets the information from the submission bar on the website and stores the information in a 
    a variable called place. Then, gets the results from variables get_nearest_station and
    check accessibility from Project.py and stores them in their respective variables. Checks the
    validity of check_accessibility to convert True or False result to a string. Then redirects the
    results from the variables to the results page.
    
    """

    if request.method == 'POST':
        place = request.form.get('place_name')
        print(json.dumps(place), file=sys.stderr) #checks that computer receives input

        result_nearest_station = get_nearest_station(12.44, 14.22)
        result_accessibility = check_accessibility(result_nearest_station)
        string_accessibility = ''

        if result_nearest_station == True:
            string_accessibility = 'true'
        else:
            string_accessibility = 'false'

        print(result_nearest_station, file=sys.stderr) #checks result_nearest_station to make sure it's correctly outputting
        print(string_accessibility, file=sys.stderr) #checks string_accesibility to make sure it's correctly outputting
        
        return redirect(url_for('results', ACCESSIBLE = json.dumps(string_accessibility), BUSSTOP = json.dumps(result_nearest_station)))
    
    return render_template('index.html')

@app.route('/results/', methods=['GET', 'POST'])
def results():
    BUSSTOP = request.args['BUSSTOP']
    ACCESSIBLE = request.args['ACCESSIBLE']
    return  render_template('results.html', BUSSTOP = json.loads(BUSSTOP), ACCESSIBLE = json.loads(ACCESSIBLE))


if __name__ == "__main__":
    app.run(debug=True)




