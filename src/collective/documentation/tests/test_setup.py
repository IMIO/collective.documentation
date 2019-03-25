# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.documentation.testing import (
    COLLECTIVE_DOCUMENTATION_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


no_get_installer = False


try:
    from Products.CMFPlone.utils import get_installer
except Exception:
    no_get_installer = True


class TestSetup(unittest.TestCase):
    """Test that collective.documentation is properly installed."""

    layer = COLLECTIVE_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.documentation is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.documentation"))

    def test_browserlayer(self):
        """Test that ICollectiveDocumentationLayer is registered."""
        from collective.documentation.interfaces import ICollectiveDocumentationLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveDocumentationLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_DOCUMENTATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.documentation")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.documentation is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.documentation")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveDocumentationLayer is removed."""
        from collective.documentation.interfaces import ICollectiveDocumentationLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveDocumentationLayer, utils.registered_layers())
