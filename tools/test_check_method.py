import unittest
from check_method import (parse_lines, Finding, check_money, check_timezone,
                          check_denylist, check_proper_nouns, check_agent_tooling)


class Ctx:
    allowlist: set = set()
    denylist: set = set()
    contract_paths: list = []
    root = None
    path: str = "<test>"


class TestParseLines(unittest.TestCase):
    def test_marks_fenced_blocks(self):
        lines = parse_lines("before\n```\ninside\n```\nafter\n")
        self.assertEqual([l.in_fence for l in lines], [False, True, True, True, False])

    def test_marks_language_sections(self):
        text = "en\n<!-- lang:pt-BR -->\nnao\n<!-- /lang -->\nen again\n"
        lines = parse_lines(text)
        self.assertEqual([l.in_lang for l in lines], [False, True, True, True, False])

    def test_marks_headings(self):
        lines = parse_lines("# Title\ntext\n## Sub\n")
        self.assertEqual([l.is_heading for l in lines], [True, False, True])

    def test_strips_code_spans(self):
        lines = parse_lines("see `tools/tracker.py` now\n")
        # Three spaces: the one before the span, the substitution, the one after.
        # Substituting with "" instead would glue `a`x`b` into `ab` and destroy
        # the word boundaries the proper-noun and language checks rely on.
        self.assertEqual(lines[0].prose, "see   now")

    def test_keeps_line_numbers_one_based(self):
        lines = parse_lines("a\nb\n")
        self.assertEqual([l.no for l in lines], [1, 2])


class TestMoney(unittest.TestCase):
    def test_flags_currency_symbol(self):
        found = check_money(parse_lines("the floor is US$120k\n"), Ctx())
        self.assertEqual(len(found), 1)

    def test_flags_bare_thousands(self):
        self.assertEqual(len(check_money(parse_lines("asking 160k\n"), Ctx())), 1)

    def test_flags_iso_code(self):
        self.assertEqual(len(check_money(parse_lines("BRL 20000 monthly\n"), Ctx())), 1)

    def test_allows_plain_numbers(self):
        self.assertEqual(check_money(parse_lines("keep it to 2 pages\n"), Ctx()), [])

    def test_allows_ordinary_english_with_numbers(self):
        # Every one of these matched while the pattern carried a blanket IGNORECASE.
        for ok in ["wait for 24 hours", "after 3 weeks", "under 5 minutes",
                   "over 100 applications", "LAYER 3 is state"]:
            with self.subTest(ok=ok):
                self.assertEqual(check_money(parse_lines(ok + "\n"), Ctx()), [])

    def test_allows_inside_language_section(self):
        text = "<!-- lang:pt-BR -->\nUS$120k\n<!-- /lang -->\n"
        self.assertEqual(check_money(parse_lines(text), Ctx()), [])


class TestTimezone(unittest.TestCase):
    def test_flags_utc_offset(self):
        self.assertEqual(len(check_timezone(parse_lines("works UTC-3\n"), Ctx())), 1)

    def test_flags_iana_zone(self):
        self.assertEqual(len(check_timezone(parse_lines("America/Sao_Paulo\n"), Ctx())), 1)

    def test_flags_abbreviation(self):
        self.assertEqual(len(check_timezone(parse_lines("overlap with PST\n"), Ctx())), 1)

    def test_does_not_flag_country_names(self):
        # Country and city names belong to the proper-noun check, not this one.
        self.assertEqual(check_timezone(parse_lines("hiring in Brazil\n"), Ctx()), [])


class TestDenylist(unittest.TestCase):
    def setUp(self):
        self.ctx = Ctx()
        self.ctx.denylist = {"Ronaldo", "Eduzz", "Laravel"}

    def test_flags_at_sentence_start(self):
        found = check_denylist(parse_lines("Eduzz is the employer.\n"), self.ctx)
        self.assertEqual(len(found), 1)

    def test_flags_mid_sentence(self):
        found = check_denylist(parse_lines("built at Eduzz for years\n"), self.ctx)
        self.assertEqual(len(found), 1)

    def test_flags_inside_code_fence(self):
        text = "```\nsite:lever.co Laravel\n```\n"
        self.assertEqual(len(check_denylist(parse_lines(text), self.ctx)), 1)

    def test_flags_inside_code_span(self):
        found = check_denylist(parse_lines("see `Eduzz` here\n"), self.ctx)
        self.assertEqual(len(found), 1)

    def test_is_case_sensitive_on_word_boundary(self):
        self.assertEqual(check_denylist(parse_lines("orbital mechanics\n"), self.ctx), [])


class TestProperNouns(unittest.TestCase):
    def setUp(self):
        self.ctx = Ctx()
        self.ctx.allowlist = {"Greenhouse", "Lever", "LinkedIn"}

    def test_flags_mid_sentence_capital(self):
        found = check_proper_nouns(parse_lines("they use Workday for this\n"), self.ctx)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].excerpt, "Workday")

    def test_allows_sentence_initial(self):
        # Accepted miss: the denylist covers the names that matter at any position.
        self.assertEqual(check_proper_nouns(parse_lines("Workday is common.\n"), self.ctx), [])

    def test_allows_allowlisted(self):
        self.assertEqual(check_proper_nouns(parse_lines("post on Greenhouse today\n"), self.ctx), [])

    def test_allows_short_acronyms(self):
        self.assertEqual(check_proper_nouns(parse_lines("run the ATS and STAR checks\n"), self.ctx), [])

    def test_allows_hyphenated_short_acronyms(self):
        for ok in ["the rule ZERO-A is mandatory", "same as ZERO-B here"]:
            with self.subTest(ok=ok):
                self.assertEqual(check_proper_nouns(parse_lines(ok + "\n"), self.ctx), [])

    def test_flags_long_all_caps(self):
        self.assertEqual(len(check_proper_nouns(parse_lines("the SALESFORCE export\n"), self.ctx)), 1)

    def test_allows_headings(self):
        self.assertEqual(check_proper_nouns(parse_lines("## The Measured Number Test\n"), self.ctx), [])

    def test_allows_code_spans_and_fences(self):
        self.assertEqual(check_proper_nouns(parse_lines("read `profile/PROFILE.md` now\n"), self.ctx), [])
        self.assertEqual(check_proper_nouns(parse_lines("```\nAshby\n```\n"), self.ctx), [])

    def test_allows_after_terminal_punctuation(self):
        found = check_proper_nouns(parse_lines("Do it. Workday is fine.\n"), self.ctx)
        self.assertEqual(found, [])

    def test_allows_i(self):
        self.assertEqual(check_proper_nouns(parse_lines("what I own here\n"), self.ctx), [])


class TestAgentTooling(unittest.TestCase):
    def test_flags_tool_names(self):
        for bad in ["use the Task tool", "call TodoWrite", "the Bash tool",
                    "a slash command", "see .claude/skills", "read CLAUDE.md"]:
            with self.subTest(bad=bad):
                self.assertEqual(len(check_agent_tooling(parse_lines(bad + "\n"), Ctx())), 1)

    def test_allows_neutral_vocabulary(self):
        for ok in ["dispatch a subagent with clean context",
                   "read the file at tools/tracker.py",
                   "ask the person to paste it"]:
            with self.subTest(ok=ok):
                self.assertEqual(check_agent_tooling(parse_lines(ok + "\n"), Ctx()), [])

    def test_flags_inside_code_fence(self):
        text = "```\nTask tool: review\n```\n"
        self.assertEqual(len(check_agent_tooling(parse_lines(text), Ctx())), 1)


if __name__ == "__main__":
    unittest.main()
