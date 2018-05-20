from setuptools import setup
setup(
    name = 'python-service',
    packages = ['pyservice'],
    version = "0.0.3",
    description = 'Placeholder description',
    author = "Jason Trigg",
    author_email = "jasontrigg0@gmail.com",
    url = "https://github.com/jasontrigg0/python-service",
    download_url = 'https://github.com/jasontrigg0/python-service/tarball/0.0.3',
    scripts=[],
    install_requires=[
        "python-daemon",
        "setproctitle"
    ],
    keywords = [],
    classifiers = [],
)
