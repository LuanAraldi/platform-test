import json
import requests
import concurrent.futures

def image_exists(product):
    if requests.get(json.loads(product).get('image')).status_code == 200:
        return (True, product)
    return (False, product)

def check(dump):
    dump_out = open('./dump_out', 'w+')
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(image_exists, prd): prd for prd in open(dump, 'r')}
        for future in concurrent.futures.as_completed(future_to_url):
            result = future.result()
            if result[0]:
                dump_out.write(result[1])