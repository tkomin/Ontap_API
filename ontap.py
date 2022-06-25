import requests


r1 = requests.get('https://ontap_ip/api/network/ethernet/ports', auth=('admin', ''),
                 verify=False)

print(r1.text)


r2 = requests.get('https://ontap_ip/api/network/ip/interfaces', auth=('admin', ''),
                 verify=False)

print(r2.text)


r3 = requests.get('https://ontap_ip/api/svm/svms', auth=('admin', ''),
                 verify=False)

print(r3.text)


r4 = requests.get('https://ontap_ip/api/protocols/cifs/shares', auth=('admin', ''),
                 verify=False)

print(r4.text)




