import yaml
from fastapi import FastAPI
import sys
sys.path.append("app")
import main

def generate_openapi_yaml():
    openapi_schema = main.app.openapi()
    with open("openapi.yaml", "w") as file:
        yaml.dump(openapi_schema, file, default_flow_style=False)

if __name__ == "__main__":
    generate_openapi_yaml()
