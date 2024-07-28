from setuptools import setup, find_packages

setup(
    name='financial_data',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'gspread',
        'numpy',
        'oauth2client',
        'pandas',
        'yfinance'
    ],
    description='A library for processing financial data and interacting with Google Sheets.',
    author='Alyx C',
    author_email='xalyx007@gmail.com',
    url='https://github.com/xalyx007/financial_data',
)
