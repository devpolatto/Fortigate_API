from config_api import get_requeste_cmdb

get_interfaces = get_requeste_cmdb({
    'host': '',
    'endpoint': 'system/interface',
    'token': ''
})

interfaces = get_interfaces['results']

# print(data.headers)
for item in interfaces:
    print('interface: ',item['name'])
