from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph

from moviecritic.templates.cypher_gen_template import CYPHER_GEN_PROMPT

import openai


openai_api_key = "" # left blank for repo
uri = "" # left blank for repo
username = "" # left blank for repo
password = "" # left blank for repo

openai.api_key = openai_api_key

llm = ChatOpenAI(temperature=0)

graph = Neo4jGraph(
        url=uri,
        username=username,
        password=password,
    )

chain = GraphCypherQAChain.from_llm(
        llm=llm,
        graph=graph,
        verbose=False,
        cypher_prompt=CYPHER_GEN_PROMPT,
    )

def test_movie_count_38():
    """
    Test movie count of raw Movies db in Neo4j.
    """
    assert chain.run("How many movies are you aware of?") == "I am aware of 38 movies."

def test_movie_count_not_37():
    """
    Test movie count of raw Movies db in Neo4j.
    """
    assert chain.run("How many movies are you aware of?") != "I am aware of 37 movies."