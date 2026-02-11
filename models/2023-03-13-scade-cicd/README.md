# SCADE CI/CD

[![ansys-scade](https://img.shields.io/badge/Ansys-SCADE-ffb71b?labelColor=black&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://github.com/ansys-scade/)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Windows batch scripts to support a CI/CD (Continuous Integration / Continuous Delivery) workflow on a SCADE project.

The `templates` folder provides workflow templates to integrate these scripts into CI/CD workflows on **Gitlab** and **Jenkins**.

> ℹ️ Note: **GitHub** users should directly use the complete set of SCADE GitHub Actions over at [scade-actions](https://github.com/ansys/scade-actions).

## Installation

Copy the contents of the `scripts` folder into a `scade-cicd` folder at the root of your project.

## Usage

### GitHub
GitHub users should use the complete set of SCADE GitHub Actions over at [scade-actions](https://github.com/ansys/scade-actions). Those actions provide a more integrated version of the scripts provided in this example.

### GitLab
Copy file `templates/.gitlab-ci-template.yml` as `.gitlab-ci.yml` at the root of your GitLab project repository.

Edit this file to configure project settings:
  - set the path to the SCADE installation folder on your GitLab runner
  - set the path to the different SCADE projects etp files (without the `.etp` extension)
  - set configurations names for the different SCADE activities

Example of content for the `variables` section:

    variables:
        # SCADE installation folder for runners
        SCADE_DIR: "C:\\Program Files\\ANSYS Inc\\v231\\SCADE"
        # SCADE project relative path without extension
        SCADE_PROJECT_ROOT: "CruiseControl\\CruiseControl"
        # SCADE test project relative path without extension
        SCADE_PROJECT_TEST_ROOT: "CruiseControl_Test\\CruiseControl_Test"
        # SCADE test result project relative path without extension
        SCADE_PROJECT_TEST_RESULT_ROOT: "CruiseControl_Test\\CruiseControl_Test"
        CONF_CHECK: "KCG"
        CONF_REPORT: "RTF"
        CONF_GEN: "KCG"
        CONF_TEST: "Test"

### Jenkins
Copy file `templates/Jenkinsfile` to the root of your project repository.
Edit this file to configure project settings in the `pipeline/environment` section:
  - set the path to the SCADE installation folder on your Jenkins agent
  - set the path to the different SCADE projects etp files (without the `.etp` extension)
  - set configurations names for the different SCADE activities
  - adapt path to artifacts to upload

Make additional changes to adapt this newly-configured workflow to your specific repository needs. For instance, you may want to run the workflow only upon commits to the main branch.
