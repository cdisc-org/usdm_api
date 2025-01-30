import json
from model.api_base_model import ApiBaseModel
from model.code import Code
from model.study_definition_document import StudyDefinitionDocument
from model.extension_attribute import ExtensionAttribute
from model.extension_class import ExtensionClass

def pretty_json(label, instances: list[ApiBaseModel]):
  print(f"\n{label}:\n\n")
  for instance in instances:
    print(f"{json.dumps(instance.model_dump(), indent=2)}\n\n")


# Standard code, baseline
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code')
pretty_json('STANDARD CODE', [code])

# Example of extending code with single value
ext = ExtensionAttribute(
  id='X1', # Id because the attribute is actually .... a class!
  url='http://cdisc.org/usdm/extensions/extension-1/attribute', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  valueString='Extra value', # The actual extra value
  instanceType='ExtensionAttribute')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[ext])
pretty_json('SIMPLE EXTENSION', [code])

# Simple way of adding array of values. Only works if there is a single array of values.
params = {
  'id': 'X1', 
  'url': 'http://cdisc.org/usdm/extensions/extension-2/attribute', # Name is a different URL 
  'valueString': 'Extra value 1', 
  'instanceType': 'ExtensionAttribute'
}
ext_value_1 = ExtensionAttribute(**params)
params['id'] = 'X2'
params['valueString'] = 'Extra value 2'
ext_value_2 = ExtensionAttribute(**params)
params['id'] = 'X3'
params['valueString'] = 'Extra value 3'
ext_value_3 = ExtensionAttribute(**params)
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[ext_value_1, ext_value_2, ext_value_3])
pretty_json('SIMPLE ARRAY EXTENSION V1', [code])

# Slightly more complex way of building an array, array links off a single attribute, useful if need more than one array

# First collection of values, values with one URL and top level attribute with a unique URL
params = {
  'id': 'X1', 
  'url': 'http://cdisc.org/usdm/extensions/extension-3/attribute-1', # Name is a different URL 
  'valueString': 'Extra value 1', 
  'instanceType': 'ExtensionAttribute'
}
ext_value_1 = ExtensionAttribute(**params)
params['id'] = 'X2'
params['valueString'] = 'Extra value 2'
ext_value_2 = ExtensionAttribute(**params)
params['id'] = 'X3'
params['valueString'] = 'Extra value 3'
ext_value_3 = ExtensionAttribute(**params)
attribute1 = ExtensionAttribute(
  id='ARRAY_1_STRING', 
  url='http://cdisc.org/usdm/extensions/extension-3/attribute-array-1', 
  extensions=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionAttribute')

# Second collection
params = {
  'id': 'X10', 
  'url': 'http://cdisc.org/usdm/extensions/extension-3/attribute-2', # Name is a different URL 
  'valueBoolean': True, 
  'instanceType': 'ExtensionAttribute'
}
ext_value_10 = ExtensionAttribute(**params)
params['id'] = 'X11'
params['valueBoolean'] = False
ext_value_11 = ExtensionAttribute(**params)
params['id'] = 'X12'
params['valueBoolean'] = True
ext_value_12 = ExtensionAttribute(**params)
attribute2 = ExtensionAttribute(
  id='ARRAY_2_BOOLEAN', 
  url='http://cdisc.org/usdm/extensions/extension-3/attribute-array-2', 
  extensions=[ext_value_10, ext_value_11, ext_value_12], 
  instanceType='ExtensionAttribute')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[attribute1, attribute2])
pretty_json('SIMPLE ARRAY EXTENSION V2', [code])

# Complex extending code with array of values, used if you wanted to add several arrays to a class linked via a class, only one added here
ext = ExtensionClass(
  id='XCLASS1', 
  url='http://cdisc.org/usdm/extensions/extension-4/class', 
  attributes=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionClass')
link = ExtensionAttribute(
  id='LINK1', 
  url='http://cdisc.org/usdm/extensions/extension-4/attribute', 
  valueId='XC1', 
  instanceType='ExtensionAttribute')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[link])
pretty_json('CLASS EXTENSION', [code, ext])

# Array of new classes. Could link to an intermediate class like the example above if needed.
ext_1 = ExtensionClass(
  id='XCLASS1', 
  url='http://cdisc.org/usdm/extensions/extension-5/class-1', 
  attributes=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionClass')
ext_2 = ExtensionClass(
  id='XCLASS2', 
  url='http://cdisc.org/usdm/extensions/extension-5/class-2', 
  attributes=[ext_value_10, ext_value_11, ext_value_12], 
  instanceType='ExtensionClass')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[ext_1, ext_2])
pretty_json('ARRAY OF CLASSES', [code])


# The Document colour example. Example of extending an instance with a single value

# Yellow attribute  
yellow_colour_ext = ExtensionAttribute(
  id='X1', 
  url='http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  valueString='YELLOW', # The actual extra value
  instanceType='ExtensionAttribute')

# Red attribute
red_colour_ext = ExtensionAttribute(
  id='X11',
  url='http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  valueString='RED', # The actual extra value
  instanceType='ExtensionAttribute') 

# A yellow document
params = {
  'id': 'DEF_DOC_1',
  'name': 'Document',
  'label': 'Document',
  'description': 'Document',
  'language': Code(id='1', code='en', decode='English', codeSystem='ISO-639-1', codeSystemVersion='1.0', instanceType='Code'),
  'type': Code(id='1', code='Protocol', decode='Protocol Document', codeSystem='System', codeSystemVersion='1', instanceType='Code'),
  'templateName': 'ACME Sponsor Template v4.3',
  'versions': [],
  'notes': [],
  'instanceType': 'StudyDefinitionDocument',
  'extensions': [yellow_colour_ext]
}
document = StudyDefinitionDocument(**params)
pretty_json('YELLOW DOCUMENT', [document])

# Now change to a red document
params['extensions'] = [red_colour_ext]
document = StudyDefinitionDocument(**params)
pretty_json('RED DOCUMENT', [document])
