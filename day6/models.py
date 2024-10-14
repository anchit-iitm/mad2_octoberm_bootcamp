from flask_sqlalchemy import SQLAlchemy # pip install flask_sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.mutable import MutableList

from flask_security import AsaList, UserMixin, RoleMixin, SQLAlchemyUserDatastore # pip install flask_security

from datetime import datetime

db = SQLAlchemy()

class mad1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    name1 = db.Column(db.String(100))

class mad2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255)) #

    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True) #

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  # required

    email = Column(String(255), unique=True)  # required
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)  # required

    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)

    active = Column(Boolean())  # required
    fs_uniquifier = Column(String(64), unique=True, nullable=False)  # required

    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))  # required
    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean)
    created_by = db.Column(db.String(255), db.ForeignKey('user.id'))
    updated_by = db.Column(db.String(255), db.ForeignKey('user.id'), default=None)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    delete = db.Column(db.Boolean, default=False)
    products = db.relationship('Product', back_populates='category', lazy=True) # not a requirement, totaly upto you how you want to implement

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'created_by': self.created_by,
            'updated_by': self.updated_by,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'delete': self.delete,
            'products': [product.serialize() for product in self.products] if self.products else 'No products found' # not a requirement
        }
    
    def get_all():
        categories = Category.query.all()
        return categories

    def admin_delete(id):
        category = Category.query.filter_by(id=id).first()
        if not category:
            return "No category found by that id", False
        # delete category row with sql
        db.session.delete(category)
        db.session.commit()
        return "Category deleted successfully", True

def admin_delete_diff_scope(id):
    category = Category.query.filter_by(id=id).first()
    if not category:
        return "No category found by that id", False
    # delete category row with sql
    db.session.delete(category)
    db.session.commit()
    return "Category deleted successfully", True


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    status = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.String(255), db.ForeignKey('user.id'))
    updated_by = db.Column(db.String(255), db.ForeignKey('user.id'), default=None)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    delete = db.Column(db.Boolean, default=False)
    category = db.relationship('Category', back_populates='products', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'status': self.status,
            'category_id': self.category_id,
            'created_by': self.created_by,
            'updated_by': self.updated_by,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'delete': self.delete
        }
    
    def admin_delete(id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return "No product found by that id", False
        # delete product row with sql
        db.session.delete(product)
        db.session.commit()
        return "Product deleted successfully", True