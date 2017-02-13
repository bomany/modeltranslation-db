from django.db.backends.mysql.base import \
    DatabaseWrapper as MySQLDatabaseWrapper

from .creation import TranslationMySQLCreation
from django.contrib.gis.db.backends.mysql.features import DatabaseFeatures
from django.contrib.gis.db.backends.mysql.introspection import MySQLIntrospection
from django.contrib.gis.db.backends.mysql.operations import MySQLOperations
from django.contrib.gis.db.backends.mysql.schema import MySQLGISSchemaEditor


class DatabaseWrapper(MySQLDatabaseWrapper):
    SchemaEditorClass = MySQLGISSchemaEditor

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DatabaseFeatures(self)
        self.creation = TranslationMySQLCreation(self)
        self.ops = MySQLOperations(self)
        self.introspection = MySQLIntrospection(self)
