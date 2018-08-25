from peewee import SqliteDatabase, Model

db = SqliteDatabase('profiles.db')


class BaseModel(Model):
    class Meta:
        database = db
