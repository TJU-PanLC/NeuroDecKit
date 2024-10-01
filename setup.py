from setuptools import setup, find_packages

with open("README.md", "r", errors="ignore", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='neurodeckit',
    version='0.1.0',  
    author='LC.Pan',
    author_email='panlincong@tju.edu.cn',
    description='Full chain toolkit for EEG signal decoding',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TJU-PanLC/NeuroDecKit',
    packages=find_packages(),  
    install_requires=[
        'braindecode',
        'catboost',
        'einops',
        'geoopt',
        'h5py',
        'joblib',
        'lightgbm',
        'mne==1.4.2',
        'numpy',
        'pandas',
        'pooch',
        'psutil',
        'pynvml',
        'pyriemann==0.6',
        'scikit_learn',
        'scipy==1.13.1',
        'skorch',
        'statsmodels',
        'torch',
        'torchsummary',
        'xgboost',
    ],  
    keywords=['python', 'package'],
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
)