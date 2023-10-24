from elasticsearch import Elasticsearch
import configparser
import queries

config = configparser.ConfigParser()
config.read('config.ini')

es = Elasticsearch([{'host': config['ELASTIC']['HOST'], 'port': config['ELASTIC']['PORT']}])

INDEX = 'metaphorquest'


def search(search_text,search_type):        
    if(search_type == "poem_only"):
        query_body = queries.single_phrase_match(search_text, "poem_name")
        
    if(search_type == "metaphors_only"):
        query_body = queries.single_phrase_match(search_text, "metaphorical_terms", "match_phrase")
        
    if(search_type == "authors_only"):
        query_body = queries.single_phrase_match(search_text, "poet")
        
    if(search_type == "meaning_only"):
        query_body = queries.single_phrase_match(search_text, "meaning")

    if(search_type == "all"):
        query_body = queries.multi_match(search_text, ["poem_name","poet","line","metaphorical_terms", "meaning"])
   

    res = es.search(index=INDEX, body=query_body) # Calling the elastic search client with the corresponding query body
    return res