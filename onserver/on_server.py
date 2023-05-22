import json
import subprocess
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler()]
)


def LoadConfig():
    path = "/".join(os.path.abspath(__file__).split("/")[:-1]) + "/config.json"
    loadedConfig = {}
    if os.path.exists(path):
        with open(path, 'r') as file:
            loadedConfig = json.load(file)
    else:
        logging.debug(f'No config file at: {path}')
    return loadedConfig


config = LoadConfig()
serverIp = config["ip"]
dct = {}
proc = subprocess.run(["who"], stdout=subprocess.PIPE)
ssh_connectios = proc.stdout.decode("utf-8").count("pts")
dct["ssh_connections"] = ssh_connectios
loadAvg = os.getloadavg()
dct["load_1"] = loadAvg[0]
dct["load_5"] = loadAvg[1]
dct["load_15"] = loadAvg[2]
logging.debug(f"ssh balance@10.10.10.1 python3 balance.py {json.dumps(dct)}")
subprocess.run(["ssh", f"balance@{serverIp}", f"{json.dumps(dct)}"])
