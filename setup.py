from setuptools import setup, find_packages


setup(
    name='cchloader',
    version='0.2',
    packages=find_packages(),
    url='https://github.com/Som-Energia/cchloader',
    license='GPLv3',
    author='',
    author_email='',
    description='''Implementation based on sippers from GISCE 
    https://github.com/gisce/sippers''',
    entry_points='''
        [console_scripts]
        usmartdata=usmartdata.cli:usmartdata
    ''',
    package_data={
        'cchloader': ['data/*']
    },
    install_requires=[
        "raven",
        "pymongo<3.0",
        "osconf",
        "marshmallow==2.0.0b2",
        "click"
    ],
    test_suite='',
)
