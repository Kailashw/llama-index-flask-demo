import os
import json

from flask import Flask, render_template, request, jsonify, make_response
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.indices.service_context import ServiceContext
from llama_index.llms import OpenAI
from llama_index.indices.struct_store import JSONQueryEngine


os.environ["OPENAI_API_KEY"] = 'OPEN_API_KEY'
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search() -> (str | None):
    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    search_txt = request.form['search']
    response = query_engine.query(search_txt)
    return str(response)


@app.route('/search-json', methods=['POST'])
def searchJson() -> (str | None):
    search_txt = request.form['search']
    data_model = "./data/"+request.form['model'] + '_data.json'
    schema_model = "./data/"+request.form['model'] + '_schema.json'
    with open(data_model) as f:
        json_value = json.load(f)

    with open(schema_model) as f:
        json_schema = json.load(f)

    
    llm = OpenAI(model="text-davinci-003")
    service_context = ServiceContext.from_defaults(llm=llm)
    
    raw_query_engine = JSONQueryEngine(
        json_value=json_value,
        json_schema=json_schema,
        service_context=service_context,
        synthesize_response=False,
    )
    raw_response = raw_query_engine.query(search_txt)
    nl_query_engine = JSONQueryEngine(
        json_value=json_value, json_schema=json_schema, service_context=service_context
    )
    nl_query_response = nl_query_engine.query(search_txt)
    print(raw_response)

    return make_response(jsonify(nl_query_response), 200)

if __name__ == '__main__':
    app.run(debug=True, port = 8080)