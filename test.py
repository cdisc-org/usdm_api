import json
from model.api_base_model import ApiBaseModel
from model.code import Code
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
  name='http://cdisc.org/usdm/extension/fix-code', # Name is a unique URL defining who built the extension and a unique id/ref to extension
  label="Fix to add extra attribute in Code class", # What the extension is about, could be omitted but should be defined within the extension definition.
  description='Fill in a value with some shit', # What the value is about, could be omitted but should be defined within the extension definition.
  valueString='Extra value', # The actual extra value
  instanceType='ExtensionAttribute')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[ext])
pretty_json('SIMPLE EXTENSION', [code])

# Simple way of adding array of values
params = {
  'id': 'X1', 
  'name': 'http://cdisc.org/usdm/extension/fix-code-array-attrib', # Name is a different URL 
  'label': "Fix to add array of attributes in Code class", 
  'description': 'Fill in a value with some shit', 
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
pretty_json('SIMPLE ARRAY EXTENSION', [code])

# Complex extending code with array of values, used if you wanted to add several arrays to a class, only one added here
ext = ExtensionClass(
  id='XC1', 
  name='http://cdisc.org/usdm/extension/fix-code-array-class', 
  label="Fix to add extra attribute in Code class", 
  description='Fill in a value with some array of shit', 
  attributes=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionClass')
link = ExtensionAttribute(
  id='LNK1', 
  name='http://cdisc.org/usdm/extension/fix-code-array-link', 
  label="Fix to add extra attributes in Code class, via a ref", 
  description='Fill in a value with some shit', 
  valueId='XC1', 
  instanceType='ExtensionAttribute')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[link])
pretty_json('COMPLEX ARRAY EXTENSION', [code, ext])

# Array of new classes. Could link to an intermediate class like the example above if needed.
ext_1 = ExtensionClass(
  id='XC1', 
  name='http://cdisc.org/usdm/extension/fix-code-array-class', 
  label="Fix to add extra attribute in Code class", 
  description='Fill in a value with some array of shit', 
  attributes=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionClass')
ext_2 = ExtensionClass(
  id='XC2', 
  name='http://cdisc.org/usdm/extension/fix-code-array-class', 
  label="Fix to add extra attribute in Code class", 
  description='Fill in a value with some array of shit', 
  attributes=[ext_value_1, ext_value_2, ext_value_3], 
  instanceType='ExtensionClass')
code = Code(id='1', code='Code', decode='decode', codeSystem='System', codeSystemVersion='Version', instanceType='Code', extensions=[ext_1, ext_2])
pretty_json('ARRAY OF CLASSES', [code])
