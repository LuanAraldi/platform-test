import json

def format_product(productId, images):
    return {
        'productId': productId,
        'images': images
    }

def aggregate(dump):
    dump_out = open(dump, 'r')
    products = {}
    for line in dump_out:
        product = json.loads(line)
        productId = product.get('productId', None)
        if products.get(productId):
            products[productId].append(product.get('image'))
        else:
            products[productId] = [product.get('image')]

    final_dump = open('./aggregator.json', 'w+')
    for product in map(format_product, products.keys(), products.values()):
        final_dump.write(json.dumps(product) + '\n')
