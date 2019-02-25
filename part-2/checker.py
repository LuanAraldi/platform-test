import json
import requests
import concurrent.futures

def image_exists(product):
    product = json.loads(product)
    existing_images = []
    for image in product.get('images'):
        if requests.get(image).status_code == 200:
            existing_images.append(image)
        if len(existing_images) >= 3:
            break
    
    product['images'] = existing_images
    return product

def check(dump):
    dump_out = open('./dump.json', 'w+')
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        future_to_url = {executor.submit(image_exists, prd): prd for prd in open(dump, 'r')}
        for future in concurrent.futures.as_completed(future_to_url):
            product = future.result()
            dump_out.write(json.dumps(product) + '\n')