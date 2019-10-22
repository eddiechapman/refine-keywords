"""
refine-keywords.py

Identify search terms that resulted in irrelevant results.

"""
import collections
import csv
import json
import pathlib
import sys


def main():
    if not len(sys.argv) == 3:
        print('Insufficient arguments.') 
        print('Usage: refine-keywords.py <input> <destination>')
        sys.exit()
    
    INPUT = pathlib.Path(sys.argv[1])
    OUTPUT = pathlib.Path(sys.argv[2])

    try:
        with INPUT.open('r') as f:
            search_results = json.load(f)
    except FileNotFoundError:
        print(f'Input path could not be located: {sys.argv[1]}')
        sys.exit()

    print(f'Beginning keyword analysis of {INPUT}')
    
    records = collections.Counter()
    keywords = dict()
    for _id, result in search_results.items():
        cat = result['category']
        records.update({cat: 1})
        if cat not in keywords:
            keywords[cat] = collections.Counter()
        keywords[cat].update({kw: 1 for kw in result['keywords']})
            
    all_keywords = set()
    for counter in keywords.values():
        all_keywords.update(list(counter.elements()))

    results = []
    for keyword in sorted(all_keywords):
        result_data = {'keyword': keyword}
        for cat in keywords:
            result_data[cat] = keywords[cat][keyword]
            result_data[f'{cat}-total'] = records[cat]
        results.append(result_data)

    with OUTPUT.open('w') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    
    print(f'Keyword analysis complete. The results are located at {OUTPUT}')


if __name__ == '__main__':
    main()
