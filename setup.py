from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [x.strip() for x in f.readlines() if x.strip()]

setup(
    name='httpmethods',
    version='1.1.0',
    author='Shutdown',
    description='HTTP verb tampering & methods enumeration',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ShutdownRepo/httpmethods',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    py_modules=['httpmethods'],
    entry_points={
        'console_scripts': [
            'httpmethods=httpmethods:main',
        ],
    },
)
