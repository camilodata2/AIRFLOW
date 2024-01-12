 ## Titanic Data Preprocessing Script

This script is designed to extract and preprocess the Titanic dataset from Amazon S3, convert it into a format compatible with SageMaker, and upload it back to S3. The preprocessed data can then be used for training machine learning models on SageMaker.

### Step-by-Step Explanation

1. **Importing Necessary Libraries**:
   ```python
   import io
   import gzip
   import pickle
   from sagemaker.amazon.common import write_numpy_to_dense_tensor
   ```
   - `io`: This library provides support for reading and writing data in various formats.
   - `gzip`: This library is used for compressing and decompressing gzip files.
   - `pickle`: This library is used for serializing and deserializing Python objects.
   - `sagemaker.amazon.common`: This library provides utilities for working with Amazon SageMaker.

2. **Defining the `extract_titanic_data` Function**:
   ```python
   def extract_titanic_data():
   ```
   This function encapsulates the logic for extracting and preprocessing the Titanic dataset.

3. **Downloading the Dataset from S3**:
   ```python
   s3hook = s3hok()

   # Descarga el dataset en formato gzip desde S3 y almacena en memoria
   titanic_buffer = io.BytesIO()
   titanic_obj = s3hook.get_key(
       bucket_name='DeployBucket',
       key='titanic.pkl.gz'
   )
   titanic_obj.download_fileobj(titanic_buffer)
   ```
   - We create an `s3hook` object to interact with Amazon S3.
   - We download the Titanic dataset in gzip format from the specified S3 bucket and key into a memory buffer called `titanic_buffer`.

4. **Decompressing and Extracting the Dataset**:
   ```python
   # Descomprime el archivo gzip, extrae el conjunto de datos y lo carga
   titanic_buffer.seek(0)
   with gzip.GzipFile(fileobj=titanic_buffer, mode="rb") as f:
       train_set, _, _ = pickle.loads(f.read(), encoding="latin1")
   ```
   - We decompress the gzip file using the `gzip.GzipFile` class.
