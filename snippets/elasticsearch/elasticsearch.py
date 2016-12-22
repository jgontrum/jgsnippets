from elasticsearch import helpers
from elasticsearch.exceptions import NotFoundError


def query(es, query=None, index=None, doc_type=None):
    rs = es.search(body=query, index=index, doc_type=doc_type)
    rs = rs or {}
    hits = rs.get("hits", {}).get("hits", [])
    for hit in list(hits):
        ret = hit.get("_source", {})
        ret['_id'] = hit.get("_id", "_UNKNOWNid__")
        ret['_score'] = hit.get("_score", -1)
        yield ret


def find(es, query=None, index=None, doc_type=None, scroll='60s', size=100,
         raw=False):
    rs = helpers.scan(es, index=index, doc_type=doc_type, scroll=scroll,
                      size=size, query=query)

    for doc in rs:
        if raw:
            yield doc
        else:
            ret = doc.get("_source", {})
            ret['id_'] = doc.get("id_", "_UNKNOWNid__")
            yield ret


def insert(es, id_, query, index, doc_type):
    rs = es.index(index, doc_type, query, id=id_)
    rs = rs or {}
    return rs.get("result") == 'created'


def reindex(es, id_, query, index, doc_type):
    rs = es.index(index, doc_type, query, id=id_)
    rs = rs or {}
    return rs.get("result") == 'updated'


def update(es, id_, query, index, doc_type):
    rs = es.update(index, doc_type, id_, query)
    return rs.get("result") == 'updated'


def get_by_id(es, id_, index, doc_type):
    try:
        print(id_, index, doc_type)
        rs = es.get(index, id_, doc_type)
        rs = rs or {}
    except NotFoundError:
        return {}
    return rs.get("_source", {})


def count(es, query, index, doc_type):
    rs = es.count(index=index, doc_type=doc_type, body=query)
    rs = rs or {}
    return rs.get("count", 0)