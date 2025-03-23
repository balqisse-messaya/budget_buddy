from CRUD.crud_user import *
from CRUD.crud_transaction import *

user_id = login_user()
if user_id is not None :
    deposit(user_id)