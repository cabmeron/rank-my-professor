# rank-my-professor

## Aggregate & Display UNR's professors by
<ul>
  <li> # of Citations </li>
</ul>

## Process
1) Gemini Research to gather all professors in a department for each college
2) Scrape Google Scholar via <a href="https://www.scrapingdog.com/"> Scrapingdog
3) Use up all free api credits, resort to pure Gemini JSON query requests (close enough)
4) Setup FastAPI server
5) Fetch from FastAPI with Vanilla Web Client

## Data format:
```
[
  {
    "name": "professor1",
    "cited_by": 1000,
    "h_index": 32,
    "gs_link": "https://scholar.google.com/citations?user=hwJ5DlQAAAAJ&hl=en"
  }
]
```
<img width="357" height="864" alt="Screenshot 2025-07-12 at 9 56 53 PM" src="https://github.com/user-attachments/assets/69018bad-93c9-4bc0-a0ff-5199724079f5" />
