""" The Facter module contains the function and classes to create a VIEW on the Registr.

Combines data from core-automation-clients, core-automation-portfolios, core-automation-zones, and core-automation-apps tables
to create a View or Context for Jinja2 templates to render.

"""

from .facter import (
    get_facts,
    get_facts_by_identity,
    get_client_facts,
    get_app_facts,
    get_portfolio_facts,
    get_zone_facts,
    get_zone_facts_by_account_id,
)

__all__ = [
    "get_client_facts",
    "get_portfolio_facts",
    "get_zone_facts",
    "get_zone_facts_by_account_id",
    "get_app_facts",
    "get_facts",
    "get_facts_by_identity",
    "FactsActions",
]
