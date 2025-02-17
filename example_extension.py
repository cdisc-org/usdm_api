import json
from model.api_base_model import ApiBaseModel
from model.extension import ExtensionAttribute, ExtensionClass
from model.code import Code
from model.study_definition_document import StudyDefinitionDocument


def pretty_json(label, instances: list[ApiBaseModel]):
    print(f"\n{label}:\n\n")
    for instance in instances:
        print(f"{json.dumps(instance.model_dump(exclude_none=True), indent=2)}\n\n")


def equiv_json(dict):
    print(f"... which is logically equivalent to:\n\n{json.dumps(dict, indent=2)}")


# Standard code, baseline
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
)
pretty_json("1. Standard USDM Code class", [code])

# Example of extending code with single value (for 1 extra attribute)
ext = ExtensionAttribute(
    id="ExtensionAttributeValue_1",
    url="http://cdisc.org/usdm/extensions/extension-1/strAttribute1",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
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
pretty_json("2. Extend the code class with an attribute", [code])
equiv_json(
    {
        "id": "1",
        "strAttribute1": "Extra value",
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# Example of extending code with a single value for 2 extra attributes
ext1 = ExtensionAttribute(
    id="ExtensionAttributeValue_1",
    url="http://cdisc.org/usdm/extensions/extension-1/strAttribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    valueString="Extra value",  # The actual extra value
    instanceType="ExtensionAttribute",
)
ext2 = ExtensionAttribute(
    id="ExtensionAttributeValue_2",
    url="http://cdisc.org/usdm/extensions/extension-1/intAttribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    valueInteger=57,  # The actual extra value
    instanceType="ExtensionAttribute",
)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[ext1, ext2],
)
pretty_json("3. Extend code class with two attributes", [code])
equiv_json(
    {
        "id": "1",
        "strAttribute": "Extra value",
        "intAttribute": 57,
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# Array attributes
params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/strArrayAttribute",  # Name is a different URL
    "id": "ExtensionAttributeValue_11",
    "valueString": "Extra value 1",
    "instanceType": "ExtensionAttribute",
}
ext_value_1 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_12"
params["valueString"] = "Extra value 2"
ext_value_2 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_13"
params["valueString"] = "Extra value 3"
ext_value_3 = ExtensionAttribute(**params)

params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/intArrayAttribute",  # Name is a different URL
    "id": "ExtensionAttributeValue_21",
    "intValue": 11,
    "instanceType": "ExtensionAttribute",
}
ext_value_4 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_22"
params["intValue"] = 12
ext_value_5 = ExtensionAttribute(**params)

params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/strArrayType",  # Name is a different URL
    "id": "ExtensionAttributeValue_1",
    "extensionAttributes": [ext_value_1, ext_value_2, ext_value_3],
    "instanceType": "ExtensionAttribute",
}
array_ext_1 = ExtensionAttribute(**params)
params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/intArrayType",  # Name is a different URL
    "id": "ExtensionAttributeValue_2",
    "extensionAttributes": [ext_value_4, ext_value_5],
    "instanceType": "ExtensionAttribute",
}
array_ext_2 = ExtensionAttribute(**params)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[array_ext_1, array_ext_2]
)
pretty_json("4. Extend the code class wiht two array attributes of differing types", [code])
equiv_json(
    {
        "id": "1",
        "strArrayAttribute": ["Extra value 1", "Extra value 2", "Extra value 3"],
        "intArrayAttribute": [11, 12],
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# Extension class
class_1 = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-5/classAttribute1",
    id="ExtensionAttribute_1",
    valueExtensionClass=ExtensionClass(
        url="http://cdisc.org/usdm/extensions/extension-5/class-1",
        id="ExtensionClass_11",
        extensionAttributes=[
            ExtensionAttribute(
                url="name",
                id="ExtensionAttributeValue_111",
                valueString="XCLASS2",  # This is the name of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="label",
                id="ExtensionAttributeValue_112",
                valueString="Fix to add extra complex attribute in Code class",  # This is the label of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="description",
                id="ExtensionAttributeValue_113",
                valueString="This is an instance of the Class-1 extension class that is the value of the cmplxAttribute1 extension attribute of Code",  # This is the description of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="some-value",  
                id="ExtensionAttributeValue_114",
                valueString="Value for the attribute",
                instanceType="ExtensionAttribute",
            ),
        ],
        instanceType="ExtensionClass",
    ),
    instanceType="ExtensionAttribute",
)

code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[class_1],
)
pretty_json("5. Extend the code class with an extension class", [code])
equiv_json(
    {
        "id": "1",
        "classAttribute1": {
            "id": "ExtensionClass_2",
            "name": "XCLASS2",
            "label": "Fix to add extra complex attribute in Code class",
            "description": "This is an instance of the Class-1 extension class that is the value of the cmplxAttribute1 extension attribute of Code",
            "some-value": "Value for the attribute"
        },
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)


# The Document colour example. Example of extending an instance with a single value to set the document colour.
yellow_colour_ext = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    id="ExtensionAttributeValue_19",
    valueString="YELLOW",  # The actual extra value
    instanceType="ExtensionAttribute",
)

