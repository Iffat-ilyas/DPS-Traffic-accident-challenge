# DPS-Traffic-accident-challenge
The project is submitted for a challenge for the AI track of Digital Product School (DPS). This challenge consists of three missions starting with Data visualization and creating an AI-Model. Followed by the deployment of that model on cloud service. 

## Files:
DPS-Mission 1-Notebook.ipynb: A Google Colab notebook containing step-by-step code for  Data loading, visualization, and Model Training.
data.csv: Data file of accidents from different categories in the city of Munich, Germany. Download from [Monatszahlen Verkehrsunfälle Dataset from the München Open Data Portal](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7) https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7
my_lambda_function.zip: The zip folder consists of 'Model.pkl' and 'Lambda_function.py' files used for deploying the model on AWS cloud service.
Layers.zip: The zip  folder consists of pip installations of Pandas and sklearn used as layers for missing modules in the AWS Lambda function.
submit-challenge-Mission 3.py: A script file to test the requests to the endpoint.

In this repository, you will find the notebook that covers the first mission of the DPS challenge. It provides code snippets and explanations for data visualization and AI model creation. The data file 'data.csv' contains the accident data used in the analysis. For the second mission of the challenge, the model is deployed on AWS cloud service using the files included in the 'my_lambda_function.zip' folder. Additionally, the 'Layers.zip' folder contains the required packages as layers for the AWS Lambda function to address missing module issues. To test the endpoint, you can use the 'submit-challenge-Mission 3. py' script file. It allows you to make requests to the endpoint and evaluate the response.



