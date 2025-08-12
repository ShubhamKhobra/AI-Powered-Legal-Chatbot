from src.generator import generator_response

def pipeline(query):
    # Generate a response based on the query
    response = generator_response(query)
    return response
