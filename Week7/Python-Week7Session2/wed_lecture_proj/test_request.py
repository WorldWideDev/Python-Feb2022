import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
headers = {
    'TRN-api-key': 'd717a54c-5dea-4d9a-bbec-b458d29e8ec6'
}
r = requests.get('https://api.fortnitetracker.com/v1/store', headers=headers)
print(r.json())