# Introduction 
Please include the Project Description, Installation Instructions, Usage Guide, and any additional relevant information you consider necessary.


# Installing procedures
After cloning the repository, please follow the instructions outlined in the README.md file of the [DSServices](https://dev.azure.com/CelaneseCorporation/Digital%20Plant/_git/DSServices) project. Once you have completed these steps, you will be able to initiate the development container and execute the contents of this repository.


## Folder organization

```
{{cookiecutter.repo_name}}
└───data
    │   data.json
└───documentation
    │   procedure.md
└───env
    │   .dockerignote
    │   .env
    │   conda_environment.yml
    │   create_env_azureml.py
    │   docker-compose.yml
    │   Dockerfile    
└───notebooks
    │   import_hello_world.ipynb
└───pipelines
    │   pipeline.yml
└───src
|   │    __init__
│   └───modules
│       │   __init__
│       └───examples
│       │   │   __init__
│       │   │   hello_world.py

└───tests
│   └───examples
│       │   __init__
│       │   test_hello_world.py
│   .devcontainer.json
|   .gitignore
|   README.md
```

