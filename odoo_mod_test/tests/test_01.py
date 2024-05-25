from odoo.tests.common import TransactionCase

class ModTest(TransactionCase):
    def setUp(self):
        super(ModTest, self).setUp()

    def test_01(self):
        print("test_01")
        self.assertTrue(True)
