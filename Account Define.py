# First Python script with dependencies on Git!

import requests, json, os
from datetime import datetime
start = datetime.now()

with open(os.path.expanduser("~") + r'/testconfig.json') as json_data_file:
    configuration = json.load(json_data_file)
    access_token = configuration["canvas"]["access_token"]
    baseUrl = "https://"+configuration["canvas"]["host"] + "/api/v1/"
header = {'Authorization' : 'Bearer ' + access_token}
#############################

def accountname(account_id):

    url = baseUrl + 'accounts/%s' % (account_id)
    ar = requests.get(url, headers=header)
    if ar.status_code == requests.codes.ok:
        data = ar.json()
        account_name = data['name']
        print('Account name: ' + account_name)

    return account_name

def main():

    account_id = 39
    print('\n')
    account_name = accountname(account_id)

if __name__ == "__main__": main()

end = datetime.now()
total_time = end - start
print("Running Time:", total_time)