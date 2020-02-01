from aifc import Error

import requests
import json


def main(gcp_request):
    gcp_request_json = gcp_request.get_json()
    if gcp_request_json and 'barcode' in gcp_request_json:
        current_barcode = gcp_request_json['barcode']
        print(current_barcode)
    resp = requests.get('https://world.openfoodfacts.org/api/v0/product/' +
                        current_barcode + '.json')
    if (resp.status_code != 200) or (resp.status_code == 404):
        # smth went wrong
        raise Error('Get request error '.format(resp.status_code))
    else:
        res = beautifyprint(resp.json())
        return res


def beautifyprint(obj):
    # create a formatted string
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
