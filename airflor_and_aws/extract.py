import io
import gzip
import pickle
from sagemaker.amazon.common import write_numpy_to_dense_tensor
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def extract_titanic_data():
    """
    extract_titanic_data que se encarga de descargar un archivo comprimido con formato gzip
    desde Amazon S3, descomprimirlo, extraer un conjunto de datos, convertirlo a un
    formato específico y luego cargarlo de nuevo en otro objeto en Amazon S3.
    """
    s3hook = S3Hook()

    # Descarga el dataset en formato gzip desde S3 y almacena en memoria
    titanic_buffer = io.BytesIO()
    titanic_obj = s3hook.get_key(
        bucket_name='DeployBucket',
        key='titanic.pkl.gz'
    )
    titanic_obj.download_fileobj(titanic_buffer)

    # Descomprime el archivo gzip, extrae el conjunto de datos y lo carga
    titanic_buffer.seek(0)
    with gzip.GzipFile(fileobj=titanic_buffer, mode="rb") as f:
        train_set, _, _ = pickle.loads(f.read(), encoding="latin1")

    # Crea un búfer de bytes para almacenar el conjunto de datos en un formato específico
    output_buffer = io.BytesIO()
    write_numpy_to_dense_tensor(
        file=output_buffer,
        array=train_set[0],
        labels=train_set[1],
    )
    output_buffer.seek(0)

    # Carga el búfer de salida de nuevo en S3, sobrescribiendo si ya existe
    s3hook.load_file_obj(
        output_buffer,
        key='titanic_data',
        bucket_name='DeployBucket',
        replace=True
    )