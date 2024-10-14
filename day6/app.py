from flask import render_template, request  # pip install flask

from flask_security import auth_required, auth_token_required, roles_accepted, roles_required, current_user

from models import db, user_datastore, mad1

def create_app():
    from flask import Flask
    init_app = Flask(__name__)

    from config import LocalDev
    init_app.config.from_object(LocalDev)

    # db = SQLAlchemy(app)
    db.init_app(init_app)

    from flask_security import Security # pip install flask_security
    security = Security(init_app, user_datastore)

    from flask_restful import Api
    init_api = Api(init_app)

    from flask_cors import CORS
    CORS(init_app)

    return init_app, init_api

app, api = create_app()

@app.route('/test', methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        data = request.form.get('name')
        print(data)
        from models import mad1
        new_data = mad1(name=data)
        db.session.add(new_data)
        db.session.commit()
        return "success"
    var1 = 'this is coming from the backend'
    return render_template('test.html', var2=var1)

from routes.auth import register, login, switchuser
api.add_resource(register, '/signup')
api.add_resource(login, '/signin')
api.add_resource(switchuser, '/switchuser')

from routes.test import test, version2
api.add_resource(test, '/api/test')
api.add_resource(version2, '/api/version2')


from routes.category import CategoryResource, CategorySpecific, newCategorySpecific
api.add_resource(CategoryResource, '/api/category')
api.add_resource(CategorySpecific, '/api/category/<int:id>')
api.add_resource(newCategorySpecific, '/api/newcategory')

# get is to send data from backend to frontend  /  whenever we hit a url in the browser, it is a get request
# post is to send data from frontend to backend
# put is to update data in the backend from frontend  / patch is similar to put
# delete is to delete data in the backend


if __name__ == '__main__':
    app.run()