import json

def single_phrase_match(query,field, type="match"):
    print(query, field)
    q = {
        "size": 200,
        # "explain": True,
        "query": {
            "bool": {
          		"should": [
					{
					type: { field : query }
					}
				]
        	}
        },
        "aggs": {
            "Metaphor count filter": {
                "terms": {
                    "field": "count",
                    "size": 10
                }
            },
            "Metaphor present filter": {
                "terms": {
                    "field": "metaphor_present",
                    "size": 10
                }
            }
        }
    }
    q = json.dumps(q)	
    return q

def multi_match(query, fields, operator ='or'):
    print(query, fields)
    q = {
		"size": 200,
		"explain": True,
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "phrase", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": operator,
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
            "Metaphor count filter": {
                "terms": {
                    "field": "count",
                    "size": 10
                }
            },
            "Metaphor present filter": {
                "terms": {
                    "field": "metaphor_present",
                    "size": 10
                }
            }
        }
	}
    q = json.dumps(q)
    return q


