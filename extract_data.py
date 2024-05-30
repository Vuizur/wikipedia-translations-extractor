from collections import defaultdict
import json
import mariadb
from tqdm import tqdm

# Connect to database wikipedia
conn = mariadb.connect(
    user="root",
    password="lune",
    host="localhost",
    port=3306,
    database="wikipedia"
)

cursor = conn.cursor()

def decode_bytes(value):
    return value.decode('utf-8') if isinstance(value, bytes) else value

cursor.execute("""
SELECT 
    page.page_id, 
    page.page_title, 
    page.page_namespace, 
    page.page_is_redirect, 
    CONCAT(
  '[',
    GROUP_CONCAT(JSON_OBJECT('title', langlinks.ll_title, 'lang_code', langlinks.ll_lang)),
  ']') AS languages
FROM 
    page 
JOIN 
    langlinks ON page.page_id = langlinks.ll_from
GROUP BY 
    page.page_id
LIMIT 10;
""")
# Write results to jsonl
with open('output.jsonl', 'w') as file:
    for page_id, page_title, page_namespace, page_is_redirect, languages in cursor:
        page_title = decode_bytes(page_title)
        languages = json.loads(languages)
        # Write the JSON line
        file.write(json.dumps({
            "page_id": page_id,
            "title": page_title.replace('_', ' '),
            "is_redirect": page_is_redirect,
            "namespace": page_namespace,
            "languages": languages
        }, ensure_ascii=False) + '\n')


cursor.close()
conn.close()