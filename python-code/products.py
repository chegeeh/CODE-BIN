
from __main__ import app,db,ma,request,pprint,json,my_util,users,sqlalchemy
from users import User
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
import uuid
from my_util import GUID


class Product(db.Model):
    productId = db.Column(GUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable = False)
    img_url = db.Column(db.String(1000))
    price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    desc = db.Column(db.String(3000), nullable = True)
    img_data = db.Column(db.LargeBinary,nullable = True) # I rather just use a storage service and place the url here

    def __init__(self,title,img_url,price,quantity,desc,img_data):
        self.title = title
        self.img_url = img_url
        self.price = price
        self.quantity = quantity
        self.desc = desc
        self.img_data = img_data


    def  any(self):
        return '<product %r>' % self.title

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('title','img_url','price','quantity','desc','img_data')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/product/create',methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
    	product_content= request.json['Product']
    	new_product = Product(product_content)

    	try:
			db.session.add(new_product)
			db.session.commit()

			return redirect ('/product/read')

		except: 
			return "there was an issue creating your product!"

	else:

		return render_template("/product/read", product_content=product_content)



#i made an assumption here that we are trying to read data of one particular product and not all
@app.route('/product/read/<int:productId>',methods=['POST', 'GET'])
def read_product(productId):
	product_read = Product.query.get_or_404(productId)
	for product in product_read:
		print(product)


@app.route('/product/update/<int:productId>',methods=['POST', 'GET'])
def update_product(productId):
    product_to_update = Product.query.get_or_404(productId)
    if request.method == 'POST': 
		product = request.json['Product']

		try: 
			db.session.commit()
			return redirect('/')
		except:
			return 'there was an error updating your task'  
	else:
		return render_template('update.html', product_to_update=product_to_update)
	



@app.route('/product/delete/<int:productId>') #alternatively you could use the uuid
def delete_product(productId):
	product_to_delete = Product.query.get_or_404(productId)

	try:
		db.session.delete(product_to_delete)
		db.session.commit()

		return redirect('/product/list')

	except:
		return "couldn't delete because there was an error"	

@app.route('/product/list',methods=['POST'])
def list_products():
	product_list = Product.query.all()
	for x in product_list:
		print(x)
