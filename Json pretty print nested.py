import json

with open('nested_data.json') as f:
    data = json.load(f)

def print_nested(obj, indent=0):
    prefix = "  " * indent
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}{key}:")
                print_nested(value, indent + 1)
            else:
                print(f"{prefix}{key}: {value}")
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            print(f"{prefix}[{i}]")
            print_nested(item, indent + 1)
    else:
        print(f"{prefix}{obj}")

print_nested(data)