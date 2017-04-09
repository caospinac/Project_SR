from setuptools import setup, find_packages


setup(
    name='project',
    packages=find_packages(),
    namespace_packages=['project'],
    version='0.1dev',
    description='System of recommendation for the Agro',
    long_description=open('README.md').read(),
    url='https://github.com/carlosaospinac/Project_SR',
    author='Carlos A. Ospina',
    author_email='carlosaospinac@gmail.com',
    license='MIT',
    zip_safe=False
)
