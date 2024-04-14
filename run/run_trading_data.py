import subprocess
import logging
from datetime import datetime, timedelta
from argparse import ArgumentParser
import os

# Set up logging
logging.basicConfig(filename='trading_log.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_name, contract, time, interval):
    try:
        subprocess.run([
            'python', script_name, 
            '--contract', contract, 
            '--time', time, 
            '--interval', interval
        ], check=True)
        logging.info(f"Successfully ran {script_name} with contract {contract}, time {time}, interval {interval}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Script {script_name} failed with error: {e}")

if __name__ == '__main__':

    # testing
    param = {
        "contract": "0xcBC67Ea382F8a006d46EEEb7255876BeB7d7f14d", "time": "weekly", "interval": "12"
    }

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    scripts_directory = "get_trading_data"
    scripts_directory = os.path.join(repo_root, scripts_directory)


    for filename in os.listdir(scripts_directory):
        if filename.endswith(".py") and filename.startswith("get_"):
            # Construct the full file path
            script_path = os.path.join(scripts_directory, filename)
            print(script_path)
            run_script(script_path, param['contract'], param['time'], param['interval'])
