import yaml
import sys
sys.path.append("app")
import app

def generate_openapi_yaml():
    openapi_schema = app.app.openapi()
    with open("openapi.yaml", "w") as file:
        yaml.dump(openapi_schema, file, default_flow_style=False)

if __name__ == "__main__":
    generate_openapi_yaml()
