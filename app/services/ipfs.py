# IPFS service
import requests

class IPFS:
    @staticmethod
    def add(file):
        response = requests.post(IPFS_NODE_URL + '/api/v0/add', files={'file': file})
        return response.json()['Hash']

    @staticmethod
    def get(ipfs_hash):
        response = requests.get(IPFS_NODE_URL + '/api/v0/get', params={'arg': ipfs_hash})
        return response.content
