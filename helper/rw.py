import yaml
from pathlib import Path


def read_data_from_file(filepath: str):
    with open(filepath, 'r') as f:
        data = f.read()
    return data

def write_to_file(data: str, filename: str):
    out_path = f"output/{filename}"
    Path("output").mkdir(parents=True, exist_ok=True)

    with open(out_path, 'w') as o:
        o.write(data)

# ----------------------------------------------------------------------
def read_config(filepath: str):
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    return config

def read_data_from_config(config: dict):

    data = None
    if config['source']['file']['enable']:
        filepath = config['source']['file']['filepath']
        data = read_data_from_file(filepath)

    # elif config['source']['databse']['enable']:

    return data

def write_output(config: dict, data: str):
        
    if config['sink']['file']['enable']:
        filename = config['sink']['file']['filename']
        write_to_file(data, filename)

    # add more sinks

def generate_config_from_source_target(source: str, target: str):

    config =  {
        "source": {
            "file": {
                "enable": True,
                "filepath": source
            }
        },
        "sink": {
            "file": {
                "enable": True,
                "filename": target
            }
        }
    }
    return config
