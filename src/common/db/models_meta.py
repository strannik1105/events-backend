from common.db.base import SQLAlchemyBaseModel
from events.models.event import EventModel  # noqa
from events.models.event_type import EventTypeModel # noqa
from events.models.event_content_type import EventContentTypeModel # noqa

metadata = SQLAlchemyBaseModel.metadata
