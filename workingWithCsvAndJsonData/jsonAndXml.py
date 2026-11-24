# JSON FILE FORMAT
# import json

# # # Reading JSON Data
# # # Reading json with the loads() function
# # json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer": true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type":"mobile", "number": "415-555-7890"}, {"type": "work", "number": "415-555-1234"}]}'
# # python_data = json.loads(json_string)
# # print(python_data)


# # Writing JSON Data
# python_data = {'name': 'Alice Doe', 'age': 30, 'car': None, 'programmer': True, 'address':
# {'street': '100 Larkin St.', 'city': 'San Francisco', 'zip': '94102'}, 'phone': [{'type': 
# 'mobile', 'number': '415-555-7890'}, {'type': 'work', 'number': '415-555-1234'}]}
# json_string = json.dumps(python_data)
# print(json_string)
# json_string = json.dumps(python_data, indent=2)     # indent=2 keyword formats the JSON text into seperate lines, with two spaces of indentation for each nested dictionary or list.
# print(json_string)


# XML FILE FORMAT
# Reading XML Files
import xml.etree.ElementTree as ET
xml_string = """
<person>
    <name>Alice Doe</name>
    <age>30</age>
    <programmer>true</programmer>
    <car xsi:nil="true" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
    <address>
        <street>100 Larkin St.</street>
        <city>San Francisco</city>
        <zip>94102</zip>
    </address>
    <phone>
        <phoneEntry>
            <type>mobile</type>
            <number>415-555-7890</number>
        </phoneEntry>
        <phoneEntry>
            <type>work</type>
            <number>415-555-1234</number>
        </phoneEntry>
    </phone>
</person>
"""
root = ET.fromstring(xml_string)        # get the root element from the xml string
print(root)
print(root.tag)     
print(list(root))

print(root[0].tag)
print(root[0].text)
print(root[3].tag)
print(root[3].text == None)  # <car/> has no text. 
print(root[4].tag)
print(root[4][0].tag)
print(root[4][0].text)

# Iterating over immediate child elements
for elem in root:
    print(elem.tag, '--', elem.text)

# Iterating over all children underneath the Element
for elem in root.iter():
    print(elem.tag, '--', elem.text)

# Filter for XML elements with a matching tag
for elem in root.iter('number'):
    print(elem.tag, '--', elem.text)


# tree = ET.parse('my_data.xml')      # load elemnet object from xml file
# root = tree.getroot()

# Coverting XML text to Python dictionary
import xmltodict
python_data = xmltodict.parse(xml_string)
print(python_data)

# Writing XML Files
person = ET.Element('person')  # Create the root XML element.
name = ET.SubElement(person, 'name')  # Create <name> and put it under <person>.
name.text = 'Alice Doe'  # Set the text between <name> and </name>.
age = ET.SubElement(person, 'age')
age.text = '30'  # XML content is always a string.
programmer = ET.SubElement(person, 'programmer')
programmer.text = 'true'
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')
car.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
address = ET.SubElement(person, 'address')
street = ET.SubElement(address, 'street')
street.text = '100 Larkin St.'

print(ET.tostring(person, encoding='utf-8').decode('utf-8'))