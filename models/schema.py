from dataclasses import dataclass
from typing import Dict

@dataclass
class DocumentChunk:
    content: str
    source_id: str
    source_type: str
    metadata: Dict

@dataclass
class WebSearchResult:
    title: str
    content: str
    url: str
