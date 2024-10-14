from app import create_app

app, _ = create_app()

with app.app_context():

    from models import db, user_datastore, Category, Product
    db.drop_all()

    db.create_all()

    # admin_role = Role(name='admin', description='the top level role as per the problem statement')
    # db.session.add(admin_role)
    user_datastore.find_or_create_role(name='admin', description='the top level role as per the problem statement')
    user_datastore.find_or_create_role(name='manager', description='the middle level role as per the problem statement')
    user_datastore.find_or_create_role(name='customer', description='the bottom level role as per the problem statement')

    db.session.commit()

    if not user_datastore.find_user(email="a@abc.com"):
        admin_user = user_datastore.create_user(email="admin@a.com", password="a")
        # admin_user = user_datastore.create_user(email="a@abc.com", password="a", roles=["admin"])
        user_datastore.add_role_to_user(admin_user, "admin")
        # role = user_datastore.find_role("admin")
        # user_datastore.add_role_to_user(admin_user, role)
    
    if not user_datastore.find_user(email='manager@a.com'):
        user = user_datastore.create_user(email='manager@a.com', password='manager')
        user_datastore.add_role_to_user(user, 'manager')
        user_datastore.add_role_to_user(user, 'customer')
        print("Created manager user")

    if not user_datastore.find_user(email='customer@a.com'):
        user = user_datastore.create_user(email='customer@a.com', password='customer')
        user_datastore.add_role_to_user(user, 'customer')
        print("Created customer user")
    
    db.session.commit()

    # dummy users
    admin_user = user_datastore.find_user(email='admin@a.com')
    manager_user = user_datastore.find_user(email='manager@a.com')
    customer_user = user_datastore.find_user(email='customer@a.com')

    # Create categories
    category1 = Category(name='Fruits', description='Fresh Fruits', status=True, created_by=admin_user.id)
    category2 = Category(name='Vegetables', description='Green Vegetables', status=True, created_by=admin_user.id)
    db.session.add(category1)
    db.session.add(category2)
    db.session.commit()
    print("Created categories")

    # Create products
    product1 = Product(name='Apple', description='Fresh Red Apples', price=100.0, stock=50, category_id=category1.id, created_by=manager_user.id)
    product2 = Product(name='Banana', description='Ripe Yellow Bananas', price=50.0, stock=100, category_id=category1.id, created_by=manager_user.id)
    product3 = Product(name='Carrot', description='Organic Carrots', price=30.0, stock=200, category_id=category2.id, created_by=manager_user.id)
    product4 = Product(name='Spinach', description='Fresh Spinach', price=25.0, stock=150, category_id=category2.id, created_by=manager_user.id)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.commit()
    print("Created products")
