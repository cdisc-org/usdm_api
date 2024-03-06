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