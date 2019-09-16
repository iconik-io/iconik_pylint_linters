import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class MultipleNamesOnImportFromChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'multiple-names-on-import-from'
    priority = -1
    msgs = {
        'W0001': (
            'Contains multiple names on one import statement',
            'multiple-names-on-import-from',
            'All names imported should be as separate statements.'
        ),
    }
    options = (
        (
            'ignore-ints',
            {
                'default': False, 'type': 'yn', 'metavar': '<y_or_n>',
                'help': 'Allow having multiple names on one import from statement',
            }
        ),
    )

    def visit_importfrom(self, node):
        if len(node.names) > 1:
            self.add_message("multiple-names-on-import-from", node=node)


def register(linter):
    linter.register_checker(MultipleNamesOnImportFromChecker(linter))
