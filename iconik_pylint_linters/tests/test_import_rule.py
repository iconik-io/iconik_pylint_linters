import astroid
import pylint.testutils
from iconik_pylint_linters.linters.import_rule import MultipleNamesOnImportFromChecker

class TestMultipleNamesOnImportFromChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = MultipleNamesOnImportFromChecker
    def setUp(self):
        self.setup_method()

    def test_does_not_find_import_with_multiple_names(self):
        node = astroid.extract_node("""from uuid import uuid3""")

        with self.assertNoMessages():
            self.checker.visit_importfrom(node)

        node = astroid.extract_node("""from uuid import uuid5""")

        with self.assertNoMessages():
            self.checker.visit_importfrom(node)

        node = astroid.extract_node("""from uuid import UUID""")

        with self.assertNoMessages():
            self.checker.visit_importfrom(node)

    def test_finds_import_with_multiple_names(self):
        node = astroid.extract_node("""from uuid import uuid3, uuid5, UUID""")

        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='multiple-names-on-import-from',
                node=node,
            ),
        ):
            self.checker.visit_importfrom(node)

        node = astroid.extract_node("""
        from uuid import (
            uuid3,
            uuid5,
            UUID
        )
        """)

        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id='multiple-names-on-import-from',
                node=node,
            ),
        ):
            self.checker.visit_importfrom(node)
