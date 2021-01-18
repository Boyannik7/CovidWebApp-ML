import os
import csv
from flask import Flask, request
server = Flask(__name__)

@server.route("/analyze", methods = ['POST'])
def analyze():
    data = request.get_json(force=True)
    file_name = data['input_file_name']
    with open("../" + file_name) as f:
        return f.read(), 200

@server.route("/status/<id>")
def check_status(id):
    fields = ["Date", "Country", "Confirmed", "Deaths", "Recovered", "Active", "New cases", "New deaths", "New recovered"]
    rows = [["2020-01-01", "Turkey", "0", "0", "1", "2", "3", "4", "5"]]
    with open(os.environ['OUTPUT_DATA_FILE_NAME'] + '_' + id + ".csv", "w+") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)  
        csvwriter.writerows(rows) 
    return "done", 200

@server.route("/shutdown", methods = ['POST'])
def shutdown():
    return "", 200

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8000)
