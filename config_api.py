import requests
import urllib3


def get_requeste_cmdb(params: dict):

    api_url = 'http://{}/api/v2/cmdb/{}?access_token={}'.format(params['host'],params['endpoint'], params['token'])

    urllib3.disable_warnings()

    data = requests.get(api_url, verify=False).json()

    return data

