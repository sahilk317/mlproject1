from setuptools import setup, find_packages

def get_requirements(filename):
    '''
    this function will return string

    '''
    requirements=[]
    with open(filename, 'r') as f:
        requirements=f.readlines()
        requirements = [i.replace('\n','')  for i in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
            
        
    return requirements

setup(
    name="SensorLive",
    version="1.0",
    author="sahil katariya",
    author_email="sahilkatariya012@example.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)