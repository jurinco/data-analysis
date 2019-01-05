from setuptools import setup, find_packages

setup(
        name='data_analysis',
        version='0.0.1',
        url='www.github.com/jurinco/data-analysis',
        license='BSD',
        author='Fer',
        packages=find_packages(),
        install_requires=['PyQt5', 'pandas', 'sqlalchemy', 'nltk', 'numpy',
            'jupyter', 'python-twitter', 'PyQtChart', 'lda', 'matplotlib',
            'scipy'],
        entry_points={},
        extras_require={'dev': ['flake8',]},
        )
