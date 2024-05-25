from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged("post_install", "-at_install")
class ModTest(TransactionCase):
    def setUp(self):
        super(ModTest, self).setUp()

    def test_01(self):
        print("test_01")
        self.assertTrue(False, "This test should fail")

    def test_02(self):
        print("test_02")
        self.assertTrue(True, "This test should pass")
