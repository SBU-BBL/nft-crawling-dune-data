import requests
import yaml
from dotenv import load_dotenv
import os
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase
import argparse
import sys
# Add the root directory to sys.path
current_script_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_script_path, '..'))
sys.path.append(project_root)
from utilities.save_data import write_data_to_csv

load_dotenv()
API_KEY = os.getenv('API_KEY')

with open("config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Fetch wallet distribution over time from Dune Analytics.')
parser.add_argument('-c', '--contract', required=True, help='Contract address to query')
parser.add_argument('-t', '--time', required=True, help='daily or weekly query')
parser.add_argument('-i', '--interval', required=True, help='length of the interval query')

args = parser.parse_args()
contract_address = args.contract
time = args.time
interval = args.interval

# contract_address = '0xcBC67Ea382F8a006d46EEEb7255876BeB7d7f14d'
# time = 'weekly'
# interval = '12'

query_id = config['QUERY_ID'][time]['average_volume_price']
data_folder_path = config['PATH']['data_trading_folder']

dune = DuneClient(
    api_key=API_KEY,
    base_url="https://api.dune.com",
    request_timeout=(300) # request will time out after 300 seconds
)

try:
    query = QueryBase(
    query_id=query_id,
    
    params=[
        QueryParameter.text_type(name="Average Volume Price - weekly Contract address:", value=contract_address), 
        QueryParameter.text_type(name="Average Volume Price - weekly Time interval", value=interval)
    ]
    )

    query_result = dune.get_latest_result(query=query_id)
    # print(query)
    data_rows  = query_result.result.rows
    write_data_to_csv(__file__, time, data_folder_path, contract_address, data_rows)
except Exception as e:
    print(f"An error occurred: {e}")




