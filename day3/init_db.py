from app import create_app

app = create_app()

with app.app_context():

    from models import db, user_datastore
    db.drop_all()

    db.create_all()

    # admin_role = Role(name='admin', description='the top level role as per the problem statement')
    # db.session.add(admin_role)
    user_datastore.find_or_create_role(name='admin', description='the top level role as per the problem statement')
    user_datastore.find_or_create_role(name='manager', description='the middle level role as per the problem statement')
    user_datastore.find_or_create_role(name='customer', description='the bottom level role as per the problem statement')

    db.session.commit()

    if not user_datastore.find_user(email="a@abc.com"):
        admin_user = user_datastore.create_user(email="a@abc.com", password="a")
        # admin_user = user_datastore.create_user(email="a@abc.com", password="a", roles=["admin"])
        user_datastore.add_role_to_user(admin_user, "admin")
        # role = user_datastore.find_role("admin")
        # user_datastore.add_role_to_user(admin_user, role)
        
        db.session.commit()
