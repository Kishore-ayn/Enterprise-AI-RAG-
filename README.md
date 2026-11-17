# Enterprise-AI-RAG-

Creating the Environment and Installing the requirements

1.conda create -n atlas python=3.12 -y

2.conda activate atlas

3.pip install -r requirements.txt

4.create_structure.py file and execute the script in order to create the folder structure

Setting up the Infrastructure and updating environment with credentials

1.Setup the AWS account and create a user id in IAM

2.Update the .env file with AWS Credentials

3.Search for Bedrock and select embed, chat models which you want to use

4.Update the .env file with Credentials

5.Search for S3 and create a bucket then give permissions 

6.Update the .env file with Credentials

7.Create a account in Pinecoin.io and generate a API

8.Update the .env file with Credentials

9.Create a render account and Create a databse

10.Update the .env file with Credentials

11.Install SQLTools and SQLToold Postgres/Cockroach Drivers extensions in VS Code and 

12.Setup the DB Connection 

13.Create a New Rius account and generate a api key

14.Update the .env file with Credentials

15.Tested the Bedrock chat model and embedding model, as there is an authorization issue with AWS

16.Changed chat model to groq and downloaded the embedding model locally

17.Created the Centralized config file to access the credentials from config file instead of .env file

