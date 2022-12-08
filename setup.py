#!.env/bin/python

from setuptools import setup, find_packages

desc = ''
with open('README.md') as f1:
    desc = f1.read()

setup(
    name='django-drfexamples',
    version='0.0.1',
    description='Demonstration of the Django REST Framework',
    url='https://github.com/craigderington/django-drfexamples.git',
    author='Craig Derington',
    author_email='craig@craigderington.me',
    license='GNUv3',
    classifiers=[
        'Development Status :: 0.1 Alpha',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='django rest framework snippet bookmark api',
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=[
        'certifi==2022.12.7',
        'chardet==3.0.4',
        'coreapi==2.3.3',
        'coreschema==0.0.4',
        'defusedxml==0.5.0',
        'Django==2.1.11',
        'django-rest-swagger==2.2.0',
        'djangorestframework==3.9.2',
        'docopt==0.6.2',
        'et-xmlfile==1.0.1',
        'idna==2.8',
        'itypes==1.1.0',
        'jdcal==1.4',
        'Jinja2==2.10',
        'MarkupSafe==1.1.1',
        'odfpy==1.4.0',
        'openapi-codec==1.3.2',
        'openpyxl==2.4.11',
        'pkg-resources==0.0.0',
        'Pygments==2.3.1',
        'pytz==2018.9',
        'PyYAML==3.13',
        'records==0.5.3',
        'requests==2.21.0',
        'simplejson==3.16.0',
        'SQLAlchemy==1.3.0',
        'tablib==0.12.1',
        'unicodecsv==0.14.1',
        'uritemplate==3.0.0',
        'urllib3==1.24.1',
        'xlrd==1.2.0',
        'xlwt==1.3.0',
        'GeoIP==1.3.2',
        'ipaddress==1.0.22',
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'drf-run = python manage.py runserver 8888'
            'celery-worker = celery -A tasks worker -E --loglevel=INFO -c 10'
        ],
    },
)
