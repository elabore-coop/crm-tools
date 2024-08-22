# Copyright  Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "crm usability misc",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Elabore",
    "license": "AGPL-3",
    "category": "CRM",
    "summary": "Various modifications of CRM app",
    # any module necessary for this one to work correctly
    "depends": [
        "base","crm","sales_team",
    ],
    # always loaded
    "data": [
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}