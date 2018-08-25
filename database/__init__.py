from .base import db, BaseModel
from .profile import ProfileModel

db.create_tables([ProfileModel])