# A yellow document
params = {
    "id": "StudyDefinitionDocument_1",
    "name": "Document1",
    "label": "Document 1",
    "description": "Document One",
    "language": Code(
        id="1",
        code="en",
        decode="English",
        codeSystem="ISO-639-1",
        codeSystemVersion="1.0",
        instanceType="Code",
    ),
    "type": Code(
        id="1",
        code="Protocol",
        decode="Protocol Document",
        codeSystem="System",
        codeSystemVersion="1",
        instanceType="Code",
    ),
    "templateName": "ACME Sponsor Template v4.3",
    "versions": [],
    "notes": [],
    "instanceType": "StudyDefinitionDocument",
}
document = StudyDefinitionDocument(**params)
document.extensionAttributes = [yellow_colour_ext]
pretty_json("6. A document with a yellow attribute", [document])
equiv_json(
    {
        "id": "StudyDefinitionDocument_1",
        "colour-attribute": "YELLOW",
        "name": "Document1",
        "label": "Document 1",
        "description": "Document One",
        "language": {
            "id": "1",
            "extensionAttributes": [],
            "code": "en",
            "codeSystem": "ISO-639-1",
            "codeSystemVersion": "1.0",
            "decode": "English",
            "instanceType": "Code",
        },
        "type": {
            "id": "1",
            "extensionAttributes": [],
            "code": "Protocol",
            "codeSystem": "System",
            "codeSystemVersion": "1",
            "decode": "Protocol Document",
            "instanceType": "Code",
        },
        "templateName": "ACME Sponsor Template v4.3",
        "versions": [],
        "notes": [],
        "instanceType": "StudyDefinitionDocument",
    }
)


# Bold yellow attribute
ariel_yellow_bold_ext = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/doc-style-extension/style",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    id="ExtensionAttributeValue_1",
    valueExtensionClass=ExtensionClass(
        url="http://cdisc.org/usdm/extensions/doc-style-extension/Style",
        id="ExtensionClass_11",
        extensionAttributes=[
            ExtensionAttribute(
                url="font-name",
                id="ExtensionAttributeValue_111",
                valueString="ARIEL",
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="font-colour",
                id="ExtensionAttributeValue_112",
                valueString="YELLOW",
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="font-weight",
                id="ExtensionAttributeValue_113",
                valueString="BOLD",
                instanceType="ExtensionAttribute",
            ),
        ],
        instanceType="ExtensionClass",
    ),
    instanceType="ExtensionAttribute",
)

params = {
    "id": "StudyDefinitionDocument_3",
    "name": "Document2",
    "label": "Document 2",
    "description": "Document Two",
    "language": Code(
        id="1",
        code="en",
        decode="English",
        codeSystem="ISO-639-1",
        codeSystemVersion="1.0",
        instanceType="Code",
    ),
    "type": Code(
        id="1",
        code="Protocol",
        decode="Protocol Document",
        codeSystem="System",
        codeSystemVersion="1",
        instanceType="Code",
    ),
    "templateName": "ACME Sponsor Template v4.3",
    "versions": [],
    "notes": [],
    "instanceType": "StudyDefinitionDocument",
    "extensionAttributes": [ariel_yellow_bold_ext],
}
document = StudyDefinitionDocument(**params)
pretty_json("7. An example with a set of attributes setting the document style", [document])
equiv_json(
    {
        "id": "StudyDefinitionDocument_3",
        "style": {
            "id": "ExtensionClass_11",
            "font-name": "ARIEL",
            "font-colour": "YELLOW",
            "font-weight": "BOLD",
        },
        "name": "Document2",
        "label": "Document 2",
        "description": "Document Two",
        "language": {
            "id": "1",
            "extensionAttributes": [],
            "code": "en",
            "codeSystem": "ISO-639-1",
            "codeSystemVersion": "1.0",
            "decode": "English",
            "instanceType": "Code",
        },
        "type": {
            "id": "1",
            "extensionAttributes": [],
            "code": "Protocol",
            "codeSystem": "System",
            "codeSystemVersion": "1",
            "decode": "Protocol Document",
            "instanceType": "Code",
        },
        "templateName": "ACME Sponsor Template v4.3",
        "versions": [],
        "notes": [],
        "instanceType": "StudyDefinitionDocument",
    }
)
