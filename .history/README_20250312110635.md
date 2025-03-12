# Pharma Papers Fetcher

## Project Overview
This Python program fetches research papers from PubMed using the PubMed API and identifies authors affiliated with pharmaceutical or biotech companies. The results are returned in a CSV file or printed to the console.

## Features
- Fetch papers based on user queries using PubMed's full query syntax.
- Identify authors affiliated with pharmaceutical/biotech companies.
- Save results as a CSV file or print to console.
- Command-line interface with options for file output and debug mode.

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/pharma_papers.git cd pharma_papers

1. Install dependencies using Poetry:
poetry install

## Usage

### Command Line
You can run the script with the following command:

poetry run get-papers-list "<query>" [--file <filename>] [--debug]

Examples:
- To print the output to the console:
poetry run get-papers-list "cancer research"

- To save the results to a file:
poetry run get-papers-list "cancer research" --file output.csv

### Options
- `-f`, `--file`: Specify the filename to save the results.
- `-d`, `--debug`: Enable debug mode to print additional information.

## Testing
Run tests with pytest:
poetry run pytest

## Tools Used
- [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/)
- [Poetry](https://python-poetry.org/) for dependency management
- [Click](https://click.palletsprojects.com/) for the CLI

Steps to Run the Project
Clone the Repository:
git clone https://github.com/yourusername/pharma_papers.git
cd pharma_papers

Install Dependencies:
poetry install

Run the Program:
poetry run get-papers-list "<query>" [--file <filename>] [--debug]

Run Tests:
poetry run pytest



Developed by Ashvani s !!!!!






