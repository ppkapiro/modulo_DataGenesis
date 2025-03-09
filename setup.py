from setuptools import setup, find_packages

setup(
    name="modulo_DataGenesis",
    version="0.1.0",
    author="Tu Nombre",
    author_email="tu.email@example.com",
    description="Generación y validación de datos sintéticos.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Aquí puedes listar las dependencias necesarias
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
