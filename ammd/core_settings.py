""" Django settings for core applications.
"""
import os

SERVER_URI = os.environ["SERVER_URI"] if "SERVER_URI" in os.environ else None

# ===============================================
# Website configuration
# ===============================================
WEBSITE_SHORT_TITLE = "AMMD"
WEBSITE_ADMIN_COLOR = "black-light"
# Choose from:  black, black-light, blue, blue-light, green, green-light, purple, purple-light, red, red-light, yellow,
#               yellow-light

# Customization Label
CUSTOM_CURATE = "Add your resource"
CUSTOM_DATA = "Materials Data"
CUSTOM_NAME = "AMMD"
# MENUS NAMES
EXPLORE_TREE_MENU_NAME = "Browse Database"
EXPLORE_MENU_NAME = "Search Data"
CURATE_MENU_NAME = "Curate Data"
SCHEMA_VIEWER_MENU_NAME = "View Schema"
EXPLORE_EXAMPLE_MENU_NAME = "Data Query"
ADVANCED_MENU_NAME = "Advanced Functions"
VISUALIZATION_USER_MENU_NAME = "Data Visualization"
VISUALIZATION_INSITU_USER_MENU_NAME = "Insitu Data Visualization"
DISPLAY_NIST_HEADERS = True
#DATA_SOURCES_EXPLORE_APPS

# DASHBOARD
DATA_DISPLAY_NAME = "record"
DRAFT_DISPLAY_NAME = "draft"
WORKSPACE_DISPLAY_NAME = "workspace"

# FIXME: set desired value before release
# Lists in data not stored if number of elements is over the limit (e.g. 100)
SEARCHABLE_DATA_OCCURRENCES_LIMIT = None

PARSER_DOWNLOAD_DEPENDENCIES = True
""" boolean: Does the parser download dependencies
"""

EXPLORE_ADD_DEFAULT_LOCAL_DATA_SOURCE_TO_QUERY = True
""" boolean: Do we add the local data source to new queries by default
"""

SSL_CERTIFICATES_DIR = True
""" Either a boolean, in which case it controls whether requests verify the server's TLS certificate, 
or a string, in which case it must be a path to a CA bundle to use.
"""

XSD_URI_RESOLVER = None
""" :py:class:`str`: XSD URI Resolver for lxml validation. Choose from:  None, 'REQUESTS_RESOLVER'.
"""

DISPLAY_EDIT_BUTTON = True
""" boolean: Display the edit button on the result page
"""

DATA_SORTING_FIELDS = ["-last_modification_date"]
""" Array<string>: Default sort fields for the data query. 
"""

DATA_DISPLAYED_SORTING_FIELDS = [
    {
        "field": "last_modification_date",
        "display": "Last updated",
        "ordering": "-last_modification_date",
    },
    {
        "field": "last_modification_date",
        "display": "First updated",
        "ordering": "+last_modification_date",
    },
    {"field": "title", "display": "Titles (A-Z)", "ordering": "+title"},
    {"field": "title", "display": "Titles (Z-A)", "ordering": "-title"},
    {"field": "template", "display": "Templates", "ordering": "+template"},
]
"""The default sorting fields displayed on the GUI, Data model field Array"""

SORTING_DISPLAY_TYPE = "single"
"""Result sorting graphical display type ('multi' / 'single')"""
DEFAULT_DATE_TOGGLE_VALUE = True
""" boolean: Set the toggle default value in the records list
"""
DISPLAY_PRIVACY_POLICY_FOOTER = False
""" boolean: display the privacy policy link in the footer
"""
DISPLAY_TERMS_OF_USE_FOOTER = True
""" boolean: display the terms of use link in the footer
"""
DISPLAY_CONTACT_FOOTER = False
""" boolean: display the contact link in the footer
"""
DISPLAY_HELP_FOOTER = False
""" boolean: display the help link in the footer
"""
DISPLAY_RULES_OF_BEHAVIOR_FOOTER = False
""" boolean: display the rules of behavior link in the footer
"""
ID_PROVIDER_SYSTEM_NAME = "local"
""" str: internal name of the provider system.
"""

ID_PROVIDER_SYSTEM_CONFIG = {
    "class": "core_linked_records_app.utils.providers.local.LocalIdProvider",
    "args": [],
}
""" dict: provider system configuration for resolving PIDs.
"""

ID_PROVIDER_PREFIXES = (
    os.environ["ID_PROVIDER_PREFIXES"].split(",")
    if "ID_PROVIDER_PREFIXES" in os.environ
    else ["cdcs"]
)
""" list<str>: accepted providers if manually specifying PIDs (first item is the
default prefix)
"""
ID_PROVIDER_PREFIX_DEFAULT = os.getenv(
    "ID_PROVIDER_PREFIX_DEFAULT", ID_PROVIDER_PREFIXES[0]
)

ID_PROVIDER_PREFIX_BLOB = os.getenv(
    "ID_PROVIDER_PREFIX_BLOB", ID_PROVIDER_PREFIXES[0]
)

PID_XPATH = os.getenv("PID_XPATH", "root.pid")
""" string: location of the PID in the document, specified as dot notation
"""

AUTO_SET_PID = os.getenv("AUTO_SET_PID", "False").lower() == "true"
""" boolean: enable the automatic pid generation for saved data.
"""

ENABLE_SAML2_SSO_AUTH = os.getenv("ENABLE_SAML2_SSO_AUTH", "False").lower() == "true"
""" boolean: enable SAML2 SSO authentication.
"""

ENABLE_HANDLE_PID = os.getenv("ENABLE_HANDLE_PID", "False").lower() == "true"
""" boolean: enable handle server PID support.
"""

CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT = True
""" boolean: Can anonymous user access public data
"""

CQL_NAMESPACE = "http://siam.nist.gov/Database-Navigation-Ontology#"
