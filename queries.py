import json


def single_phrase_match(query,field, type="match"):
    print(query, field)
    q = {
        "size": 15,
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
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                # "fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "sinhala_singer.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "sinhala_composer.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "sinhala_lyricist.keyword",
					"size": 10
				}
			}
		}
	}

    q = json.dumps(q)
    return q

def multi_phrase_match(query,field):
    operator = 'and'
    q = {
        "size": 200,
        "explain": True,
        "query": {
            "match_phrase": {
				field: {
					"query" : query,
					"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
					"operator": operator,
					"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
					"fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
					"lenient": False, # Avoid data type similarity requirement
					"prefix_length": 0, 
					"max_expansions": 50,
					"auto_generate_synonyms_phrase_query": True,
					"zero_terms_query": "none"
				}
			}
		},
	}
    q = json.dumps(q)
    return q

def single_field_full_match(query,field):
		operator = 'and'
		q = {
			"size": 200,
			"explain": True,
			"query": {
				"match": {
					field: {
						"query" : query,
						"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
						"operator": operator,
						"analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
						"fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
						"fuzzy_transpositions": True, # Allow character swaps
						"lenient": False, # Avoid data type similarity requirement
						"prefix_length": 0, 
						"max_expansions": 50,
						"auto_generate_synonyms_phrase_query": True,
						"zero_terms_query": "none"
					}
				}
			},
			"aggs": {
				"Singer Filter": {
					"terms": {
						"field": "sinhala_singer.keyword",
						"size": 10
					}
				},
				"Composer Filter": {
					"terms": {
						"field": "sinhala_composer.keyword",
						"size": 10
					}
				},
				"Lyricist Filter": {
					"terms": {
						"field": "sinhala_lyricist.keyword",
						"size": 10
					}
				}
			}
		}

		q = json.dumps(q)
		return q



def fuzzy_multi_match(query, fields, operator ='or'):
	q = {
		"size": 200,
		"explain": True,
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": operator,
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "sinhala_singer.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "sinhala_composer.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "sinhala_lyricist.keyword",
					"size": 10
				}
			}
		}
	}

	q = json.dumps(q)
	return q


def sorted_fuzzy_multi_match(query, sort_num, fields, operator ='or'):
	print ('sort num is ',sort_num)
	q = {
		"size": sort_num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields", # best_fields, most_fields, cross-fields, phrase, phrase_prefix try all
                "operator": "or",
                #"minimum_should_match": 2, # How many terms must be included to match if the operator is or
                "analyzer": "standard", # standard, simple, whitespace, stop, keyword, pattern, <language>, fingerprint
                "fuzziness": "AUTO", # The number of character edits (insert, delete, substitute) to get the required term
                "fuzzy_transpositions": True, # Allow character swaps
                "lenient": False, # Avoid data type similarity requirement
                "prefix_length": 0, 
                "max_expansions": 50,
                "auto_generate_synonyms_phrase_query": True,
                "zero_terms_query": "none"
			}
		},
		"aggs": {
			"Singer Filter": {
				"terms": {
					"field": "sinhala_singer.keyword",
					"size": 10
				}
			},
			"Composer Filter": {
				"terms": {
					"field": "sinhala_composer.keyword",
					"size": 10
				}
			},
			"Lyricist Filter": {
				"terms": {
					"field": "sinhala_lyricist.keyword",
					"size": 10
				}
			}
		}
	}
	q = json.dumps(q)
	return q

