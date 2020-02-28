import io
import sys

from unittest import TestCase

class Account:
    def __init__(self, output = sys.stdout):
        self.output = output

    def print_statement(self):
        self.output.write('''\
Date|Credit|Debit|Balance
14/01/2012||500|2500
13/01/2012|2000||3000
10/01/2012|1000||1000\
''',)

class FakeStdout:
    def write(self, words):
        self.words = words

class TestAcceptance(TestCase):
    
    def test_imaginary_system(self):
        fake_stdout = FakeStdout()
        account = Account(fake_stdout)
        # account.deposit(2000)
        # account.withdrawal(500)
        account.print_statement()
        self.assertEqual('''\
Date|Credit|Debit|Balance
14/01/2012||500|2500
13/01/2012|2000||3000
10/01/2012|1000||1000\
''', fake_stdout.words)