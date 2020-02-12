from listservice import app,db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
import json
from listservice.listShared.models import ListShared

# Init bluebripnt
listShared = Blueprint('listShared', __name__)

# Init marshmallow
ma = Marshmallow(listShared)

# TestClass schema
class ListSharedSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('emailUser', 'list_id', 'group_id', 'shared_at', 'permission')

# Init schema
listShared_schema = ListSharedSchema()
listsShared_schema = ListSharedSchema(many=True)

@listShared.route('/listShared', methods=['GET'])
def get_list_Shared():
    all_shared_list =ListShared.query.all()
    result = listsShared_schema.dump(all_shared_list)
    return jsonify(result.data)
