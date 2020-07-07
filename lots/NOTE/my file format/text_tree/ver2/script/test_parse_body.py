

from unittest import TestCase
import unittest
from .parse_body import (
    parse_text2simple_body
    , ParseError
    , EscapeError
    , ContinuationError
    , IndentError
    , BodyError
    , BlockDedentError
    , AnchorError
    , LastAnchorError
    , FirstAnchorError
    )
# tree = (-1, comment, None) | (1, content, None) | (3, content, [tree])
# body = [tree]

input_output_pairs = \
    [ ('', [])
    , ('  ', [])
    , ('  \n  ', [])
    ]
white_line_data = input_output_pairs


input_output_pairs = \
    [ ('''
    ! free indent
        ! xxx
      ! xxx
  ! xxx
    ''', [])
    ]
free_comment_data = input_output_pairs
input_output_pairs = \
    [ ('" \n ! ', [(3, '', [])])
    , ('\' \n ! ', [(1, '', None)])
    , ('# \n ! ', [(-1, '', None)])
    , ('\' \n; ! ', [(1, '\n! ', None)])
    , ('\' \n\\ ! ', [(1, '! ', None)])
    , ('\' \n\\ \n; x\n\\ ! ', [(1, '\nx! ', None)])
    ]
simple_content_node_data = input_output_pairs


p = parse_text2simple_body
class TestTextTreeBodyParser(TestCase):
    def _test_with_pairs(self, pairs):
        for input, output in pairs:
            with self.subTest(text=input, tree_body=output):
                self.assertEqual(p(input), output)
    def test_while_line(self):
        self._test_with_pairs(white_line_data)
    def test_free_comment(self):
        self._test_with_pairs(free_comment_data)
    def test_simple_content_node(self):
        self._test_with_pairs(simple_content_node_data)
    def test_indent(self):
        txt1 = '''
            " a
                ' b
            '''
        out1 = [(3, 'a', [(1, 'b', None)])]
        self.assertEqual(p(txt1), out1)

        txt2 = '''
            " a
                ' b
                " c
                    " d
                        " e
            " f
            '''
        out2 = [(3, 'a', [(1, 'b', None), (3, 'c', [(3, 'd', [(3, 'e', [])])])]), (3, 'f', [])]
        self.assertEqual(p(txt2), out2)


        txt_err = '''
            " a
                ' b
              ' c
            '''
        self.assertRaises(IndentError, lambda:p(txt_err))

        txt_err = '''
            ' a
                ' b
            '''
        self.assertRaises(BodyError, lambda:p(txt_err))

        txt_err = '''
            " a
                \\ b
            '''
        self.assertRaises(ContinuationError, lambda:p(txt_err))

        txt_err = '''
            " a
                ; b
            '''
        self.assertRaises(ContinuationError, lambda:p(txt_err))

    def test_fence_dotdot(self):
        txt_err = '''
            ' a
            ..
            \\ b
            '''
        self.assertRaises(ContinuationError, lambda:p(txt_err))

        txt_err = '''
            ' a
            ..
            ; b
            '''
        self.assertRaises(ContinuationError, lambda:p(txt_err))

        txt_err = '''
            " a
            ..
                ' b
            '''
        self.assertRaises(BodyError, lambda:p(txt_err))

        txt1 = '''
            " a
                .
            " a
                ..
            ..
            ' b
            '''
        out1 = [(3, 'a', []), (3, 'a', []), (1, 'b', None)]
        self.assertEqual(p(txt1), out1)

    def test_fence_dot(self):
        txt_err = '''
            ' a
            .
            \\ b
            '''
        self.assertRaises(ContinuationError, lambda:p(txt_err))

        txt1 = '''
            ' a
            \\ b
            .
            ' c
            '''
        out1 = [(1, 'ab', None), (1, 'c', None)]
        self.assertEqual(p(txt1), out1)

        txt2 = '''
            ' a
            .
            ; b
            '''
        out2 = [(1, 'a\nb', None)]
        self.assertEqual(p(txt2), out2)

        txt3 = '''
            " a
            .
                ' b
            '''
        out3 = [(3, 'a', [(1, 'b', None)])]
        self.assertEqual(p(txt3), out3)

    def test_multi_line_node(self):
        txt = '''
            ' abc
            \\---- defg
            \\ h
            ; ij
            \\- k
            \\-- l
            ; m
            ; n
            ; o
            \\ 
            ; 
            ' pq
            ; 
            ; 
        '''
        content1 = 'abcdefgh\nijkl\nm\nn\no\n'
        content2 = 'pq\n\n'
        output = [(1,content1,None), (1,content2,None)]
        self.assertEqual(p(txt), output)

    def test_block_indent(self):
        txt1 = '''
            " a
                <>>>>>>>> tag x
                        ' b
                ><<<<<<<< tag x
                ' c
            ' d
            '''
        out1 = [(3,'a',[(1,'b',None), (1,'c',None)]), (1,'d',None)]
        self.assertEqual(p(txt1), out1)

        txt_err = '''
            " a
                <>>>>>>>>> tag x
                    ' b
                ><<<<<<<<< tag x
                ' c
            ' d
            '''
        self.assertRaises(BlockDedentError, lambda: p(txt_err))

        txt_err = '''
            " a
                <>>>>>>>>> tag x
                            ' b
                ><<<<<<<<< tag x
                ' c
            ' d
            '''
        self.assertRaises(BodyError, lambda: p(txt_err))



    def test_block_dedent(self):
        txt1 = '''
            " a
        <<<<<<<<< tag x
        ' b
        >>>>>>>>> tag x
                ' c
            ' d
            '''
        out1 = [(3,'a',[(1,'b',None), (1,'c',None)]), (1,'d',None)]
        self.assertEqual(p(txt1), out1)

        # close before open
        txt_err = '''
            " a
        >>>>>>>>> tag x
        ' b
        <<<<<<<<< tag x
                ' c
            ' d
            '''
        self.assertRaises(BlockDedentError, lambda:p(txt_err))

        txt_err = '''
            " a
        <<<<<<<<< tag x
    <<<<<<<<< tag x
    ' b
    >>>>>>>>> tag x
        >>>>>>>>> tag x
                ' c
            ' d
            '''
        self.assertRaises(BodyError, lambda:p(txt_err))

        txt2 = '''
            " a
        <<<<<<<<< tag x
    <<<<< tag x
    ' b
    >>>>> tag x
        >>>>>>>>> tag x
                ' c
            ' d
            '''
        out2 = out1
        self.assertEqual(p(txt2), out2)

        txt_err = '''
            " a
        <<<<<<<<< tag x
            ' b
        >>>>>>>>> tag x
                ' c
            ' d
            '''
        self.assertRaises(BodyError, lambda: p(txt_err))

        # y != x
        txt_err = '''
            " a
        <<<<<<<<< tag y
        ' b
        >>>>>>>>> tag x
                ' c
            ' d
            '''
        self.assertRaises(BlockDedentError, lambda: p(txt_err))

        # dedent too much
        txt_err = '''
            " a
        <<<<<<<<< tag x
    " b
        >>>>>>>>> tag x
            '''
        self.assertRaises(BlockDedentError, lambda: p(txt_err))
    def test_nonleaf_comment(self):
        txt = '''
            - nonleaf_comment
            ; next
                " a
                    ' b
                # c
            ' d
            '''
        out = [(-2, 'nonleaf_comment\nnext',
                    [(3, 'a', [(1,'b',None)])
                    ,(-1, 'c', None)
                    ])
              ,(1,'d', None)]
        self.assertEqual(p(txt), out)


    def test_transparent_scope(self):
        txt = '''
            + transparent_scope
            ; next
                " a
                    ' b
                # c
            ' d
            '''
        out = [(2, 'transparent_scope\nnext',
                    [(3, 'a', [(1,'b',None)])
                    ,(-1, 'c', None)
                    ])
              ,(1,'d', None)]
        self.assertEqual(p(txt), out)

    def test_escape(self):
        txt_err = '!^ \c()'
        self.assertRaises(EscapeError, lambda: p(txt_err))

        txt = r'''!^ \c(\n)
            "^ \U(U+38)\([])\u(37)\ud(54)\ad(53)\a(34)\c(\n)\()
            '''
        out = [(3, '87654\n\\', [])]
        self.assertEqual(p(txt), out)


