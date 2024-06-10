# nft-crawling-dune-data

This repo is specifically designed for getting the data from Dune for each contract address of each collection of each category. Therefore, the input here will be the csv file that has contract addresses of each category and the output will be the data table of average volume price, intraday volatily, unique buyers and sellers and wallet distribution for each category.

Also, this repo only serves the use of getting the data from Dune to local database and it has nothing to do with the logic of query the data. If the users want to check or change the logic of how to query the data, please check the corresponding SQL scripts in the Dune website. The users can go into the config file to use the ID to trace back which SQL scripts are used in Dune. 

Here are some steps that walk the users through the process of how to use this repo:

1. Go into the config file, change the following line to the path that you want to store your data:

    data_trading_folder: '/Users/vuh/Documents/nft-crawling-dune-data/data/trading_data'

2. Go into the run folder, change the input csv file to the csv file of the desired category (here, for example, I used the pfp category and take the first 10 rows, i.e first 10 collections). Note that the input csv file is the output csv file of the repo 'nft-data-engineering-project'

    sample_df = pd.read_csv('sample_data.csv')

3. After you run the script, the data will be store in your data_trading_folder that you set in the config. Also, while running this script, the error, status will be logged to a trading_log.log file for debugging purposes, 

Please note that in order to run this repo, you need an API key which was put in the .env file and this file is not published to the github repo for security purposes. Please contact the owner of this repo to get the .env file or you can create one yourself by creating an account on Dune website.