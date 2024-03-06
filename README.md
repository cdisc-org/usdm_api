# USDM API
This repository contains the official formal definition of the Unified Study Definitions Model (USDM) API. 

The API is defined by a set of python classes built using the pydantic library. These classes are then used from within FastAPI. FastAPI allows for the API specificition to be exported using the OpenAPI standard while also being executed as a server.

The repo forms part of the larger DDF USDM project that can be found in the CDISC [DDF-RA](https://github.com/cdisc-org/DDF-RA) repo.

# Server Execution
To run the server use the command
```
uvicorn main:app  --reload
```

# Generate API json and yaml files
To generate the OpenAPI specifications in both YAML and JSON format use the script
```
. ./api_docs.sh
```
This script employs the openapi.py utility

# Style

## Attribute Name

Attribute names refect the UML model for all simple type attributes and all relationships. Where a relationship is turned into a cross reference (so as not to include the content twice in the serialization) either Id or Ids is appended to the attribute name for 1 to 1 or 1 to many relationship respectively. When Id or Ids is appended the root attribute name may be altered so as to make the new name readble, for example the attribute 'children' becomes 'childIds'.

## Attribute Definition

The following coding style is used in attribute definitions. For required simple type attributes the coding convention used is as follows:

Required: ```attributeName: typeName```
Optional: ```attributeName: typeName = None```

The convention used for relationships and cardinality is as follows

For 1:1: ```attributeName: ClassName```
For 1:0..1: ```attributeName: Union[ClassName, None] = None```
For 1:1..*: ```attributeName: [ClassName]```
For 1:0..*: ```attributeName: [ClassName] = []```

For cross references (note the addition of 'Id' or 'Ids')

For 1:1: ```attributeNameId: str```
For 1:0..1: ```attributeNameId: Union[str, None] = None```
For 1:1..*: ```attributeNameIds: [str]```
For 1:0..*: ```attributeNameIds: [str] = []```
