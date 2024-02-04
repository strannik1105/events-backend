from common.db.base_model import BaseModel

# include models here
from models.events.event import Event  # noqa
from models.events.event_content import EventContent  # noqa

# from models.users.user import User  # noqa

metadata = BaseModel.metadata
