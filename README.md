# pypi package template

[![GitHub Workflow Status](https://img.shields.io/badge/CI/CD-Automated-success?style=flat-square&logo=github)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI](https://img.shields.io/badge/PyPI-Package-3775A9?style=flat-square&logo=pypi)](https://pypi.org/)

A streamlined template for creating Python packages with an automated CI/CD pipeline.

## Features

-   Automated publishing to PyPI on GitHub releases
-   Version automatically synced from GitHub release tags
-   requirements.txt support for project dependencies
-   Pre-configured setup with pyproject.toml using PEP 517/518
-   Includes build and twine for modern package distribution

## Setup Guide

1. **Create a new repository** from this template

2. **Configure your package**

    - Update `pyproject.toml` with your package metadata (name, author, description)
    - Version is automatically set from GitHub release tags during release publishing
    - Edit `requirements.txt` to include your package dependencies
    - Place your code inside your package folder (e.g., `your_package/`, in this example `summing_lixelv/`)

3. **Set up CI/CD**

    - Generate a PyPI API token: [Get PyPI token](https://pypi.org/manage/account/token/)
    - Add the token as `PYPI_TOKEN` in GitHub Secrets: [Create GitHub secret](https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_GITHUB_REPOSITORY>/settings/secrets/actions)
    - Replace `<YOUR_GITHUB_USERNAME>` and `<YOUR_GITHUB_REPOSITORY>` with your actual GitHub account and repository names

4. **Release your package**
    - Create a GitHub release with a semantic version tag (e.g., `v1.0.0`)
    - The workflow will automatically update the version, build, and publish your package to PyPI

---

<div align="center">
  <code>pip install your-package-name</code>
</div>
