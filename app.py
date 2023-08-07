from flask import Flask, request
import yaml
import json
from bot import send_message

app = Flask(__name__)

report_registry = None

@app.route('/register-report', methods=['GET', 'POST'])
def register_report():
    if request.method == 'POST':
        json_bytes = request.data
        json_str = json_bytes.decode('utf-8')
        data = json.loads(json_str)

        with open(r'config.yaml') as file:
            report_list = yaml.load(file, Loader=yaml.FullLoader)

        unparsed_name = data['name'] 
        name = unparsed_name.split('(')[0].strip()
        report = report_list[name]

        part = unparsed_name.split('(')[1][0:-1]
        
        pages = report['pages']

        page_received_index = pages.index(int(part))
        print(page_received_index)
        
        global report_registry
        try:         
            if page_received_index not in report_registry[name]:
                report_registry[name].append(page_received_index)
        except TypeError:
            report_registry = {
                name: [page_received_index]
            }
        send_message(f'Report {name}')
        return str(page_received_index)

if __name__ == '__main__':
    app.run(debug=True)
