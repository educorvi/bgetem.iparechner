# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bgetem.iparechner.testing import BGETEM_IPARECHNER_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that bgetem.iparechner is properly installed."""

    layer = BGETEM_IPARECHNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bgetem.iparechner is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'bgetem.iparechner'))

    def test_browserlayer(self):
        """Test that IBgetemIparechnerLayer is registered."""
        from bgetem.iparechner.interfaces import (
            IBgetemIparechnerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IBgetemIparechnerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BGETEM_IPARECHNER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['bgetem.iparechner'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if bgetem.iparechner is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'bgetem.iparechner'))

    def test_browserlayer_removed(self):
        """Test that IBgetemIparechnerLayer is removed."""
        from bgetem.iparechner.interfaces import \
            IBgetemIparechnerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IBgetemIparechnerLayer,
            utils.registered_layers())
