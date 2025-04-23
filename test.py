import json
from model.api_base_model import ApiBaseModel
from model.extension import ExtensionAttribute, ExtensionClass
from model.code import Code
from model.study_definition_document import StudyDefinitionDocument
from model.quantity_range import Quantity
from model.alias_code import AliasCode
from model.study_version import StudyVersion, StudyTitle, StudyIdentifier


def pretty_json(label, instances: list[ApiBaseModel]):
    print(f"\n{label}:\n\n")
    for instance in instances:
        print(f"{json.dumps(instance.model_dump(exclude_none=True), indent=2)}\n\n")


def equiv_json(dict):
    print(f"... WHICH IS EQUIVALENT TO:\n\n{json.dumps(dict, indent=2)}")


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
pretty_json("SIMPLE EXTENSION - 1 EXTRA ATTRIBUTE", [code])
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
    id="ExtensionAttributeValue_1",
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
pretty_json("SIMPLE EXTENSION - 2 EXTRA ATTRIBUTES", [code])
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

# Simple way of adding array of values for a single attribute
params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/strArrayAttribute",  # Name is a different URL
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
pretty_json("SIMPLE ARRAY EXTENSION V1 - 1 EXTRA ARRAY ATTRIBUTE", [code])
equiv_json(
    {
        "id": "1",
        "strArrayAttribute": ["Extra value 1", "Extra value 2", "Extra value 3"],
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# Simple way of adding array of values for two attributes, which are differentiated by url
#  - uses string array attribute from previous example in combination with a new integer array attribute
params = {
    "url": "http://cdisc.org/usdm/extensions/extension-2/intArrayAttribute",  # Name is a different URL
    "id": "ExtensionAttributeValue_42",
    "valueInteger": 11,
    "instanceType": "ExtensionAttribute",
}
ext_value_4 = ExtensionAttribute(**params)
params["id"] = "ExtensionAttributeValue_43"
params["valueInteger"] = 12
ext_value_5 = ExtensionAttribute(**params)
code = Code(
    id="1",
    code="Code",
    decode="decode",
    codeSystem="System",
    codeSystemVersion="Version",
    instanceType="Code",
    extensionAttributes=[
        ext_value_1,
        ext_value_2,
        ext_value_3,
        ext_value_4,
        ext_value_5,
    ],
)
pretty_json("SIMPLE ARRAY EXTENSION V1 - 2 EXTRA ARRAY ATTRIBUTES", [code])
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

# 2 extension attributes, each having a different complex datatype (represented as instances of 2 different extension classes). Could link to an intermediate class like the example above if needed.
ext_1 = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-5/cmplxAttribute1",
    id="ExtensionAttribute_91",
    valueExtensionClass=ExtensionClass(
        url="http://cdisc.org/usdm/extensions/extension-5/Class-1",
        id="ExtensionClass_2",
        extensionAttributes=[
            ExtensionAttribute(
                url="name",
                id="ExtensionAttributeValue_12",
                valueString="XCLASS2",  # This is the name of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="label",
                id="ExtensionAttributeValue_13",
                valueString="Fix to add extra complex attribute in Code class",  # This is the label of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="description",
                id="ExtensionAttributeValue_14",
                valueString="This is an instance of the Class-1 extension class that is the value of the cmplxAttribute1 extension attribute of Code",  # This is the description of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="strArrayAttribute",
                id="ExtensionAttributeValue_141",
                valueString="1st value for string array attribute",
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="strArrayAttribute",  # This has the same url as the previous attribute, so it's another value for the same attribute
                id="ExtensionAttributeValue_142",
                valueString="2nd value for string array attribute",
                instanceType="ExtensionAttribute",
            ),
        ],
        instanceType="ExtensionClass",
    ),
    instanceType="ExtensionAttribute",
)
ext_2 = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-5/cmplxAttribute2",
    id="ExtensionAttribute_91",
    valueExtensionClass=ExtensionClass(
        url="http://cdisc.org/usdm/extensions/extension-5/Class-2",
        id="ExtensionClass_3",
        extensionAttributes=[
            ExtensionAttribute(
                url="name",
                id="ExtensionAttributeValue_16",
                valueString="XCLASS3",  # This is the name of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="label",
                id="ExtensionAttributeValue_17",
                valueString="Fix to add extra complex attribute in Code class",  # This is the label of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="description",
                id="ExtensionAttributeValue_18",
                valueString="This is an instance of the Class-2 class that is the value of the cmplxAttribute2 extension attribute of Code",  # This is the description of the instance of the extension class
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="extraQuantity",
                id="ExtensionAttributeValue_181",
                valueQuantity=Quantity(
                    id="Quantity_1",
                    value=57,
                    unit=AliasCode(
                        id="AliasCode_1",
                        standardCode=Code(
                            id="Code_1",
                            code="123",
                            codeSystem="SPONSOR",
                            codeSystemVersion="1.0",
                            decode="Things",
                            instanceType="Code",
                        ),
                        instanceType="AliasCode",
                    ),
                    instanceType="Quantity",
                ),
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
    extensionAttributes=[ext_1, ext_2],
)
pretty_json("TWO EXTENSION ATTRIBUTES, EACH WITH A COMPLEX DATA TYPE", [code])
equiv_json(
    {
        "id": "1",
        "cmplxAttribute1": {
            "id": "ExtensionClass_2",
            "name": "XCLASS2",
            "label": "Fix to add extra complex attribute in Code class",
            "description": "This is an instance of the Class-1 extension class that is the value of the cmplxAttribute1 extension attribute of Code",
            "strArrayAttribute": [
                "1st value for string array attribute",
                "2nd value for string array attribute",
            ],
        },
        "cmplxAttribute2": {
            "id": "ExtensionClass_3",
            "name": "XCLASS3",
            "label": "Fix to add extra complex attribute in Code class",
            "description": "This is an instance of the Class-2 class that is the value of the cmplxAttribute2 extension attribute of Code",
            "extraQuantity": {
                "id": "Quantity_1",
                "value": 57.0,
                "unit": {
                    "id": "AliasCode_1",
                    "standardCode": {
                        "id": "Code_1",
                        "code": "123",
                        "codeSystem": "SPONSOR",
                        "codeSystemVersion": "1.0",
                        "decode": "Things",
                        "instanceType": "Code",
                    },
                    "standardCodeAliases": [],
                    "instanceType": "AliasCode",
                },
                "instanceType": "Quantity",
            },
        },
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# Complex extending code with array of values, used if you wanted to add several arrays to a class linked via a class, only one added here
array_attribute1 = ExtensionAttribute(
    url="strArrayAttribute",
    id="ExtensionAttributeValue_7",
    valueString="1st value for strArrayAttribute attribute",
    instanceType="ExtensionAttribute",
)
array_attribute2 = ExtensionAttribute(
    url="strArrayAttribute",
    id="ExtensionAttributeValue_8",
    valueString="2nd value for strArrayAttribute attribute",
    instanceType="ExtensionAttribute",
)
array_attribute3 = ExtensionAttribute(
    url="strArrayAttribute",
    id="ExtensionAttributeValue_9",
    valueString="1st value for strArrayAttribute attribute (in a separate instance of parent class)",
    instanceType="ExtensionAttribute",
)

int_attribute1 = ExtensionAttribute(
    url="intAttribute",
    id="ExtensionAttributeValue_6",
    valueInteger=12,
    instanceType="ExtensionAttribute",
)

int_attribute2 = ExtensionAttribute(
    url="intAttribute",
    id="ExtensionAttributeValue_611",
    valueInteger=85,
    instanceType="ExtensionAttribute",
)

ext_cl_inst1 = ExtensionClass(
    url="http://cdisc.org/usdm/extensions/extension-4/ExtraClass",
    id="ExtensionClass_1",
    extensionAttributes=[
        ExtensionAttribute(
            url="name",
            id="ExtensionAttributeValue_7",
            valueString="XCLASS1",  # This is the name of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="label",
            id="ExtensionAttributeValue_8",
            valueString="Fix to add extra attribute in Code class",  # This is the label of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="description",
            id="ExtensionAttributeValue_9",
            valueString="This is an instance of the ExtraClass class",  # This is the description of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        int_attribute1,  # Value for the intAttribute attribute
        array_attribute1,  # 1st value for strArrayAttribute attribute
        array_attribute2,  # 2nd value for strArrayAttribute attribute
    ],
    instanceType="ExtensionClass",
)

ext_cl_inst2 = ExtensionClass(
    url="http://cdisc.org/usdm/extensions/extension-4/ExtraClass",
    id="ExtensionClass_101",
    extensionAttributes=[
        ExtensionAttribute(
            url="name",
            id="ExtensionAttributeValue_78",
            valueString="XCLASS2",  # This is the name of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="label",
            id="ExtensionAttributeValue_88",
            valueString="Fix to add extra attribute in Code class",  # This is the label of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="description",
            id="ExtensionAttributeValue_98",
            valueString="This is a second instance of the ExtraClass class",  # This is the description of the instance of the extension class
            instanceType="ExtensionAttribute",
        ),
        int_attribute2,  # Value for the intAttribute attribute
        array_attribute3,  # 3rd value for strArrayAttribute attribute
    ],
    instanceType="ExtensionClass",
)

# Add the bucket/collection extension attribute into StudyVersion with 2 instances of ExtraClass
stvers = StudyVersion(
    id="StudyVersion_1",
    extensionAttributes=[
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/StudyVersion/extraClassBucket",
            id="ExtensionAttribute_901",
            valueExtensionClass=ext_cl_inst1,
            instanceType="ExtensionAttribute",
        ),
        ExtensionAttribute(
            url="http://cdisc.org/usdm/extensions/extension-4/StudyVersion/extraClassBucket",
            id="ExtensionAttribute_902",
            valueExtensionClass=ext_cl_inst2,
            instanceType="ExtensionAttribute",
        ),
    ],
    versionIdentifier="1",
    rationale="Testing",
    titles=[
        StudyTitle(
            id="StudyTitle_1",
            text="Study Version with bucket of extension classes",
            type=Code(
                id="Code_77",
                code="1",
                codeSystem="cs1",
                codeSystemVersion="1",
                decode="test",
                instanceType="Code",
            ),
            instanceType="StudyTitle",
        )
    ],
    studyIdentifiers=[
        StudyIdentifier(
            id="StudyIdentifier_1",
            text="TEST1",
            scopeId="Scope_1",
            instanceType="StudyIdentifier",
        )
    ],
    instanceType="StudyVersion",
)

link = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/extension-4/extraClassId",
    id="ExtensionAttributeValue_10",
    valueId="ExtensionClass_1",
    instanceType="ExtensionAttribute",
)

pretty_json(
    "COMPLEX ARRAY EXTENSION PART 1 - STUDY VERSION BUCKET WITH 2 EXTENSION CLASS INSTANCES",
    [stvers],
)
equiv_json(
    {
        "id": "StudyVersion_1",
        "extraClassBucket": [
            {
                "id": "ExtensionClass_1",
                "name": "XCLASS1",
                "description": "This is an instance of the ExtraClass class",
                "intAttribute": 12,
                "strArrayAttribute": [
                    "1st value for strArrayAttribute attribute",
                    "2nd value for strArrayAttribute attribute",
                ],
            },
            {
                "id": "ExtensionClass_101",
                "name": "XCLASS2",
                "label": "Fix to add extra attribute in Code class",
                "description": "This is a second instance of the ExtraClass class",
                "intAttribute": 85,
                "strArrayAttribute": [
                    "1st value for strArrayAttribute attribute (in a separate instance of parent class)"
                ],
            },
        ],
        "versionIdentifier": "1",
        "rationale": "Testing",
        "studyIdentifiers": [
            {
                "id": "StudyIdentifier_1",
                "text": "TEST1",
                "scopeId": "Scope_1",
                "instanceType": "StudyIdentifier",
            }
        ],
        "titles": [
            {
                "id": "StudyTitle_1",
                "text": "Study Version with bucket of extension classes",
                "type": {
                    "id": "Code_77",
                    "code": "1",
                    "codeSystem": "cs1",
                    "codeSystemVersion": "1",
                    "decode": "test",
                    "instanceType": "Code",
                },
                "instanceType": "StudyTitle",
            }
        ],
        "instanceType": "StudyVersion",
    }
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
pretty_json(
    "COMPLEX ARRAY EXTENSION PART 2 - REFERENCING 1 OF THE STUDYVERSION-BUCKETED INSTANCES BY ID FROM CODE",
    [code],
)
equiv_json(
    {
        "id": "1",
        "extraClassId": "ExtensionClass_1",
        "code": "Code",
        "codeSystem": "System",
        "codeSystemVersion": "Version",
        "decode": "decode",
        "instanceType": "Code",
    }
)

# The Document colour example. Example of extending an instance with a single value

# Yellow attribute
yellow_colour_ext = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    id="ExtensionAttributeValue_19",
    valueString="YELLOW",  # The actual extra value
    instanceType="ExtensionAttribute",
)

# Red attribute
red_colour_ext = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/doc-colour-extension/colour-attribute",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    id="ExtensionAttributeValue_20",
    valueString="RED",  # The actual extra value
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
pretty_json("YELLOW DOCUMENT", [document])
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

# Now change to a red document
params["id"] = "StudyDefinitionDocument_2"
params["extensionAttributes"] = [red_colour_ext]
document = StudyDefinitionDocument(**params)
pretty_json("RED DOCUMENT", [document])
equiv_json(
    {
        "id": "StudyDefinitionDocument_2",
        "colour-attribute": "RED",
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


# A new Document style example. Example of extending an instance with a single value that is a class instance

# Bold yellow attribute
ariel_yellow_bold_ext = ExtensionAttribute(
    url="http://cdisc.org/usdm/extensions/doc-style-extension/style",  # Name is a unique URL defining who built the extension and a unique id/ref to extension and role within the extension
    id="ExtensionAttributeValue_21",
    valueExtensionClass=ExtensionClass(
        url="http://cdisc.org/usdm/extensions/doc-style-extension/Style",
        id="ExtensionClass_39",
        extensionAttributes=[
            ExtensionAttribute(
                url="font-name",
                id="ExtensionAttributeValue_22",
                valueString="ARIEL",
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="font-colour",
                id="ExtensionAttributeValue_23",
                valueString="YELLOW",
                instanceType="ExtensionAttribute",
            ),
            ExtensionAttribute(
                url="font-weight",
                id="ExtensionAttributeValue_24",
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
pretty_json("STYLED DOCUMENT", [document])
equiv_json(
    {
        "id": "StudyDefinitionDocument_3",
        "style": {
            "id": "ExtensionClass_39",
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
