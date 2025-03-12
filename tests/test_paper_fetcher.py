# tests/test_paper_fetcher.py

import pytest
from pharma_papers.paper_fetcher import PaperFetcher

def test_fetch_paper_ids():
    fetcher = PaperFetcher(query="cancer", debug=True)
    paper_ids = fetcher.fetch_paper_ids()
    assert isinstance(paper_ids, list)

def test_fetch_paper_details():
    fetcher = PaperFetcher(query="cancer", debug=True)
    paper_ids = ["12345", "67890"]
    papers = fetcher.fetch_paper_details(paper_ids)
    assert isinstance(papers, list)
