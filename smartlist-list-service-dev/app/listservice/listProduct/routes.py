from listservice import app,db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
import json
from listservice.listProduct.models import ListProduct

# Init bluebripnt
listProduct = Blueprint('listProduct', __name__)

# Init marshmallow
ma = Marshmallow(listProduct)

# TestClass schema
class ListProductSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'barcode', 'qrcode', 'list_id')

# Init schema
listProduct_schema = ListProductSchema()
listsProduct_schema = ListProductSchema(many=True)

@listProduct.route('/listProduct', methods=['GET'])
def get_list_Products():
    all_list_of_products =ListProduct.query.all()
    result = listsProduct_schema.dump(all_list_of_products)
    return jsonify(result.data)
