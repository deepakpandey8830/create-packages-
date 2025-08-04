from setuptools import setup, find_namespace_packages

setup(
    name='django-tasks',
    version='0.1',
    packages=find_namespace_packages(include=['tasks', 'tasks.*']),
    include_package_data=True,
    package_data={
        'tasks': ['templates/tasks/*.html'],
    },
    license='MIT',
    description='A reusable Django tasks app',
    long_description=open('README.md').read(),
    author='Your Name',
    author_email='your@email.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.2',
    ],
    python_requires='>=3.8',
)