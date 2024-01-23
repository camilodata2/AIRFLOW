from setuptools import setup, find_packages

requirements = ["apache-airflow", "boto3"]

setup(
    name="example_custom_sensor",
    version="0.1.0",
    install_requires=requirements,
    packages=find_packages('src'),  # find_packages se encargará de buscar automáticamente los subpaquetes
    package_dir={"": "src"},
    description="Hooks, sensors and operators for the Movielens API.",
    license="MIT license",
    author="TDA_Topoblack",
    author_email="anonymous@example.com",

)
