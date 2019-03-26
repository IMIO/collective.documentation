# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implements


class IDocumentationSection(model.Schema):
    """IDocumentationSection"""


class DocumentationSection(Container):
    implements(IDocumentationSection)
