"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "kitconcept_blog"

_ = MessageFactory("kitconcept_blog")

logger = logging.getLogger("kitconcept_blog")
