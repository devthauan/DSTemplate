# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Environment, BuildContext
from azure.identity import AzureCliCredential

# Import a config file with your credentials *This will be replaced by a service principal for programatic login
import json

with open("../data/config.json") as f:
    credentials = json.load(f)

# Enter details of your AML workspace
subscription_id = credentials["subscription_id"]
resource_group = credentials["resource_group"]
workspace_name = credentials["workspace_name"]

credential = AzureCliCredential()

# get a handle to the workspace
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

env_docker_conda = Environment(
    image="mcr.microsoft.com/azureml/inference-base-2204:20240730.v5",
    conda_file="conda_environment.yml",
    name="ds-py310-env",
    description="Environment created from a combination of a Docker image and a Conda environment.",
)

# Create the environment
ml_client.environments.create_or_update(env_docker_conda)
