import re

# Sample documents
documents = {
    "doc1": "Information retrieval systems use Boolean queries to find documents.",
    "doc2": "Boolean retrieval is fundamental to search engines.",
    "doc3": "Modern search engines use advanced algorithms beyond simple Boolean queries.",
    "doc4": "Data mining techniques are used for more complex search tasks.",
    "doc5": "Machine learning improves the accuracy of search engines.",
    "doc6": "Natural language processing is key to understanding search queries.",
    "doc7": "Cloud computing supports large-scale information retrieval systems."
}

# Tokenize documents into sets of words
def tokenize(text):
    return set(re.findall(r'\b\w+\b', text.lower()))

# Index documents
def index_documents(docs):
    index = {}
    for doc_id, text in docs.items():
        index[doc_id] = tokenize(text)
    return index

# Boolean retrieval function
def boolean_retrieval(index, query):
    query = query.lower()
    tokens = re.findall(r'\b\w+\b', query)
    result_docs = set(index.keys())
    
    # Processing the query
    if 'and' in tokens:
        terms = query.split(' and ')
        for term in terms:
            term = term.strip()
            if term:
                result_docs = result_docs.intersection(set(doc_id for doc_id, words in index.items() if term in words))
    elif 'or' in tokens:
        terms = query.split(' or ')
        for term in terms:
            term = term.strip()
            if term:
                result_docs = result_docs.union(set(doc_id for doc_id, words in index.items() if term in words))
    elif 'not' in tokens:
        terms = query.split(' not ')
        if len(terms) == 2:
            term_to_exclude = terms[1].strip()
            result_docs = result_docs.difference(set(doc_id for doc_id, words in index.items() if term_to_exclude in words))
    else:
        result_docs = set(doc_id for doc_id, words in index.items() if any(token in words for token in tokens))
    
    return result_docs

# Index the sample documents
index = index_documents(documents)

# Example queries
while True:
    user_query = input("Enter a Boolean query (or type 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break
    results = boolean_retrieval(index, user_query)
    
    print(f"Query: '{user_query}'")
    if results:
        print("Results:", results)
        print("Documents:")
        for doc_id in results:
            print(f"  {doc_id}: {documents[doc_id]}")
    else:
        print("No documents found.")
    print()
