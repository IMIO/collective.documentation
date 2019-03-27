# -*- coding: utf-8 -*-

from plone.app.contenttypes.content import File
from plone.supermodel import model
from zope.interface import implements
from plone.namedfile.field import NamedBlobFile
from zope import schema
from collective.documentation import _


class IDocumentationFile(model.Schema):
    """IDocumentationFile"""
    source_title = schema.TextLine(
        title=_(u"Source title"),
        required=False,
    )

    source = schema.URI(
        title=_(u"Source"),
        required=False,
    )

    file = NamedBlobFile(
        title=_(u"File"),
        required=True,
    )


class DocumentationFile(File):
    implements(IDocumentationFile)
