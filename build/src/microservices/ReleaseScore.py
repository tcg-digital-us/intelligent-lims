import json
import requests
from Config import base_urls, ConfigGetError
from storage.RecordStore import RecordStore, RecordStoreError

class ReleaseScoreError(Exception):
    pass

class ReleaseScore(object):
    @staticmethod
    def get(_content):
        try:
            base_urls_list = base_urls()
            lv_release_score_url = base_urls_list['lv_release_score']
        except ConfigGetError as e:
            print(str(e))
            raise ReleaseScoreError("Could not connect to releaseScore microservice")
        except KeyError as e:
            print(f'key {str(e)} could not be found in the config')
            raise ReleaseScoreError("Could not connect to releaseScore microservice")

        try:
            response = requests.post(f'{lv_release_score_url}/releaseScore', json=_content)
        except Exception as e:
            print(str(e))
            raise ReleaseScoreError("The releaseScore microservice at the given address did not respond")
        print(response.json())
        if response.status_code < 200 or response.status_code >= 300: raise ReleaseScoreError("The releaseScore microservice indicated failure")

        try:
            response_record = { "content": _content, "result": response.json() }
            transaction_id = RecordStore.put_record(response_record)
        except RecordStoreError as e:
            raise ReleaseScoreError(str(e))
        
        result = response.json()
        result["transaction_id"] = transaction_id
        return result
