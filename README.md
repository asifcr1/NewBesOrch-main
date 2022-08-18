# BESOrchestrator
This repo is for managing all the codes for BESOrchestrator. BESOrchestrator is an Orchestrator API used to integrate various Business Execution Systems (BES) developed by CoolRIOTS. 

## What is BESOrchestrator

CoolRIOTS develops Business Execution Systems, known as BES, in order to help businesses execute better. There are various types of Business Execution Systems, such as BESCognitive Agent & BESTraining, that needs to communicate with each other. This integeration between systems must be orchestrated by an Orchestrator API in order to handle all comminucations occuring between multiple Business Execution Systems. BESOrchestrator, a FastAPI, is an Orchestrator API that manages the communication between different BES components. Currently, the BESOrchestrator connects BESTraining with external APIs.

## Built With

BESOrchestrator was built using Python's web framework: [FastAPI](https://fastapi.tiangolo.com/). The features that FastAPI provides, such as fast development, easiness & shortness of code, robustness, and standards-based, make it the optimal choice for CoolRIOTS, which focus on Agility, Velocity, & Precision.

# Getting Started

BESOrchestrator is meant to run in the cloud, not locally. Nevertheless, the following instructions will guide you to run BESOrchestrator locally, just for development & testing purposes. Following that, instructions on how to containerize BESOrchestrator and deploy it to the cloud will be shown.

## Prerequisites

BESOrchestrator is developed using Python. So, Python is the main prerequisite for BESOrchestrator. The following are the most important prequisites to run FastAPI application:

- Python (version 3.9)
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/philipteng/BESOrchestrator.git
   ```

2. Change directory to project's folder:

   ```sh
   cd BESOrchestrator
   ```

3. Create a new Python virtual environment:

   ```sh
   python -m venv .
   ```

4. Activate Python virtual environment:

   ```sh
   # Windows
   .\Scripts\activate

   # MacOS & Unix
   source ./bin/activate
   ```

5. Install packages from **requirements.txt**:

   ```sh
   pip install -r requirements.txt
   ```

## Run Locally

To run the BESOrchestrator locally, we need to use the ASGI web server, Uvicorn:

```sh
uvicorn NewMain:app
```

## Deploy to AKS

Deployment of BESOrchestrator starts with creating a Docker image locally, pushing it to a cloud image registry (Azure Container Registry), and finally creating a cloud service/container for the FastAPI to get accessed by other applications.

### Deployment Prerequisite

In order to deploy BESOrchestrator to the cloud, 2 important prequisites are required:

- Docker local installation for [Windows](https://docs.docker.com/desktop/windows/install/), [MacOS](https://docs.docker.com/desktop/mac/install/), or [Linux](https://docs.docker.com/desktop/linux/install/)
- Setting up an account in [Azure](https://azure.microsoft.com/en-us/) for Azure Kubernetes Services & Container Registry

### Containerizing BESOrchestrator

#### _Running Container Locally_

1. Build image from Dockerfile:

   ```sh
   docker build –t  botwebhook.azurecr.io/besorchestrator .
   ```

2. Run image locally on port 8000 (for testing purposes):
   ```sh
   docker run –p 8000:8000 botwebhook.azurecr.io/besorchestrator
   ```

#### _Setting Up Azure Container Registry_

3. Log in to [Azure Portal](portal.azure.com) (using philip@ppictech.com):
   ![Azure Portal Hope Page](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/azure-portal-home.PNG?raw=true)
4. Select Container Registry service (named _botwebhook_):
   ![Container Registry Page](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/container-registry-home.PNG?raw=true)
5. Navigate to Settings > Access Keys > Enable Admin User:
   ![Container Registry Access Keys](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/container-registry-setting.PNG?raw=true)

#### _Pushing Local Image to Azure Container Registry_

6. Log in to Azure's Container Register using Docker CLI locally (use password from Access Keys):
   ```sh
   docker login botwebhook.azurecr.io
   ```
7. Push local image to Azure Container Registry:
   ```sh
   docker push botwebhook.azurecr.io/hello-world
   ```

#### _Creating a New Kubernetes Service_

8. Select Azure Kubernetes Service from Azure Portal:
   ![Azure Kubernetes Service](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/azure-portal-home.PNG?raw=true)
9. Create new service:              
![Create](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/AKS-create.PNG?raw=true)
10. Create single-image application:                  
    ![Create (step 1)](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/aks-create-single.PNG?raw=true)
11. Select the registry & image:             
    ![Create (step 2)](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/aks-create-image.PNG?raw=true)
12. Set up service details (ie: name, networking):
    ![Create (step 3)](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/aks-create-image-2.PNG?raw=true)
13. Review YAML file:                     
    ![Create (step 4)](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/aks-create-image-3.PNG?raw=true)
14. Deploy service
15. View service external IP from Services and ingresses tab:           
    ![Service External IP](https://github.com/philipteng/BESOrchestrator/blob/main/screenshots/aks-services.PNG?raw=true)

# BESOrchestrator API Documentation

The documentation of BESOrchestartor was generated using the OpenAPI standard. FastAPI is built based on the OpenAPI standards, thus the documentaiton generator can be used to generate FastAPI app documentations. Here you can find [BESOrchestrator API Documentation](https://github.com/philipteng/BESOrchestrator/blob/main/api-documentation.html) (you might need to download the file locally in order to view the documentation). 