if __name__ == '__main__':
    unittest.main()


'''
print('\n'.join(dir(TestCase)))

addCleanup
addTypeEqualityFunc
assertAlmostEqual
assertAlmostEquals
assertCountEqual
assertDictContainsSubset
assertDictEqual
assertEqual
assertEquals
assertFalse
assertGreater
assertGreaterEqual
assertIn
assertIs
assertIsInstance
assertIsNone
assertIsNot
assertIsNotNone
assertLess
assertLessEqual
assertListEqual
assertLogs
assertMultiLineEqual
assertNotAlmostEqual
assertNotAlmostEquals
assertNotEqual
assertNotEquals
assertNotIn
assertNotIsInstance
assertNotRegex
assertNotRegexpMatches
assertRaises
assertRaisesRegex
assertRaisesRegexp
assertRegex
assertRegexpMatches
assertSequenceEqual
assertSetEqual
assertTrue
assertTupleEqual
assertWarns
assertWarnsRegex
assert_
countTestCases
debug
defaultTestResult
doCleanups
fail
failIf
failIfAlmostEqual
failIfEqual
failUnless
failUnlessAlmostEqual
failUnlessEqual
failUnlessRaises
failureException
id
longMessage
maxDiff
run
setUp
setUpClass
shortDescription
skipTest
subTest
tearDown
tearDownClass
'''
