from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import url_for, redirect, request, abort
from orm import Clients, Role
from flask_login import current_user
import flask_login as login
from flask_security import SQLAlchemyUserDatastore, Security
import flask_admin
from flask_admin import helpers, expose
from flask_admin.contrib import sqla


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orm_db.db'
db = SQLAlchemy(app)
user_datastore = SQLAlchemyUserDatastore(db, Clients, Role)
security = Security(app, user_datastore)

class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('admin')
                )

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('security.login', next=request.url))

class MyAdminIndexView(flask_admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_page'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_page(self):
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_page(self):
        login.logout_user()
        return redirect(url_for('.index'))

    @expose('/reset/')
    def reset_page(self):
        return redirect(url_for('.index'))

admin = flask_admin.Admin(app, index_view = MyAdminIndexView(), base_template = 'admin/master-extended.html')
admin.add_view(MyModelView(Clients, db.session))

@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        h = helpers,
        get_url = url_for
    )

admin_bp = Blueprint('admin_blueprint', __name__)
app.register_blueprint(admin_bp, url_prefix="/admin")