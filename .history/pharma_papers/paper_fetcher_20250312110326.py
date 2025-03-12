# pharma_papers/paper_fetcher.py

import requests
from typing import List, Dict, Optional, Tuple
import csv
import re

class PaperFetcher:
    PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    PUBMED_API_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    PUBMED_API_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def __init__(self, query: str, debug: bool = False):
        self.query = query
        self.debug = debug

    def fetch_paper_ids(self) -> List[str]:
        """Fetch PubMed IDs based on the query."""
        if self.debug:
            print(f"Fetching paper IDs for query: {self.query}")
        
        params = {
            "db": "pubmed",
            "term": self.query,
            "retmode": "json",
            "retmax": 100
        }
        
        response = requests.get(self.PUBMED_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        paper_ids = data["esearchresult"]["idlist"]
        if self.debug:
            print(f"Found paper IDs: {paper_ids}")
        return paper_ids

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict]:
        """Fetch details of papers by their PubMed IDs."""
        if self.debug:
            print(f"Fetching paper details for IDs: {paper_ids}")

        params = {
            "db": "pubmed",
            "id": ",".join(paper_ids),
            "retmode": "xml"
        }

        response = requests.get(self.PUBMED_API_FETCH_URL, params=params)
        response.raise_for_status()

        # Here you would parse the XML response
        # Simulating parsed data for example purposes
        paper_details = [
            {
                "PubmedID": "12345",
                "Title": "Example Research Paper",
                "PublicationDate": "2024-03-10",
                "NonAcademicAuthors": ["John Doe", "Jane Smith"],
                "CompanyAffiliations": ["PharmaTech"],
                "CorrespondingAuthorEmail": "jane.smith@pharmatech.com"
            }
        ]
        
        if self.debug:
            print(f"Fetched paper details: {paper_details}")
        
        return paper_details

    def save_as_csv(self, papers: List[Dict], filename: str):
        """Save the fetched paper details as a CSV."""
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["PubmedID", "Title", "PublicationDate", "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingAuthorEmail"])
            writer.writeheader()
            for paper in papers:
                writer.writerow(paper)

    def identify_non_academic_authors(self, affiliations: List[str]) -> Tuple[List[str], List[str]]:
        """Identify authors affiliated with non-academic institutions."""
        companies = []
        non_academic_authors = []
        for affiliation in affiliations:
            if any(keyword in affiliation.lower() for keyword in ["pharma", "biotech", "corporation", "inc", "ltd"]):
                companies.append(affiliation)
                # Assume author name parsing is correct in real implementation
                non_academic_authors.append("Author Name")
        return non_academic_authors, companies
