from setuptools import setup, find_packages
from pathlib import Path

# Чтение содержимого README файла для использования как long_description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Чтение файла requirements.txt
requirements = []
requirements_file = this_directory / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="TimeSeriesAnalysis",
    version="1.0.0",
    author="UrFu",
    author_email="",
    description="Complete educational course on time series analysis with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/graiustommy/TimeSeriesAnalysis.git",
    project_urls={
        "Documentation": "https://github.com/graiustommy/TimeSeriesAnalysis#readme",
        "Source Code": "https://github.com/graiustommy/TimeSeriesAnalysis",
        "Issue Tracker": "https://github.com/graiustommy/TimeSeriesAnalysis/issues",
    },
    license="CC BY 4.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Russian",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "time series",
        "forecasting",
        "analysis",
        "machine learning",
        "deep learning",
        "jupyter",
        "education",
        "tutorial",
        "course",
        "ARIMA",
        "SARIMA",
        "LSTM",
        "exponential smoothing",
        "stationarity",
    ],
    include_package_data=True,
    zip_safe=False,
)
