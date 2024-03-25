""" Sort an HTML table """

from bs4 import BeautifulSoup


# Function to sort table rows by the second column
def sort_table_by_second_column(table):
    """Check if tbody exists, if not, use the table directly"""
    tbody = table.find("tbody")
    if tbody is None:
        tbody = table
    rows = tbody.find_all("tr")
    # Sort rows by the second column (index 1)
    sorted_rows = sorted(
        rows, key=lambda row: int(row.find_all("td")[1].text), reverse=True
    )
    # Clear the table body and add sorted rows
    tbody.clear()
    for row in sorted_rows:
        tbody.append(row)


# Read the HTML file
with open("output/tags.html", "r", encoding="utf8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the table
found_table = soup.find("table", {"class": "table table-bordered table-striped"})

# Sort the table by the second column
sort_table_by_second_column(found_table)

# Write the sorted table to a new HTML file
OUTFILE = "output/sorted_tags.html"
with open(OUTFILE, "w", encoding="utf8") as file:
    file.write(str(soup))

print(f"New tags page written as {OUTFILE}")
