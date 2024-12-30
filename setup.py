# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="volunteer_management_frappe_erpnext_app",
    version="0.0.1",
    author="Sreeraj Thamarappilly",
    author_email="sreeraj.techie@gmail.com",
    description="Advanced Volunteer Management System on Frappe/ERPNext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SreerajThamarappilly/volunteer_management_frappe_erpnext_app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.11",
)
