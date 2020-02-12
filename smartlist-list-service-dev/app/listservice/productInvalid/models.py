from listservice import db

class ProductInvalid(db.Model):
    idProductInvalid = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(200))
    marque = db.Column(db.String(200))
    price = db.Column(db.Double)
    list_id = db.Column(db.Integer, db.ForeignKey('list.idList'), nullable=False)

    def __init__(self, designation, list_id, price, marque):
        self.designation = designation
        self.list_id = list_id
        self.price = price
        self.marque = marque


    def __repr__(self):
        return '<ProductInvalid %r>' % self.designation

db.create_all() # In case user table doesn't exists already. Else remove it
