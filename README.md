# Refine Keywords

> Identify search terms that resulted in irrelevant results.

## Usage
```bash
$ python3 refine-keywords.py [search data] [results]
```
**`[search data]`**  
A JSON file listing the IDs, category, and keyword hits for each search result. 
```{json}
{
    "847594": {
        "category": "relevant",
        "keywords": [
            "example keyword",
            "another keyword found in the record",
            "one last keyword in the record"
        ]
    }
}
```

**`[results]`**  
A path to a CSV file where the analysis results will be written. Each row will contain a keyword and the frequency that it appears in either group.

### Other files:
**`keywords.txt`**  
lists the keywords (or key phrases) that appear in the article abstracts. 