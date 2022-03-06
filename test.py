import unittest

from unittest.mock import Mock
from app import FrequentWordParser


class FrequentWordTester(unittest.TestCase):

    def setUp(self):
        self.parser = FrequentWordParser()

    def test_process_file_line_by_line(self):
        # use a file in the current DIR
        files = ["moby_dick.txt"]

        self.parser.print_frequency_map = Mock()
        self.parser.clean_data = Mock()
        self.parser.fill_frequency_map = Mock()
        self.parser.word_count = Mock(return_value=100)
        self.parser.process_line_by_line_file(files)

        self.assertTrue(self.parser.clean_data.called)
        self.assertTrue(self.parser.fill_frequency_map.called)
        self.assertTrue(self.parser.print_frequency_map.called)

    def test_process_std_in(self):

        self.parser.process_line_by_line_std_in = Mock()
        self.parser.word_count = Mock(return_value=100)
        self.parser.frequency_map = {}
        res = self.parser.process_std_in([])

        self.assertTrue(self.parser.process_line_by_line_std_in.called)

    def test_open_file(self):
        files = []

        self.parser.process_line_by_line_file = Mock()
        self.parser.open_file(files)
        self.assertTrue(self.parser.process_line_by_line_file.called)

    def test_cleaned_data(self):
        test_cases = [
            ("This is a basic string", ['this', 'is', 'a', 'basic', 'string']),
            ("what's that is isn't what you'd think it might've been", [
             'whats',  'that',   'is',   'isnt',   'what',   'youd',   'think',   'it',  'mightve',  'been']),
            ("WhY dId wE evER gO THIS way!!", [
             'why', 'did', 'we', 'ever', 'go', 'this', 'way']),
            ("I love sandwiches", ['i', 'love', 'sandwiches']),
            ("I love\nsandwiches", ['i', 'love', 'sandwiches']),
            ("I LOVE SANDWICHES", ['i', 'love', 'sandwiches']),
            ("Hello there. General kenobi", [
             'hello', 'there', 'general', 'kenobi']),
            ("I AM BATMAN", ['i', 'am', 'batman']),
            ("", []),
            ("The pale Usher--threadbare in coat, heart, body, and brain;",
             ['the',  'pale',  'usherthreadbare',  'in',  'coat',  'heart',  'body',  'and',  'brain']),
            ("WHALE.... Sw. and Dan. HVAL. This animal is named from roundness or \
rolling; for in Dan. HVALT is arched or vaulted", ['whale',  'sw',  'and',  'dan',  'hval',  'this',  'animal',  'is',  'named',  'from',  'roundness',  'or',  'rolling',  'for',  'in',  'dan',  'hvalt',  'is',  'arched',  'or',  'vaulted']),
            ("Among the \
former, one was of a most monstrous size.... This came towards us, \
open-mouthed, raising the waves on all sides, and beating the sea before \
him into a foam.", ['among',  'the',  'former',  'one',  'was',  'of',  'a',  'most',  'monstrous',  'size',  'this',  'came',  'towards',  'us',  'openmouthed',  'raising',  'the',  'waves',  'on',  'all',  'sides',  'and',  'beating',  'the',  'sea',  'before',  'him',  'into',  'a',  'foam']),
            ("October 13.  \"There she blows,\" was sung out from the mast-head.\
            \"Where away?\" demanded the captain. \
            \"Three points off the lee bow, sir.\" \
            \"Raise up your wheel.  Steady!\"  \"Steady, sir.\" \
            \"Mast-head ahoy!  Do you see that whale now?\" \
            \"Ay ay, sir!  A shoal of Sperm Whales!  There she blows!  There she \
            breaches!\" \
            \"Sing out! sing out every time!\" \
            \"Ay Ay, sir!  There she blows! there--there--THAR she \
            blows--bowes--bo-o-os!\" \
            \"How far off?\" \
            \"Two miles and a half.\" \
            \"Thunder and lightning! so near!  Call all hands.\" \
            --J. ROSS BROWNE'S ETCHINGS OF A WHALING CRUIZE.  1846.",
             ['october', '13', 'there', 'she', 'blows', 'was', 'sung', 'out', 'from', 'the', 'masthead', 'where', 'away', 'demanded', 'the', 'captain', 'three', 'points', 'off', 'the', 'lee', 'bow', 'sir', 'raise', 'up', 'your', 'wheel', 'steady', 'steady', 'sir', 'masthead', 'ahoy', 'do', 'you', 'see', 'that', 'whale', 'now', 'ay', 'ay', 'sir', 'a', 'shoal', 'of', 'sperm', 'whales', 'there',
                 'she', 'blows', 'there', 'she', 'breaches', 'sing', 'out', 'sing', 'out', 'every', 'time', 'ay', 'ay', 'sir', 'there', 'she', 'blows', 'theretherethar', 'she', 'blowsbowesbooos', 'how', 'far', 'off', 'two', 'miles', 'and', 'a', 'half', 'thunder', 'and', 'lightning', 'so', 'near', 'call', 'all', 'hands', 'j', 'ross', 'brownes', 'etchings', 'of', 'a', 'whaling', 'cruize', '1846']
             ),
            ("reveries--stand that man on his legs, set his feet a-going, and he will",
             ['reveriesstand', 'that', 'man', 'on', 'his', 'legs', 'set', 'his', 'feet', 'agoing', 'and', 'he', 'will']),
            ("GRAND CONTESTED ELECTION FOR THE PRESIDENCY OF THE UNITED STATES",
             ['grand', 'contested', 'election', 'for', 'the', 'presidency', 'of', 'the', 'united', 'states']),
            ("have been inducements; but as for me, I am tormented with an everlasting", [
             'have', 'been', 'inducements', 'but', 'as', 'for', 'me', 'i', 'am', 'tormented', 'with', 'an', 'everlasting']),
            ("was her great original--the Tyre of this Carthage;--the place where the",
             ['was', 'her', 'great', 'originalthe', 'tyre', 'of', 'this', 'carthagethe', 'place', 'where', 'the']),
        ]

        for test_case in test_cases:
            actual_result = []
            test_data = test_case[0]
            expected_result = test_case[1]

            self.parser.clean_data(test_data, actual_result)

            self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
