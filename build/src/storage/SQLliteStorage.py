import os, uuid, json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from storage.RecordStore import RecordStoreABC

class SQLiteStoreError(Exception):
    pass

class SQLiteDataStore(RecordStoreABC):

    def __init__(self, _app: Flask):
        self.db = self.init_db(_app)
        self.Cache = self.create_cache_model(self.db)  # Create the Cache model with the given db
        self.db.create_all()  # Create the tables after initializing the db

    def init_db(self, _app: Flask):
        try:
            main_file_path = os.path.abspath(os.path.dirname(__file__))
            instance_folder_path = os.path.join(main_file_path, 'instance')
            os.makedirs(instance_folder_path, exist_ok=True)
            db_file_path = os.path.join(instance_folder_path, 'mydb.sqlite3')
            _app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file_path}'
            _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            sqlite = SQLAlchemy(_app)
            return sqlite
        except Exception as e:
            raise SQLiteStoreError(f"Error occured while trying to initialize datastorage connection: {e}")

    # Define a function to create the Cache model with the given db
    def create_cache_model(self, db):
        class Cache(db.Model):
            transaction_id = db.Column(db.String(36), primary_key=True)
            data = db.Column(db.String, nullable=False)

            def __repr__(self):
                return f"<Transaction {self.transaction_id}>"

        return Cache

    def get_record(self, id: str) -> dict:
        try:
            cache_entry = self.Cache.query.filter_by(transaction_id=id).first()
            if cache_entry:
                return json.loads(cache_entry.data)
            else:
                raise SQLiteStoreError(f"Transaction ID {id} not found")
        except Exception as e:
            raise SQLiteStoreError(f"An error occured while trying to get data: {e}")

    def put_record(self, record: dict) -> uuid:
        try:
            # The record isn't being validated before being saved.
        
            transaction_id = str(uuid.uuid4())
            record['transaction_id'] = transaction_id

            cache_entry = self.Cache(transaction_id=transaction_id, data=json.dumps(record))
            self.db.session.add(cache_entry)
            self.db.session.commit()
            return transaction_id
        except Exception as e:
            raise SQLiteStoreError(f"An error occured while trying to save data: {e}")
