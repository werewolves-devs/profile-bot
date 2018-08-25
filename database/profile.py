from typing import Union

from discord import User, Member
from peewee import BigIntegerField, IntegerField, CharField

from .base import BaseModel


class ProfileModel(BaseModel):
    uid = BigIntegerField(primary_key=True)
    age = IntegerField(default=0)
    bio = CharField(max_length=2012, default="None")
    gender = CharField(max_length=255, default="Undefined")

    @classmethod
    def get_or_insert(cls, user: Union[User, Member, int]) -> 'ProfileModel':
        if hasattr(user, 'id'):
            user = user.id
        model, created = cls.get_or_create(uid=user)
        if created:
            model.save()
        return model
