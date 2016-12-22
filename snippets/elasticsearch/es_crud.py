from elasticsearch import Elasticsearch
from snippets.elasticsearch.elasticsearch import elasticsearch
import uuid


class ElasticsearchCrud(object):

    def __init__(self, index, doc_type=None, hosts=[]):
        self.index = index
        self.doc_type = doc_type
        self.es = Elasticsearch(hosts)
        self.es.count()

    def find_one(self, query):
        for hit in elasticsearch.query(
                self.es, query, self.index, self.doc_type):
            return hit
        return {}

    def get(self, id_):
        return elasticsearch.get_by_id(self.es, id_, self.index, self.doc_type)

    def cursor(self, query):
        for result in elasticsearch.find(
                self.es, query, self.index, self.doc_type):
            yield result

    def find(self, query):
        for hit in elasticsearch.query(
                self.es, query, self.index, self.doc_type):
            yield hit

    def reindex(self, id_, document):
        return elasticsearch.reindex(
            self.es, id_, document, self.index, self.doc_type)

    def update(self, id_, document):
        return elasticsearch.update(
            self.es, id_, document, self.index, self.doc_type)

    def insert(self, document, id_=None, id_field=None):
        assert self.doc_type
        if not id_:
            id_ = uuid.uuid4()
        if id_field:
            document[id_field] = str(id_)

        if elasticsearch.insert(
                self.es, id_, document, self.index, self.doc_type):
            return id_
        return False

    def count(self, document):
        return elasticsearch.count(self.es, document, self.index, self.doc_type)

