from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name="time_complexity",
    url="https://github.com/Cy-r0/time_complexity",
    author="Ciro Cursio",
    author_email="none@gmail.com",
    # Needed to actually package something
    packages=["time_complexity"],
    # Needed for dependencies
    install_requires=["matplotlib"],
    # *strongly* suggested for sharing
    version="0.1",
    # The license can be anything you like
    license="Apache 2.0",
    description="Measure time complexity of python functions",
    # We will also need a readme eventually (there will be a warning)
    long_description=open("README.md").read()
)
