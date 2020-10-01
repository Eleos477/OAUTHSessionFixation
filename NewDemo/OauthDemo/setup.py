import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="OauthDemo",
    version="1.0.0",
    maintainer="Steve from IT",
    description="OAuth session fixation vulnerability demonstration.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)