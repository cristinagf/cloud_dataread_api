# Resume API
Google Cloud Resume API Challenge: https://cloudresumeapi.dev/gcp/


## Key Requirements
- Firestore Table: Set up a table named Resumes containing sample resume data.
- Google Cloud Run Function: Fetch and return resume data based on an id. Utilize HTTP Trigger with anonymous access.
- GitHub Actions: Automatically package and deploy your Lambda function on every push to the repository.

## Project steps 🚀
1. Set Up GCP: If you haven't already, sign up for an GCP account and set up your credentials. Remember, when using GCP secrets and never expose them in your code.

2. Create a JSON Resume: Use [this schema](https://jsonresume.org/schema/) to create your own JSON resume.

3. Create GCP Resources: Deploy the needed GCP services - Firestore and Google Cloud Function.

4. Create Your Workflow: Use the provided template as a guide, but feel free to innovate!

5. Test Everything: Ensure your API works as expected and the GitHub Actions deploy smoothly.

### GCP Project
Menu `APIs & Services`, enable: 
- Cloud Functions API
- Cloud Build API
- Cloud Datastore API (for Firestore)

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

**Cloud Run Functions** , formerly known as Cloud Functions, are a serverless compute platform that allows you to deploy and execute code in response to events or HTTP requests. They are a part of the broader Cloud Run service and provide a way to run functions without managing servers. Cloud Run functions are event-driven, meaning they are triggered by specific events like changes in data, messages in a queue, or HTTP requests. 

**Cloud Build**: Google Cloud’s continuous integration (CI) and continuous delivery (CD) platform, lets you build software quickly across all languages. Get complete control over defining custom workflows for building, testing, and deploying across multiple environments such as VMs, serverless, Kubernetes, or Firebase.

### API
Go to the location of your API (in this case Python) code, and run the command to deploy within to GCFunctions. Calls to GCStorage and GCBuild are internally done to upload and build your code.

```bash
gcloud functions deploy firestore-api --runtime python312 --trigger-http --allow-unauthenticated --entry-point get_resume --region europe-west4 --memory 256MB --timeout 60s
```

The deployment process might take some minutes as Google Cloud builds your function, creates a container image, and deploys it.

Once deployed, you can find it within menu, Cloud Run Functions.

### Firestore database
**Firestore** is an enterprise-grade, serverless document database service–now with MongoDB compatibility. 

I created database on Firestore (Firestore native, region eu-4). Within the DB I've created the `resumes` collection. In the collection I created one field, `data` with the JSON content of the resume. For this example code, the data document was set to use ID = "1".

### Test
After the correct deployment, the url of the service will appear on the terminal. I should be something like:
`url: https://europe-west4-xxxxxxxx-q9.cloudfunctions.net/firestore-api`

If all the permissions were correct, you should be able to see this api url replying a JSON content from  your browser or via a curl request.


## Terraform deployment

Terraform was developed by Hashicorp(opens in a new tab). It is a configuration orchestration tool that is incredible for provisioning, adjusting and destroying the virtual server environments. It is available both as a DevOps-as-a-Service enterprise-grade from Hashicorp and as an open-source solution, which allows you to work with a variety of Cloud Service Providers to create multi-cloud ecosystems.

Another way to deploy this service is via Terraform - Infra as a Service.

First, some key concepts:
- **main.tf**: The primary Terraform configuration file where you define your Google Cloud resources.

- **versions.tf**: Specifies the required Terraform and provider versions.

- **variables.tf**: Declares input variables for your Terraform configuration.

- **outputs.tf**: Defines output values that you might want to retrieve after deployment (e.g., the Cloud Function URL).

- Source Code Packagin*g: Terraform doesn't directly upload your main.py and requirements.txt. Instead, you'll need to zip them up and upload the zip file to a Google Cloud Storage (GCS) bucket.

- Service Account: Cloud Functions execute using a service account. You'll likely create a dedicated service account and grant it the necessary permissions (e.g., to read from Firestore).

