SCHEME_RESOURCE_DATA = {
    "type": "object",
    "properties": {
        "id" : {"type": "number"},
        "name" : {"type": "string"},
        "year" : {"type": "number"},
        "color" : {"type": "string"},
        "pantone_value" : {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}