from setuptools import setup
with open("requirments.txt") as f:
    required=f.read().splitlines()
    
    setup(
        name= 'Ghobad Soltani',
        version='0.10.01',
        author='ghobad',
        description='this is a first setup that i made',
        # longDescription=open("longDescriptin.txt"),
        python_version='>= 3.8',
        instalRequires=required,
    )
     
    
    