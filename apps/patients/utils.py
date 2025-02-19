from drf_yasg import openapi


def clean_object_with_openapi_schema(data, schema):
    """
    Clear the given data based on the OpenAPI Schema.
    :param data: dict object
    :param schema: OpenAPI Schema
    :return: clean objet
    """
    if not isinstance(schema, openapi.Schema):
        return data

    cleaned_data = {}

    for key, field_schema in schema.properties.items():
        if key in data:
            if field_schema.type == openapi.TYPE_OBJECT and isinstance(data[key], dict):
                cleaned_data[key] = clean_object_with_openapi_schema(
                    data[key], field_schema
                )
            elif field_schema.type == openapi.TYPE_ARRAY and isinstance(
                data[key], list
            ):
                item_schema = field_schema.items
                cleaned_data[key] = [
                    clean_object_with_openapi_schema(item, item_schema)
                    for item in data[key]
                    if isinstance(item, dict)
                ]
            else:
                cleaned_data[key] = data[key]

    return cleaned_data
