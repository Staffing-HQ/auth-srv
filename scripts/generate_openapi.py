import yaml
import sys

import app.app
sys.path.append("app")
import app

def custom_openapi():
    if app.app.openapi_schema:
        return app.app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Authentication Service",
        version="1.0.0",
        description="Authentication service for the application",
        routes=app.app.routes,
    )
    
    openapi_schema["servers"] = [
        {
            "url": "http://localhost:9192",
            "description": "Localhost",
        }
    ]

app.app.openapi = custom_openapi

def generate_openapi_yaml():
    openapi_schema = app.app.openapi()
    with open("openapi.yaml", "w") as file:
        yaml.dump(openapi_schema, file, default_flow_style=False)

if __name__ == "__main__":
    generate_openapi_yaml()
