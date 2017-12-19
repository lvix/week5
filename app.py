import os
from flask import Flask 
import json, re


def create_app():
    """create and inittialize Flask app
    returns:
        app(object): Flask App instance 
    """

    app = Flask('rmon')

    # load json configuations file name 
    file = os.environ.get('RMON_CONFIG')

    # TODO load configs from the json file and transcript them into app.config 
    conf = load_config(file)
    app.config.update(conf)
    # app.config.from_object(load_config(file))

    return app 

def load_config(file_path):
    """
    load a json-like config file and strip its comment lines
    returns:
        config_content: Dict instance
    """
    try:
        js_content = ''
        with open(file_path) as conf:
            for line in conf:
                if not line.strip().startswith('#'):
                    
                    if ':' in line:
                        colon_pos = line.find(':')
                        js_content += line[:colon_pos].upper() + line[colon_pos:]
                    else:
                        js_content += line 
        print(js_content)
        config_content = json.loads(js_content)
        return config_content
    except:
        return 

app = create_app()

@app.route('/')
def index():
    res = ''
    for k, v in app.config.items():
        res = res + str(k) + ' : ' + str(v) + '<br>'
    return res



