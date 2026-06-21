import re 
from scraper.wikipedia import get_article


def chunk_article_data(article_data: dict) -> list[dict]:
    
    pattern = r"^(={2,4})\s*(.+?)\s*\1\s*$"
    text_data = article_data["text"]
    matches = list(re.finditer(pattern, text_data, re.MULTILINE))

    chunks = []
    intro_text = text_data[:matches[0].start()] # .start() is a method on a regex match object - returns the index position (an integer) in the string where that match begins.
    chunks.append({
        "text" : intro_text.strip(),
        "article_title": article_data["title"],
        "section": "Intro",
        "subsection": None,
        "page_id": article_data["page_id"]
    })

    for i, match in enumerate(matches):
        number_of_equal_signs = len(match.group(1))
        heading_name = match.group(2)

        if i + 1 < len(matches):
            content = text_data[match.end():matches[i + 1].start()]
        else:
            content = text_data[match.end():]

        print(heading_name, "->", content)
        
        

     

 





chunk_article_data(get_article("Madrid"))


# the way it's actually done rather than path-hacking per file: run it as a module instead of as a raw script. 
# From your project root: uv run python -m pipeline.chunking
# match.group(1)is number of "=", match.group(2) is the heading name

'''
Let's keep top-level and subsection chunks independent for now and revisit if evals show a problem. 
Retrieval systems should be tuned against real evaluation data, not hypothetical edge cases. 
If chunking causes retrieval issues, it will show up in metrics like context precision or faithfulness, and we can make a targeted fix based on evidence.
'''

'''
treat === as the deepest chunking level — i.e., cap chunking at one level of subsection nesting
, and merge anything deeper (==== and beyond) up into its === parent.
metadata (section + subsection, only two levels) — adding a third tracked level (subsubsection) multiplies complexity 
(... every chunk dict needs 3 heading fields, the boilerplate filter needs to check all 3 levels, etc.)
Cap at ===, ship it, see what eval says.
'''

'''
feat: loops through matches and builds a chunk for each ==/=== heading, with the rules: == → new section, reset subsection to None, === → subsection under the current section
==== → fold onto the previous chunk, skip boilerplate headings entirely 

'''


