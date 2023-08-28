import langchain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.cache import InMemoryCache

import openai

from projections.projection import Neo4jProjection
from similarities.similarity import Neo4jSimilarity

from templates.cypher_gen_template import CYPHER_GEN_PROMPT
import colorama

colorama.init()

YELLOW = "\x1b[1;33;40m" 
RED = "\x1b[1;31;40m"

def main():
    """
    Main funciton to setup Neo4j connection, projections,
    similarites, and interact with user.
    """
    langchain.llm_cache = InMemoryCache()
    llm = ChatOpenAI(temperature=0)

    print(
        """
        Hi. I'm MovieCritic.AI, a chat bot that specializes in finding
        you the movies you enjoy most. The more we chat, the better
        the recommendations. To get started, please log in:
        """
    )

    openai_api_key = str(input("Enter OpenAI API key: "))
    uri = str(input("Enter Neo4j uri: "))
    username = str(input("Enter Neo4j username: "))
    password = str(input("Enter Neo4j password: "))

    openai.api_key = openai_api_key

    # Introduction
    print(
        """
        MovieCritic.AI: Great. Let's get started. How can I help?
        """
    )

    graph = Neo4jGraph(
        url=uri, 
        username=username, 
        password=password,
    )

    # Make projections
    projection = Neo4jProjection(graph=graph)
    projection.project_movie_person()
    projection.run()

    # Make similarities
    similarity = Neo4jSimilarity(graph=graph)
    similarity.similarity_movie_person()
    similarity.run()

    memory = ConversationBufferMemory(llm=llm)
    chain = GraphCypherQAChain.from_llm(
        llm=llm,
        graph=graph,
        memory=memory,
        verbose=False,
        cypher_prompt=CYPHER_GEN_PROMPT,
    )

    while True:
        user_input = str(input(f"\n{YELLOW}Me: "))
        try:
            result = chain(user_input)["result"]
            print(f"\n{RED}MovieCritic.AI: {result}")
        except ValueError:
            pass

if __name__ == "__main__":
    main()