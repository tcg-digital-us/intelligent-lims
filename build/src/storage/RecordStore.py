import uuid
from flask import Flask
from abc import ABC, abstractmethod

class RecordStoreError(Exception):
    pass

class RecordStoreABC(ABC):

    @abstractmethod 
    def get_record(self, id: str) -> dict:
        pass

    @abstractmethod
    def put_record(self, record: dict) -> uuid:
        pass

from storage.SQLliteStorage import SQLiteDataStore

class RecordStore(object):

    @classmethod
    def initialize(cls, _app: Flask = {}):
        try:
            cls.record_controller = SQLiteDataStore(_app) # <--- To change the datastore, change this to a new datastore implementation
        except Exception as e:
            raise RecordStoreError(str(e))

    @classmethod
    def get_record(cls, id: str) -> dict:
        try:
            record = cls.record_controller.get_record(id)
            return record
        except Exception as e:
            raise RecordStoreError(str(e))
    
    @classmethod
    def put_record(cls, record: dict) -> uuid:
        try:
            response_uuid = cls.record_controller.put_record(record)
            return response_uuid
        except Exception as e:
            raise RecordStoreError(str(e))