# tests/test_views.py
from flask_testing import TestCase
from flask import request
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_read_products_json(self):
        id = 2
        response = self.client.get(f"/api/v1/products/{id}")
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'],id)
        id = 99
        response = self.client.get(f"/api/v1/products/{id}")
        self.assertEqual(response.status,"404 NOT FOUND")

    def test_create_products(self):
        response = self.client.post(path='/api/v1/products',json={"name": "toto"})
        json = response.json
        #test the return code, should be 201 CREATED
        self.assertEqual(response.status, "201 CREATED")
        self.assertIsInstance(json, dict)
        #test the returned object, should be a product with id and name
        self.assertEqual(["id","name"],list(json))

    def test_create_fails_if_no_name_provided(self):
        response = self.client.post(path='/api/v1/products',json={})
        json = response.json
        #test the return code, should be 422 UNPROCESSABLE ENTITY
        self.assertEqual(response.status, "422 UNPROCESSABLE ENTITY")
        #test the returned object, should be None
        self.assertEqual(json, None)
