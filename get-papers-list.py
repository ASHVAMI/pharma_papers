# get-papers-list.py

import click
from pharma_papers.paper_fetcher import PaperFetcher

@click.command()
@click.argument('query')
@click.option('--file', '-f', type=str, help='Filename to save the results as CSV.')
@click.option('--debug', '-d', is_flag=True, help='Enable debug mode.')
def main(query: str, file: Optional[str], debug: bool):
    fetcher = PaperFetcher(query=query, debug=debug)
    paper_ids = fetcher.fetch_paper_ids()
    papers = fetcher.fetch_paper_details(paper_ids)
    
    if file:
        fetcher.save_as_csv(papers, file)
        if debug:
            print(f"Results saved to {file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == '__main__':
    main()
