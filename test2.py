import json
from model.api_base_model import ApiBaseModel
from model.extension import ExtensionAttribute, ExtensionClass
from model.code import Code
from model.study_definition_document import StudyDefinitionDocument
def pretty_json(label, instances: list[ApiBaseModel]):
    print(f"\n{label}:\n\n")
    for instance in instances:
        print(f"{json.dumps(instance.model_dump(exclude_none=True), indent=2)}\n\n")


# Standard code, baseline
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
)
pretty_json("STANDARD CODE", [code])

# Example of extending code with single value
ext = ExtensionAttribute(
    id="ExtensionAttributeValue_1",
    url="http://cdisc.org/usdm/extensions/extension-1/attribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    valueString="Extra value",  # The actual extra value
    instanceType="ExtensionAttribute",
)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[ext],
)
pretty_json("SIMPLE EXTENSION", [code])

# Simple way of adding array of values
params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/attribute",  # Name is a different URL
    "id": "ExtensionAttributeValue_2",
    "valueString": "Extra value 1",
    "instanceType": "ExtensionAttribute",
}
ext_value_1 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_3"
params["valueString"] = "Extra value 2"
ext_value_2 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_4"
params["valueString"] = "Extra value 3"
ext_value_3 = ExtensionAttribute(**params)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[ext_value_1, ext_value_2, ext_value_3],
)
pretty_json("SIMPLE ARRAY EXTENSION V1", [code])

# # Slightly more complex way of building an array, array links off a single attribute, useful if need more than one array
# attribute = ExtensionAttribute(
#     url="http://cdisc.org/usdm/extensions/extension-3/attribute-array",
#     id="ExtensionAttributeValue_5",
#     valueString=[
#         x.valueString for x in [ext_value_1, ext_value_2, ext_value_3]
#     ],  # A list of string values
#     instanceType="ExtensionAttribute",
# )
# code = Code(
#     id="1",
#     code="Code",
#     decode="decode",
#     codeSystem="System",
#     codeSystemVersion="Version",
#     instanceType="Code",
#     extensionAttributes=[attribute],
# )
# pretty_json("SIMPLE ARRAY EXTENSION V2", [code])

# Complex extending code with array of values, used if you wanted to add several arrays to a class linked via a class, only one added here
array_attribute = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#array-attribute-root",
    id="ExtensionAttributeValue_5",
    extensionAttributes=[
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#array-attribute",
            id="ExtensionAttributeValue_7",
            valueString="ARRAY1",
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#array-attribute",
            id="ExtensionAttributeValue_8",
            valueString="ARRAY2",  # This is the label of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#array-attribute",
            id="ExtensionAttributeValue_9",
            valueString="ARRAY3",  # This is the description of the instance of the extension class
            instanceType="ExtensionAttribute",
        )
    ],
    instanceType="ExtensionAttribute",
)
int_attribute = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#int-attribute",
    id="ExtensionAttributeValue_6",
    valueInteger=12,
    instanceType="ExtensionAttribute",
)
ext_cl_inst = ExtensionClass(
    url="http://cdisc.org/usdm/extensions/extension-4/class",
    id="ExtensionClassInstance_1",
    extensionAttributes=[
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#name",
            id="ExtensionAttributeValue_7",
            valueString="XCLASS1",  # This is the name of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#label",
            id="ExtensionAttributeValue_8",
            valueString="Fix to add extra attribute in Code class",  # This is the label of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/class/attributes#description",
            id="ExtensionAttributeValue_9",
            valueString="Fill in a value with ",  # This is the description of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        int_attribute,
        array_attribute
    ],
    instanceType="ExtensionClass",
)
link = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-4/attribute",
    id="ExtensionAttributeValue_10",
    valueId="ExtensionClassInstance_1",
    instanceType="ExtensionAttribute",
)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[link],
)
pretty_json("COMPLEX ARRAY EXTENSION", [code, ext_cl_inst])

# Array of new classes. Could link to an intermediate class like the example above if needed.
ext_1 = ExtensionClass(
        url="http://cdisc.org/usdm/extensions/extension-5/class-1",
        id="ExtensionClassInstance_2",
        extensionAttributes=[
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-1/attributes#name",
                id="ExtensionAttributeValue_12",
                valueString="XCLASS2",  # This is the name of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-1/attributes#label",
                id="ExtensionAttributeValue_13",
                valueString="Fix to add extra attribute in Code class",  # This is the label of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-1/attributes#description",
                id="ExtensionAttributeValue_14",
                valueString="Fill in a value with an array and a string value",  # This is the description of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
        ],
        instanceType="ExtensionClass",
    )
