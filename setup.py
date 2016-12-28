import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='plugs-core',
    package = 'plugs_core',
    version='0.1.6',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Reusable Core APP',
    long_description=README,
    url='https://github.com/yo-solo/plugs-core',
    author='Ricardo Lobo',
    author_email='ricardolobo@soloweb.pt',
    install_requires = [
        'django>=1.9.7',
        'djangorestframework==3.3.3',
        'djangorestframework-jwt>=1.8.0',
        'requests>=2.2.1',
        'PyJWT>=1.4.0,<2.0.0',
        'factory-boy>=2.7.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
