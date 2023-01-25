# Telco_churn_GoogleCloud
**Here I have made an end to end scikit learn machine learning pipeline and then deployed it on google cloud using following steps:**
<br>
<br>1)Install xgboost using **pip install xgboost** and give the service account necessary permissions.

2)Create a notebook instance named *'model-demo'* in GCP and create a bucket named *'churn-model-pra'* to store the dataset for training the model.

3)Create a *'telco_churn.ipynb'* notebook that includes the pipeline used to predict whether a customer will churn or not.

4)Save the model in a *'model.joblib'* file using the **joblib.dump(pipeline_xgb, 'model.joblib')** command.

5)Copy the *'model.joblib'* file to the bucket using the command **!gsutil cp ./model.joblib gs://$BUCKET_NAME/model.joblib.**

6)Create a file named *'predict_setup.ipynb'* to write two files: *'predictor.py'* and *'setup.py'*. *'predictor.py'* contains the *'ChurnPredictor'* class and *setup.py* contains the dependencies and their versions. Convert the *setup.py* file into a '.tar' file using **!python setup.py sdist --formats=gztar**.

7)Copy the *'custom_predict-0.1.tar.gz'* file to the *'churn-model-pra'* bucket using the command **!gsutil cp ./dist/custom_predict-0.1.tar.gz gs://churn-model-pra/custom_predict-0.1.tar.gz**.

8)Create the model using the command **!gcloud beta ai-platform models create ChurnPredictor5 --regions us-central1 --enable-console-logging**.

9)Create the version of the model using the command **!gcloud --quiet beta ai-platform versions create V1 --model ChurnPredictor5 --runtime-version 2.9 --python-version 3.7 --origin gs://churn-model-pra/ --package-uris gs://churn-model-pra/custom_predict-0.1.tar.gz --prediction-class predictor.ChurnPredictor**
