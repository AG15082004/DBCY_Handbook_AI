# test_vector.py

from databricks.vector_search.client import VectorSearchClient

client = VectorSearchClient(disable_notice=True)

index = client.get_index(
    endpoint_name="aichatbot-vs-endpoint",
    index_name="aichatbot.gold.handbook_vector_index"
)

print("SUCCESS")