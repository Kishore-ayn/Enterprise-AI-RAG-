
from app.services import embed

text = "What is the hospital leave policy?"

try:
    vector = embed(text)

    print("\nEmbedding test successful!")
    print("Dimensions:", len(vector))
    print("First 5 values:", vector[:5])
    print("Data type:", type(vector))

    assert len(vector) == 384
    assert isinstance(vector, list)

except Exception as e:
    print("Embedding test failed:", str(e))
