from __future__ import annotations

import logging

from .app_factory import create_app
from .settings import Settings
from src.app.retriever.provider import real_retriever_factory

logger = logging.getLogger(__name__)
settings = Settings()
app = create_app(settings=settings, retriever_provider=lambda: real_retriever_factory(settings))
