from flask import Flask
from flask_bootstrap import Bootstrap
from flask_qiniustorage import Qiniu
from flask_admin import Admin

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('localConfig.py')

bootstrap = Bootstrap(app)
qiniu_store = Qiniu(app)
admin = Admin(app)
QINIU_DOMAIN = app.config.get('QINIU_BUCKET_DOMAIN', '')
CATEGORY = app.config.get('CATEGORY')
UPLOAD_URL = app.config.get('UPLOAD_URL')


