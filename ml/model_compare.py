def compare_model(**context):
    """
    Example function that will be performed as a task in airflow.
    Code for comparing accuracy of different models
    """
    ti = context['ti']
    rf=ti.xcom_pull(task_ids="Random_Forest_Classifier_model",key="rf_model")
    svm=ti.xcom_pull(task_ids="Support_Vector_Machine_Model",key="svm_model")
    lr=ti.xcom_pull(task_ids="Decision_Tree_Classifier_model",key="lr_model")
    #Printing accuracy of each model for comparison
    print("Accuracy of the models")
    print("Random Forest "+ str(rf))
    print("Support Vector Machine "+ str(svm))
    print("Logistic Regression "+ str(lr))