COD_SYSTEM_PROMPT = """You will generate increasingly concise, entity-dense summaries of the above article. 
Repeat the following 2 steps 5 times. 
Step 1. Identify 1-3 informative entities (";" delimited) from the article which are missing from the previously generated summary. 
Step 2. Write a new, denser summary of identical length which covers every entity and detail fromthe previous summary plus the Missing Entities.

A missing entity is:
- Relevant:  to the main story.
- Specific: descriptive yet concise (5 words or fewer). 
- Novel: not in the previous summary. 
- Faithful: present in the Article.
- Anywhere: located anywhere in the Article.

Guidelines:
- The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
- Make every word count: re-write the previous summary to improve flow and make space for additional entities.
- Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
- The summar i es shoul d become hi ghl y dense and conci se yet self-contained, e.g., easily understood without the Article.
- Missing entities can appear anywhere in the newsummary.
- Never drop entities fromthe previous summary. If space cannot be made, add f ewer new entities.

Remember, use the exact same number of words for each summary.

Return a python list with square brackets. Each element should be a python dictionary with two keys: "Missing_Entities" and "Denser_Summary". There should be 5 elements in the list"""