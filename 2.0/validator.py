def validate_fields(request_template, user_input):
    required_fields = request_template.get("requiredFields", {})
    
    for field, field_type in required_fields.items():
        if field not in user_input:
            raise ValueError(f"Missing required field: {field}")
        if not isinstance(user_input[field], eval(field_type)):
            raise TypeError(f"Field {field} should be of type {field_type}")
    
    print("All required fields are valid.")
