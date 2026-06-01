# Hidden-message-grid-decoder

## What it does:
->Scrapes a Google Doc containing a table of characters with x,y coordinates and decodes them into a hidden visual message 
by reconstructing the 2D grid.

## Working mechanism:
1. Fetches HTML from a Google Doc URL
2. Parses the table using BeautifulSoup
3. Extracts character, x, y values
4. Builds a 2D grid dynamically
5. Renders the hidden message

## Tech used:
Python | requests | BeautifulSoup | 
2D Arrays | Web Scraping

## Required:
pip install requests beautifulsoup4

## What I learned from this:
- Web scraping with requests and BeautifulSoup
- Parsing HTML tables
- 2D grid construction from coordinate data
- Dynamic sizing using max() on coordinates
