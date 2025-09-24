from __future__ import annotations

from pathlib import Path

from src.api.settings import Settings
from src.core.search.retriever import Retriever


def real_retriever_factory(settings: Settings) -> Retriever:
    retr = Retriever(
        model_path=Path("data/topic_model.joblib"),
        corpus_path=Path("data/corpus.parquet"),
        cache_dir=Path("index_cache"),
    )
    retr.ready(wait=False)
    return retr