ext_2 = ExtensionClass(
        url="http://cdisc.org/usdm/extensions/extension-5/class-2",
        id="ExtensionClassInstance_3",
        extensionAttributes=[
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-2/attributes#name",
                id="ExtensionAttributeValue_16",
                valueString="XCLASS3",  # This is the name of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-2/attributes#label",
                id="ExtensionAttributeValue_17",
                valueString="Fix to add extra attribute in Code class",  # This is the label of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="http://cdisc.org/usdm/extensions/extension-5/class-2/attributes#description",
                id="ExtensionAttributeValue_18",
                valueString="Fill in a value with an integer and a string value",  # This is the description of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
        ],
        instanceType="ExtensionClass",
    )
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionClasses=[ext_1, ext_2],
)
pretty_json("ARRAY OF CLASSES", [code])

# The Document colour example. Example of extending an instance with a single value

# Yellow attribute  
yellow_colour_ext = ExtensionAttribute(
  url='http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  id='ExtensionAttributeValue_19', 
  valueString='YELLOW', # The actual extra value
  instanceType='ExtensionAttribute')

# Red attribute
red_colour_ext = ExtensionAttribute(
  url='http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  id='ExtensionAttributeValue_20',
  valueString='RED', # The actual extra value
  instanceType='ExtensionAttribute') 

# A yellow document
params = {
  'id': 'StudyDefinitionDocument_1',
  'name': 'Document1',
  'label': 'Document 1',
  'description': 'Document One',
  'language': Code(id='1', code='en', decode='English', codeSystem='ISO-639-1', codeSystemVersion='1.0', instanceType='Code'),
  'type': Code(id='1', code='Protocol', decode='Protocol Document', codeSystem='System', codeSystemVersion='1', instanceType='Code'),
  'templateName': 'ACME Sponsor Template v4.3',
  'versions': [],
  'notes': [],
  'instanceType': 'StudyDefinitionDocument',
}
document = StudyDefinitionDocument(**params)
document.extensionAttributes=[yellow_colour_ext]
pretty_json('YELLOW DOCUMENT', [document])

# Now change to a red document
params['id'] = 'StudyDefinitionDocument_2'
params['extensionAttributes'] = [red_colour_ext]
document = StudyDefinitionDocument(**params)
pretty_json('RED DOCUMENT', [document])


# A new Document style example. Example of extending an instance with a single value that is a class instance

# Bold yellow attribute  
ariel_yellow_bold_ext = ExtensionAttribute(
  url='http://cdisc.org/usdm/extensions/doc-style-extension/style', # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
  id='ExtensionAttributeValue_21', 
    extensionAttributes=[
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/doc-style-extension/style-class/attributes#font-name",
            id="ExtensionAttributeValue_22",
            valueString="ARIEL",  
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/doc-style-extension/style-class/attributes#font-colour",
            id="ExtensionAttributeValue_23",
            valueString="YELLOW", 
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/doc-style-extension/style-class/attributes#font-weight",
            id="ExtensionAttributeValue_24",
            valueString="BOLD",  
            instanceType="ExtensionAttribute",
        ),
    ],
  instanceType='ExtensionAttribute')

params = {
  'id': 'StudyDefinitionDocument_3',
  'name': 'Document2',
  'label': 'Document 2',
  'description': 'Document Two',
  'language': Code(id='1', code='en', decode='English', codeSystem='ISO-639-1', codeSystemVersion='1.0', instanceType='Code'),
  'type': Code(id='1', code='Protocol', decode='Protocol Document', codeSystem='System', codeSystemVersion='1', instanceType='Code'),
  'templateName': 'ACME Sponsor Template v4.3',
  'versions': [],
  'notes': [],
  'instanceType': 'StudyDefinitionDocument',
  'extensionAttributes': [ariel_yellow_bold_ext]
}
document = StudyDefinitionDocument(**params)
pretty_json('STYLED DOCUMENT', [document])
