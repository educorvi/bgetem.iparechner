# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bgetem.iparechner


class BgetemIparechnerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bgetem.iparechner)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bgetem.iparechner:default')


BGETEM_IPARECHNER_FIXTURE = BgetemIparechnerLayer()


BGETEM_IPARECHNER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BGETEM_IPARECHNER_FIXTURE,),
    name='BgetemIparechnerLayer:IntegrationTesting',
)


BGETEM_IPARECHNER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BGETEM_IPARECHNER_FIXTURE,),
    name='BgetemIparechnerLayer:FunctionalTesting',
)


BGETEM_IPARECHNER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BGETEM_IPARECHNER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BgetemIparechnerLayer:AcceptanceTesting',
)
