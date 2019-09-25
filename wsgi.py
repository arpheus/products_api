# wsgi.py

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

class Counter:
    def __init__(self, init_id):
        self.id = init_id

    def next(self):
        self.id += 1
        return self.id

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'LaGrosseRadio.tv' },
    { 'id': 4, 'name': 'LaGrosseRadio.tv' }
]

id_factory = Counter(len(PRODUCTS))

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def getProducts():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:post_id>')
def getProduct(post_id):

    index_products = len(PRODUCTS)
    index=0

    if post_id <= index_products:
        while index < index_products :
                PRODUCT = PRODUCTS[int(index)]
                index += 1
                if PRODUCT['id'] == post_id:
                    #print(PRODUCT)
                    return jsonify(PRODUCT)
    else:
        PRODUCT = {}
        abort (404)

@app.route('/api/v1/products', methods=['POST'])
def createProduct():
    payload = request.get_json(silent=True,force=True)
    pdb.set_trace()
    if payload != None and type(payload) is dict and "name" in list(payload):
        #generate new id
        new_id = id_factory.next()
        PRODUCTS.append({'id': new_id, 'name': payload["name"]})
        for product in PRODUCTS:
            if product['id'] == new_id:
                return jsonify(product), 201
        #reaching this should trigger an error, cannot find the element we just created
    else:
        abort(422)
