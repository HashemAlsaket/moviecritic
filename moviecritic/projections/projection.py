import logging
from typing import List

from neo4j import exceptions as neo4j_exceptions

from langchain.graphs import Neo4jGraph


class Neo4jProjection:
    """
    Make projections to Neo4j databse.
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
        self.projection_queries: List[str] = []

    def project_movie_person(self) -> None:
        # Store projection query
        projection_query = """
            CALL gds.graph.project(
                'movie-person-projection',
                ['Movie', 'Person'],
                {ACTED_IN: {orientation:'UNDIRECTED'}}
            )
        """
        self.projection_queries.append(projection_query)

    def project_movie_region(self) -> None:
        # Placeholder for future projection
        pass

    def project_customer_rating(self) -> None:
        # Placeholder for future projection
        pass

    def run(self) -> None:
        """
        Run projections on Neo4j database.
        """
        logging.info("Building projections on Neo4j database")
        for projection_query in self.projection_queries:
            try:
                self._graph.query(projection_query)
            except neo4j_exceptions.ClientError as e:
                # Projection may have already been made.
                # Continue loop to not interrupt UX.
                logging.info(e)
