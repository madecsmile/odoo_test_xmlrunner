from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged("post_install", "-at_install")
class ModTest(TransactionCase):
    def setUp(self):
        super(ModTest, self).setUp()

    def test_01(self):
        print("test_01")
        self.assertTrue(False, "This test should fail")
