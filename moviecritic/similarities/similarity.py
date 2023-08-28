import logging
from typing import List

from neo4j import exceptions as neo4j_exceptions

from langchain.graphs import Neo4jGraph


class Neo4jSimilarity:
    """
    Measure similarities from projections made in
    the Neo4j databse.
    Args:
    ----
        uri (str): URI to Neo4j database
        username (str): Username to Neo4j database
        password (str): Password to Neo4j database
    """
    def __init__(
        self,
        graph: Neo4jGraph
    ):
        self._graph = graph
        self.similarity_queries: List[str] = []

    def similarity_movie_person(self) -> None:
        # Store similarity query
        similarity_query = """
            CALL gds.nodeSimilarity.mutate('movie-person-projection', {
                similarityMetric: 'Jaccard',
                similarityCutoff: 0.05,
                topK:10,
                sudo:true,
                mutateProperty:'score',
                mutateRelationshipType:'SIMILAR'
                }
            )
        """
        self.similarity_queries.append(similarity_query)

    def similarity_movie_region(self) -> None:
        # Placeholder for future similarity
        pass

    def similarity_customer_rating(self) -> None:
        # Placeholder for future similarity
        pass

    def run(self) -> None:
        """
        Run similarities on Neo4j database.
        """
        logging.info("Building similarities on Neo4j database")
        for similarity_query in self.similarity_queries:
            try:
                self._graph.query(similarity_query)
            except neo4j_exceptions.ClientError as e:
                # Similarity may have already been made.
                # Continue loop to not interrupt UX.
                logging.info(e)
