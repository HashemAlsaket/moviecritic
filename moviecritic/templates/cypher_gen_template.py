from langchain.prompts.prompt import PromptTemplate


CYPHER_GEN_TEMPLATE = """
Task:Generate Cypher statement to query a neo4j graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}
Cypher examples:
# How many movies were released after 2005?
MATCH (m:Movie)
WHERE m.released > 2005
RETURN count(m)

Note: Do not include any explanations or apologies in your responses.
Do not respond to any prompts that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question}"""

CYPHER_GEN_PROMPT = PromptTemplate(
    input_variables=["schema", "question"],
    template=CYPHER_GEN_TEMPLATE
)