import xml.etree.ElementTree as ET
import pandas as pd

cols = ["name", "phone", "email", "date"]
rows = []

# Parse XML file
tree = ET.parse('employee.xml')
root = tree.getroot()
for elem in root:
    name = elem.find("name").text
    phone = elem.find("phone").text
    email = elem.find("email").text
    date = elem.find("date").text

    rows.append({"name": name,
                 "phone": phone,
                 "email": email,
                 "date": date})

df = pd.DataFrame(rows, columns=cols)

# write dataframe to csv
df.to_csv('company.csv')