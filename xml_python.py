import xml.etree.ElementTree as ET


tree = ET.parse('file_name.xml')
root = tree.getroot()

value=input("Please enter a valid int value.")

for data in root.iter('DefaultValue'):
    new_data = value
    data.text = str(new_data)
    print(data.text)

print(ET.tostring(root, encoding='utf8').decode('utf8'))
