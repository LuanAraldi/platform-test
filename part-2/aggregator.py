import json
import tarfile
import codecs

utf8reader = codecs.getreader('utf-8')

def format_product(productId, images):
    return {
        'productId': productId,
        'images': images
    }

def aggregate(dump):
    print(dump)
    tar = tarfile.open(dump,encoding='utf-8')
    extracted_tar = tar.extractfile(tar.getmembers()[0])
    dump_extracted = open('extracted.json', 'w+').write(utf8reader(extracted_tar).read())
    
    products = {}
    #print(extracted_tar.read())
    for line in open('extracted.json'):
        product = json.loads(line)
        productId = product.get('productId', None)
        if products.get(productId):
            products[productId].append(product.get('image'))
        else:
            products[productId] = [product.get('image')]

    final_dump = open('./aggregator.json', 'w+')
    for product in map(format_product, products.keys(), products.values()):
        final_dump.write(json.dumps(product) + '\n')
