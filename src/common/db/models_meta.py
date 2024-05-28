from common.db.base_model import BaseModel

# include models here
from models.users.user import User  # noqa
from models.events import *  # noqa

metadata = BaseModel.metadata
