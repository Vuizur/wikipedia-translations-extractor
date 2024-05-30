# Wikipedia Title Translation Extractor

This is a repo showing how to extract the title translations from Wikipedia. 
First you need to execute `setup.sh`, and then `extract_data.py` 

The resulting file is in JSON lines format, where the content of one JSON object (line) looks like this.
The data can be downloaded in the [releases](https://github.com/Vuizur/wikipedia-translations-extractor/releases/tag/latest):

```json5
{
    "page_id": 12,
    "title": "Anarchism",
    "is_redirect": 0,
    "namespace": 0,
    "languages": [
        {
            "title": "Anargisme",
            "lang_code": "af"
        },
        {
            "title": "Anarchismus",
            "lang_code": "als"
        },
        {
            "title": "ሥርዓት አልበኝነት",
            "lang_code": "am"
        },
        {
            "title": "Anarquismo",
            "lang_code": "an"
        },
        {
            "title": "Ƿealdlīste rǣd",
            "lang_code": "ang"
        }
        // ...
    ]
}