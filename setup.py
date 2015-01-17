from setuptools import setup
import sqlstr


setup(
    name="sqlstr",
    version=sqlstr.__version__,
    author="Gocho Mugo I",
    author_email="mugo@forfuture.co.ke",
    url="https://github.com/GochoMugo/sql-string-templating",
    download_url="https://github.com/GochoMugo/sql-string-templating/zipball/master",
    description="sql string templating",
    keywords=["sql", "templating"],
    license="MIT",
    long_description=sqlstr.__doc__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7"
    ],
    packages=["sqlstr"]
)
