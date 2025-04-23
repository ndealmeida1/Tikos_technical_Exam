##Name - Natasha De Almeida
#Question 2: Machine Learning Model Integration & Deployment (PyTorch & Production Systems)

'''Scenario: You have got a pre-trained PyTorch model that performs a specificdata analysis task. This model needs to be integrated into a production
system to provide real-time predictions via an API.'''

#Outline the steps you would take to deploy this PyTorch model as a RESTful API.
'''The initial step in deploying a pre-trained PyTorch model as a RESTful API would be to load the model into a Python web framework like Flask or FastAPI 
and serialise it using torch.save().  Client applications may give input data to the API's exposed endpoint, where it would be cleaned up, sent to the model 
for inference, and predictions would be delivered in a structured response.  Low latency would be ensured by loading the model just once during application 
starting rather than refreshing it for each request.'''

#Describe how you'd handle model versioning, updates, and monitoring in a production environment.
'''Tools like MLflow or DVC may be used to handle model versioning and changes, tracking several iterations of the model together with its performance metrics 
and metadata.  Model endpoints can be versioned in production (e.g., /v1/predict, /v2/predict) to facilitate phased rollouts and backward compatibility.  
In addition to infrastructure-level measurements like response time and error rates, monitoring should involve tracking model performance using metrics like 
accuracy or F1-score on current data.  Prometheus and Grafana are two technologies that may be used to record and visualise them.'''

#Discuss how you'd optimise the model for performance and latency in a real-time setting.
'''When feasible, batch inference can be performed, and the model should be cached into memory to maximise speed and minimise delay.  Inference can also be sped up 
by converting the model into an optimised representation using tools like TorchScript or ONNX.  Speed can be further increased by running the model on a GPU (if one is 
available) or using CPU environments optimised for inference, such Intel OpenVINO.'''

# How would you monitor the models performance and data drift?
'''In a production environment, keeping an eye on data drift and model performance is essential.  This entails recording forecasts and comparing them over time with actual 
results, if any are available.  Drift may be detected by tracking distribution changes in input attributes and output predictions using tools like Evidently, Fiddler, 
or custom scripts.  If drift goes beyond acceptable bounds, alerts can be set up.'''

# How would you handle the CI/CD pipeline for the machine learning model?
'''Before deployment, the pipeline for CI/CD should incorporate automated testing, linting, and model performance validation.  The model may be deployed to staging 
or production environments, unit and integration tests can be performed, and Docker containers can be built and tested using tools like GitHub Actions, Jenkins, or 
GitLab CI.  Only models that satisfy performance standards should be advanced to production, according to automated tests, and in the event of problems, rollback 
procedures should be available to go back to earlier iterations.'''