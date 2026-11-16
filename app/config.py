from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra='ignore')
    aws_region:str='us-east-1'
    aws_access_key_id:str=''
    aws_secret_access_key:str=''
    s3_bucket:str=''
    database_url:str=''  # Render PostgreSQL External Database URL
    embed_model:str='sentence-transformers/all-MiniLM-L6-v2'
    groq_chat_model:str='openai/gpt-oss-20b'
    embed_dim:int=384
    max_upload_bytes:int=10485760
    pinecone_api_key:str=''
    pinecone_index_name:str='atlas-enterprise-ai-index'
    pinecone_cloud:str='aws'
    pinecone_region:str='us-east-1'
    pinecone_ready_timeout:int=180
    min_relevance:float=0.25
    hitl_enabled:bool=True
    memory_turns:int=6


@lru_cache
def settings() -> Settings:
    return Settings()