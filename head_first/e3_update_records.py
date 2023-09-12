import gazpacho
import json
from pyprojroot import here

URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
RECORDS = (0, 2, 4, 5)
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")
WHERE = "data/swimrecord/"
JSONDATA = "records.json"

# use `gazpacho` to retrieve raw HTML from URL web address
html = gazpacho.get(URL)
# passing the raw HTML string into the "Soup" constructor creates a parsed representation of the HTML
soup = gazpacho.Soup(html)
# search for tags of interest
tables = soup.find("table", mode="all")

records = {}
for table, course in zip(RECORDS, COURSES):
    records[course] = {}
    for row in tables[table].find("tr", mode="all")[1:]:
        columns = row.find("td", mode="all")
        event = columns[0].text
        time = columns[1].text
        # filter the "relay" data
        if "relay" not in event:
            records[course][event] = time

with open(here(WHERE + JSONDATA), "w") as jf:
    json.dump(records, jf)