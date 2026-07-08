import xml.etree.ElementTree as ET

root = ET.Element("students")

data = [
    {"name": "Saif", "grade": "A", "score": "92"},
    {"name": "Ali", "grade": "B", "score": "78"},
    {"name": "Zara", "grade": "A", "score": "95"},
]

for item in data:
    student = ET.SubElement(root, "student")
    ET.SubElement(student, "name").text = item["name"]
    ET.SubElement(student, "grade").text = item["grade"]
    ET.SubElement(student, "score").text = item["score"]

tree = ET.ElementTree(root)
ET.indent(tree, space="  ")
tree.write("students.xml", encoding="unicode", xml_declaration=True)

print("students.xml created successfully.")

with open("students.xml") as f:
    print(f.read())