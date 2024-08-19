"""Sphinx documentation configuration file."""

from datetime import datetime
import os

from ansys_sphinx_theme import (
    __version__,
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    latex,
    watermark,
)
from sphinx.builders.latex import LaTeXBuilder

# Project information
project = "scade-examples"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "examples.scade.docs.pyansys.com")
switcher_version = get_version_match(__version__)

# HTML configuration
html_favicon = ansys_favicon
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "SCADE Examples"
html_static_path = ["_static"]
templates_path = ["_templates"]
html_context = {
    "github_user": "ansys",
    "github_repo": "scade-examples",
    "github_version": "main",
    "doc_path": "doc/source",
}
html_theme_options = {
    "github_url": "https://github.com/ansys/scade-examples",
    "contact_mail": "pyansys.core@ansys.com",
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
    "logo": "ansys",
}

# Sphinx extensions
extensions = [
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
]

suppress_warnings = ["config.cache"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# additional logos for the latex coverpage
LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": latex.generate_preamble(html_title)}
