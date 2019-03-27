# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implements


class IDocumentationCategory(model.Schema):
    """IDocumentationCategory"""


class DocumentationCategory(Container):
    implements(IDocumentationCategory)
