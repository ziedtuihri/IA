from listservice import app,db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
import json
from listservice.list.models import List

# Init bluebripnt
list = Blueprint('list', __name__)

# Init marshmallow
ma = Marshmallow(list)

# List schema
class ListSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'recurrence', 'created_at', 'device_id')

# Init schema
list_schema = ListSchema()
lists_schema = ListSchema(many=True)

@list.route('/list', methods=['GET'])
def get_all_list():
    all_list =List.query.all()
    result = lists_schema.dump(all_list)
    return jsonify(result.data)
