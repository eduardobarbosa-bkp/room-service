import uuid

from flask_injector import inject

from services.elasticsearch import ElasticSearchIndex


class Room(object):
    @inject
    def post(self, indexer: ElasticSearchIndex, room: dict) -> dict:
        """
        This wil return a location, kind of 'Camden, London'.
        We need to have some data like lat/lon for that input.
        """
        if indexer.exists_by_url(room['url']):
            # 409 HTTP Conflict
            return room, 409

        # Generates a unique ID for the room
        room['id'] = str(uuid.uuid4())

        if not indexer.index(room):
            return {"error": "Room not saved"}, 400

        return room, 201

    @inject
    def delete(self, indexer: ElasticSearchIndex, _id: str) -> dict:
        if not indexer.delete(_id):
            return {"error": "Room not removed"}, 400
        return None, 200

    @inject
    def get(self, indexer: ElasticSearchIndex, _id: str) -> list:
        return indexer.get(_id), 200

    @inject
    def list(self, indexer: ElasticSearchIndex) -> list:
        return indexer.list(), 200


class_instance = Room()
