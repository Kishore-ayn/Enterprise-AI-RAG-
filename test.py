
import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# ==========================================
# 1. TEST GROQ CHAT MODEL
# ==========================================

print("\n========== GROQ CHAT MODEL TEST ==========")

try:
    groq_client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    chat_model = os.getenv("GROQ_CHAT_MODEL")

    response = groq_client.chat.completions.create(
        model=chat_model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": "Explain Enterprise RAG in simple terms."
            }
        ],
        temperature=0.2,
        max_completion_tokens=300
    )

    print("Status: SUCCESS")
    print("Model:", chat_model)
    print("\nResponse:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Groq Error:", str(e))

# ==========================================
# 2. TEST LOCAL EMBEDDING MODEL
# ==========================================

print("\n========== EMBEDDING MODEL TEST ==========")

try:
    embed_model = os.getenv("EMBED_MODEL")
    expected_dim = int(os.getenv("EMBED_DIM"))

    # Load embedding model locally
    embedding_model = SentenceTransformer(
        embed_model,
        device="cpu"
    )

    # Generate embedding
    text = "Enterprise RAG uses retrieval to provide relevant answers."

    vector = embedding_model.encode(
        text,
        normalize_embeddings=True
    )

    print("Status: SUCCESS")
    print("Model:", embed_model)
    print("Expected Dimensions:", expected_dim)
    print("Actual Dimensions:", len(vector))
    print("Embedding Sample:", vector[:5])

    if len(vector) == expected_dim:
        print("\nDimension Check: PASSED")
    else:
        print("\nDimension Check: FAILED")

except Exception as e:
    print("Embedding Error:", str(e))

print("\n========== TESTING COMPLETED ==========")