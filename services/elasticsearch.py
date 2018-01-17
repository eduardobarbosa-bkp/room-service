from elasticsearch import Elasticsearch

from elastic_factory import ElasticSearchFactory


class ElasticSearchIndex(object):
    def __init__(
            self,
            elastic_factory: ElasticSearchFactory,
            index_name: str,
            doc_type: str,
            index_mapper: dict
    ):
        self.index_name = index_name
        self.index_mapper = index_mapper
        self.doc_type = doc_type
        self.elastic_factory = elastic_factory
        self.instance = None

    def connection(self) -> Elasticsearch:
        if not self.instance:
            self.instance = self.elastic_factory.create()

            if not self.instance.indices.exists(self.index_name):
                self.instance.indices.create(
                    index=self.index_name
                    ,body=self.index_mapper
                )

        return self.instance

    def index(self, payload: dict) -> bool:
        return self.connection().index(
            index=self.index_name
            ,doc_type=self.doc_type
            ,body=payload
        )

    def exists_by_url(self, url: str) -> bool:
        matches = self.connection().search(
            index=self.index_name
            ,doc_type=self.doc_type
            ,body={
                "query": {
                    "query_string": {
                        "query": 'url:"{}"'.format(url)
                    }
                }
            }
        )

        hits = matches['hits']['hits']

        if hits:
            return True

        return False

    def delete(self, _id: str) -> bool:
        result = self.connection().delete_by_query(
            index=self.index_name
            ,doc_type=self.doc_type
            ,body={
                "query": {
                    "query_string": {
                        "query": 'id:"{}"'.format(_id)
                    }
                }
            }
        )

        deleted = result['deleted']

        if deleted > 0:
            return True
        return False

    def get(self, _id: str) -> dict:
        matches = self.connection().search(
            index=self.index_name
            ,doc_type=self.doc_type
            ,body={
                "query": {
                    "query_string": {
                        "query": 'id:"{}"'.format(_id)
                    }
                }
            }
        )

        hits = matches['hits']['hits']

        if hits:
            return hits[0]['_source']

        return None

    def list(self) -> list:
        matches = self.connection().search(
            index=self.index_name,
            doc_type=self.doc_type,
            body={
                "query": {
                    "match_all": {}
                }
            }
        )

        data = [doc for doc in matches['hits']['hits']]

        return [doc['_source'] for doc in data]