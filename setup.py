import ast
import os.path

from setuptools import find_packages, setup


def readme():
    try:
        with open('README.rst') as f:
            readme = f.read()
    except IOError:
        pass
    try:
        with open('CHANGES.rst') as f:
            readme += '\n\n' + f.read()
    except IOError:
        pass
    return readme


def get_version():
    module_path = os.path.join(
        os.path.dirname(__file__),
        'sqlalchemy_utc',
        'version.py')
    module_file = open(module_path)
    try:
        module_code = module_file.read()
    finally:
        module_file.close()
    tree = ast.parse(module_code, module_path)
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target, = node.targets
        if isinstance(target, ast.Name) and target.id == '__version__':
            return node.value.s


install_requires = ['setuptools', 'SQLAlchemy >= 0.9.0']


setup(
    name='SQLAlchemy-Utc',
    description='SQLAlchemy type to store aware datetime values',
    long_description=readme(),
    version=get_version(),
    url='https://github.com/spoqa/sqlalchemy-utc',
    packages=find_packages(exclude=('tests*',)),
    package_data={'sqlalchemy_utc': ['py.typed']},
    author='Hong Minhee',
    author_email='hongminhee' '@' 'member.fsf.org',
    license='MIT License',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Programming Language :: SQL',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development',
    ]
)
