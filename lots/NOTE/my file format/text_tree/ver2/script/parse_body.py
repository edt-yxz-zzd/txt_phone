


__all__ = '''
    parse_text2simple_body
    parse_text2body

    Node
    LeafCommentNode
    LeafDataNode
    NonLeafDataNode
    NonLeafTransparentScopeNode
    NonLeafCommentNode
    tree_to_simple_tree

    ParseError
    EscapeError
    ContinuationError
    IndentError
    BodyError
    BlockDedentError
    AnchorError
    LastAnchorError
    FirstAnchorError



    is_subsequence_of_ex
    is_subsequence_of
    '''.split()



from itertools import chain

class VLine:
    # may be line, logic line, node content, leaf comment
    def __init__(self, line_no_begin, line_no_end
        , indent:int, op, payload, shifted_indent:int=None):
        # for logic line
        self.line_no_begin = line_no_begin
        self.line_no_end = line_no_end

        self.indent = indent
        self.op = op
        self.payload = payload

        self.shifted_indent = shifted_indent
    @property
    def line_no(self):
        return self.line_no_begin
    def get_args(self):
        return (self.line_no_begin, self.line_no_end
                , self.indent, self.op, self.payload, self.shifted_indent)
    def copy(self, **kwargs):
        d = dict(line_no_begin=self.line_no_begin, line_no_end=self.line_no_end
                , indent=self.indent, op=self.op, payload=self.payload
                , shifted_indent=self.shifted_indent)
        d.update(kwargs)
        return type(self)(**d)
    def __repr__(self):
        return '{}{}'.format(type(self).__name__, self.get_args())

class Line(VLine):pass
class LogicLine(VLine):pass
class NodeContent(VLine):
    # node content or leaf comment
    pass

class TmpNode:
    def __init__(self, line, body):
        self.line = line
        self.body = body
class Node:
    def __init__(self, line_no_begin, line_no_end, content):
        self.line_no_begin = line_no_begin
        self.line_no_end = line_no_end
        self.content = content
    def get_node_args(self):
        return self.line_no_begin, self.line_no_end, self.content
    def get_subclass_args(self):
        return self.get_node_args()
    def __repr__(self):
        return '{}{}'.format(type(self).__name__, self.get_subclass_args())
    def __eq__(self, other):
        if not isinstance(other, __class__):return NotImplemented
        return type(self) is type(other) and self.get_subclass_args() == other.get_subclass_args()
    def __ne__(self, other):
        return not (self == other)

class LeafNode(Node):pass
class NonLeafNode(Node):
    def __init__(self, line_no_begin, line_no_end, content, children):
        self.children = tuple(children)
        super().__init__(line_no_begin, line_no_end, content)
    def get_subclass_args(self):
        a,b,c = self.get_node_args()
        return (a,b,c,self.children)

class LeafCommentNode(LeafNode):pass
class LeafDataNode(LeafNode):pass
class NonLeafCommentNode(NonLeafNode):pass
class NonLeafTransparentScopeNode(NonLeafNode):pass
class NonLeafDataNode(NonLeafNode):pass

def tree_to_simple_tree(node:Node, body_type=list):
    # tree = (-1, comment, None) | (1, content, None) | (3, content, [tree])
    #      | (-2, comment, [tree]) | (2, comment, [tree])
    def f(node):
        if isinstance(node, LeafCommentNode):               case = -1
        elif isinstance(node, LeafDataNode):                case = 1
        elif isinstance(node, NonLeafDataNode):             case = 3
        elif isinstance(node, NonLeafCommentNode):          case = -2
        elif isinstance(node, NonLeafTransparentScopeNode): case = 2
        else: raise logic-error

        if isinstance(node, LeafNode):
            children = None
        elif isinstance(node, NonLeafNode):
            children = body_type(map(f, node.children))
        else: raise logic-error

        return (case, node.content, children)
    return f(node)




def get_line_info_for_exception(line):
    return line
class ParseError(Exception):
    def __init__(self, msg, line_no):
        super().__init__(msg, line_no)
        self.line_no = line_no
    def __init__(self, msg, line):
        super().__init__(msg, line)
        self.line = line
class ContinuationError(ParseError):pass
class IndentError(ParseError):pass
class BlockDedentError(ParseError):pass
class BodyError(ParseError):pass
class AnchorError(ParseError):pass
class LastAnchorError(AnchorError):pass
class FirstAnchorError(AnchorError):pass
ParseError
ContinuationError
IndentError
BodyError
BlockDedentError
AnchorError
LastAnchorError
FirstAnchorError

def seperate_indent(line:str):
    indent, tail = _seperate_indent(line)
    assert all(ch == ' ' for ch in indent)
    assert not tail or tail[0] != ' '
    return indent, tail
def _seperate_indent(line:str):
    # indent = ' *' not r'\s*'
    # return (indent, tail) where indent + tail == line
    for i, ch in enumerate(line):
        if ch != ' ':
            return line[:i], line[i:]
    return line, ''

def all_are_the_char(s:str, ch:'char'):
    assert len(ch) == 1
    return all(ch == c for c in s)

def is_block_dedent_open(op):
    # r"<* " or r"<>+ "
    return is_block_dedent_open__d(op) or is_block_dedent_open__i(op)
def is_block_dedent_open__d(op):
    # r"<* "
    return op and op[-1] == ' ' and all_are_the_char(op[:-1], '<')
def is_block_dedent_open__i(op):
    # r"<>+ "
    return (op and op[-1] == ' ' and op[0] == '<'
            and all_are_the_char(op[1:-1], '>'))


def is_block_dedent_close(op):
    # r">* " or r"><+ "
    return is_block_dedent_close__d(op) or is_block_dedent_close__i(op)
def is_block_dedent_close__d(op):
    # r">* "
    return op and op[-1] == ' ' and all_are_the_char(op[:-1], '>')
def is_block_dedent_close__i(op):
    # r"><+ "
    return (op and op[-1] == ' ' and op[0] == '>'
        and all_are_the_char(op[1:-1], '<'))
def is_block_dedent_op(op):
    return is_block_dedent_close(op) or is_block_dedent_open(op)
def matched_block_dedent_open_close(open, close):
    if not is_block_dedent_open(open.op): raise logic-error
    if not is_block_dedent_close(close.op): raise logic-error
    return (open.indent == close.indent and len(open.op) == len(close.op)
        and open.payload == close.payload
        and (is_block_dedent_open__d(open.op)
            and is_block_dedent_close__d(close.op)
            ) or
            (is_block_dedent_open__i(open.op)
            and is_block_dedent_close__i(close.op)
            )
        )

def is_line_continuation_op(op):
    # r'\\-* '
    return (op and op[0] == '\\' and op[-1] == ' '
        and all_are_the_char(op[1:-1], '-')
        )
def seperate_op(non_empty_tail:str):
    # return (op, payload) where op + payload == non_empty_tail
    # e.g. op = '# ' or '>>>>>> tag'
    assert non_empty_tail and non_empty_tail[0] != ' '
    op, maybe_space, payload = non_empty_tail.partition(' ')
    op += maybe_space
    assert op
    assert not payload or op[-1] == ' '

    assert op + payload == non_empty_tail
    return op, payload
def calc_offset(offset, op):
    if not is_block_dedent_op(op):
        return offset

    assert len(op) >= 2
    if is_block_dedent_open__d(op):
        offset += len(op) - 2
    elif is_block_dedent_close__d(op):
        offset -= len(op) - 2
        # offset < 0 ==>> error
    elif is_block_dedent_open__i(op):
        offset -= len(op) - 2
    elif is_block_dedent_close__i(op):
        offset += len(op) - 2
    return offset, indent

def is_subsequence_of_ex(sub, seq, sub_begin, sub_end, seq_begin, seq_end):
    subL = sub_end - sub_begin
    seqL = seq_end - seq_begin
    # assert subL >= 0
    # assert seqL >= 0
    if subL <= 0: return True
    if subL > seqL: return False
    assert 0 < subL <= seqL
    while subL:
        if sub[sub_begin] == seq[seq_begin]:
            # drop sub_begin
            subL -= 1
            sub_begin += 1
            # drop seq_begin
            seqL -= 1
            seq_begin += 1
        else:
            # drop seq_begin
            seqL -= 1
            seq_begin += 1
            if subL > seqL: return False
    return True

def is_subsequence_of(sub, seq):
    return is_subsequence_of_ex(sub, seq, 0, len(sub), 0, len(seq))





class EscapeError(ParseError):pass
class _EscapeError(Exception):pass
def escape(s:str, begin=None, end=None):
    ls_or_pair = escape_prepare__break(s, begin, end)
    T = type(ls_or_pair)
    if T is tuple:
        pair = ls_or_pair
        err_msg, idx = pair
        raise _EscapeError((err_msg, idx))
    elif T is list:
        ls = ls_or_pair
        out = []
        for one_two in ls:
            if len(one_two) == 1:
                [s] = one_two
            else:
                head, body = one_two
                try:
                    s = escape_one(head, body)
                except Exception as e:
                    raise _EscapeError((head, body), e)
            out.append(s)
        return ''.join(out)
    else:
        raise logic-error
    pass



def escape_one(head, body):
    # \\{head}({body})
    # will raise _EscapeError | ... and standard error
    r'''# rex = regex"\\[^()\\]*\([^()]*\)"

unicode "\U(U+hex)"
unicode "\u(hex)"
unicode "\ud(dec)"
ascii "\a(hex)"
ascii "\ad(dec)"
c languish style: "\c(\n)" # i.e. newline "\n"
the escape character "\()" or "\c(\\)" # i.e. "\\"
no character "\([])" i.e. ""
'''
    assert not (set('()\\') & set(head))
    assert not (set('()') & set(body))
    def from_hex(s):
        return int(s, base=16)
    def from_dec(s):
        return int(s, base=10)
    def ascii_chr(i):
        if not 0<=i<0x100:
            raise _EscapeError('\\a(...) too big')
        return chr(i)

    if head == 'U':
        if body[:2] != 'U+':
            raise _EscapeError('\\U(...) not "U+"')
        return chr(from_hex(body[2:]))
    elif head == 'u':
        return chr(from_hex(body))
    elif head == 'ud':
        return chr(from_dec(body))
    elif head == 'ad':
        return ascii_chr(from_dec(body))
    elif head == 'a':
        return ascii_chr(from_hex(body))
    elif head == 'c':
        d = { r'\n':'\n'
            , r'\t':'\t'
            , r'\r':'\r'
            , r'\a':'\a'
            , r'\b':'\b'
            , r'\f':'\f'
            , r'\v':'\v'
            , r'\\':'\\'
            , r'\'':'\''
            , r'\"':'\"'
            }
        c = d.get(body)
        if c is None: raise _EscapeError(r'unknown "\c({})"'.format(body))
        return c
    elif head == '':
        d = {r'[]': '', r'':'\\'}
        c = d.get(body)
        if c is None: raise _EscapeError(r'unknown "\({})"'.format(body))
        return c
    else:
        raise _EscapeError(r'unknown head "\{}(...)"'.format(head))
def escape_prepare__break(s:str, begin=None, end=None):
    # rex = regex"\\[^()\\]*\([^()]*\)"
    # return [(content,)|(head, body)] | (err_msg, idx)
    if begin is None: begin = 0
    if end is None: end = len(s)
    ls = []
    while begin < end:
        i = s.find('\\', begin, end)
        if i < 0: break
        ls.append((s[begin:i],))
        begin = i+1

        j = s.find(')', begin, end)
        if j < 0:
            return '"\\..." but no ")"', begin-1
        i = s.find('(', begin, j)
        if i < 0:
            return '"\\...)" but no "(" between', begin-1
        if s.find('(', i+1, j) >= 0:
            return '"\\...(...(...)" too many "("', begin-1

        ls.append((s[begin:i], s[i+1:j]))
        begin = j+1
    return ls






def parse_text2simple_body(text, body_type=list):
    return [tree_to_simple_tree(tree, body_type) for tree in parse_text2body(text)]
def parse_text2body(text):
    return ParseBody().text2trees(text)

class ParseBody:
    def __init__(self):
        self.lines = None
        self.body = None
    def text2trees(self, text:str):
        lines = text.split('\n') # not ".splitlines()"
        org_lines = lines
        pairs = map(seperate_indent, lines)


        # record line_no
        # remove white lines
        lines = []
        #for line_no, (indent, (op, payload)) in enumerate(pairs):
        for line_no, (indent, tail) in enumerate(pairs):
            # remove white lines
            if not tail: continue

            op, payload = seperate_op(tail)

            line = Line(line_no, line_no+1, len(indent), op, payload)
            lines.append(line)
        pass
        return self.__parse(lines)
    def __parse(self, lines):
        self.lines = lines
        self.__alias_line_continuation()
        self.__escape()
        self.__remove_free_comment()
        self.__merge()
        self.__alias_2_fence()
        self.__undo_block_dedent()
        self.__remove_nop_if_there_are_siblings()
        self.__verify_body_belong_to_nonleaf()
        self.__verify_indent_rule_and_make_tmp_body()
        self.__remove_nop_and_fence__lines_and_tmp_body()
        self.__verify_first_last_anchors_and_remove_them()
        self.__verify_only_normal_node_and_make_body()
        return self.body

    def __verify_only_normal_node_and_make_body(self):
        # verify only '[#'"+-] ' remains
        for line in self.lines:
            op = line.op
            if not self.is_nonescape_content_op(op):
                raise ParseError('unknown op or logic-error: {!r}'.format(op)
                        , get_line_info_for_exception(line))

        def mk_tree(tmp_node):
            line = tmp_node.line
            op = line.op
            line_no_begin = line.line_no_begin
            line_no_end = line.line_no_end
            content = line.payload
            args = line_no_begin, line_no_end, content
            if op == '# ':
                node = LeafCommentNode(*args)
            elif op == "' ":
                node = LeafDataNode(*args)
            else:
                if op == '" ': cls = NonLeafDataNode
                elif op == '+ ': cls = NonLeafTransparentScopeNode
                elif op == '- ': cls = NonLeafCommentNode
                else: raise logic-error
                body = mk_body(tmp_node.body)
                node = cls(*args, children=body)
            return node
        def mk_body(tmp_body):
            body = [mk_tree(tmp_node)
                    for tmp_node in tmp_body
                    if self.is_nonescape_content_op(tmp_node.line.op)]
            return body
        self.body = mk_body(self.body)


    def may_split_first_last_anchor(self, op):
        # "(^^^|...)[#'"+-]"
        if op[:3] != '^^^' and op[:3] != '...': return None
        if not self.is_first_last_anchors_tail(op[3:]): return None
        return (op[:3], op[3:])
    def is_first_last_anchors_tail(self, s):
        # "#?'?\"?\+?-?"
        return is_subsequence_of(s, '#\'"+-')
    def __verify_first_last_anchors_and_remove_them(self):
        #11) verify "(^^^|...)[#'"+-]" and then remove them
        self.__verify_first_last_anchors()
        self.__remove_first_last_anchors()
    def __remove_first_last_anchors(self):
        def f(line):
            if self.may_split_first_last_anchor(line.op):
                return []
            return [line]
        self.__apply(f)
    def __verify_first_last_anchors(self):
        def verify_body(body):
            occur_ops = set()
            allow_ops = {'# ', "' ", '" ', '+ ', '- '}
            _verify_body(body, occur_ops, allow_ops)
        def _verify_body(body, occur_ops, allow_ops):
            #######
            def handle_other_case(line, op):
                if op not in allow_ops:
                    raise LastAnchorError('forbid by some "...???" op'
                            , get_line_info_for_exception(line))
                occur_ops.add(op)
            def handle_anchor_case(line, c3, tail):
                ops = {c+' ' for c in tail} # expand to {'" ', '# ', "' "}
                if c3 == '^^^':
                    allow_occur_ops = ops
                    if not occur_ops <= allow_occur_ops:
                        raise FirstAnchorError('some forbidden op occurred'
                                , get_line_info_for_exception(line))
                elif c3 == '...':
                    allow_ops &= ops
                else:
                    raise logic-error
            ########
            for node in body:
                line = node.line
                op = line.op
                #if op in {'+ ', '- '}:
                may = self.may_split_first_last_anchor(op)
                if may is None:
                    handle_other_case(line, op)
                else:
                    c3, tail = may
                    handle_anchor_case(line, c3, tail)
        def recur_verify_body(body):
            verify_body(body)
            for node in body:
                recur_verify_body(node.body)
        recur_verify_body(self.body)

    def __remove_nop_and_fence__lines_and_tmp_body(self):
        #10) remove "[]"/".."
        #10) remove "[]"/".." both in lines and the tmp body
        def will_skip(op):
            return op == '[]' or op == '..'
        def f(line):
            if will_skip(line.op): return []
            return [line]
        self.__apply(f)
        def to_new_body(tmp_body):
            tmp_body = [tmp_node for tmp_node in tmp_body
                        if not will_skip(tmp_node.line.op)]
            for tmp_node in tmp_body:
                bd = tmp_node.body
                tmp_node.body = to_new_body(bd)
            return tmp_body
        self.body = to_new_body(self.body)
    def __verify_body_belong_to_nonleaf(self):
        #8) verify body follows only nonleaf node '["+-] '
        lines = self.lines
        for line, succ in zip(lines[:-1], lines[1:]):
            if line.shifted_indent < succ.shifted_indent:
                # line has body
                if not self.is_nonescape_nonleaf_content_op(line.op):
                    raise BodyError('body not belong to a nonleaf node'
                            , get_line_info_for_exception(line))
        return

    def __verify_indent_rule_and_make_tmp_body(self):
        #9) verify indent rule and make tmp body for 11
        lines = self.lines
        self.body = []
        if not lines:
            return
        shifted_indent = lines[0].shifted_indent

        shifted_indent_context = [shifted_indent]
        ancestor_bodies = [self.body]
        # parent's body and its child shifted_indent
        for line in lines:
            body = []
            node = TmpNode(line, body)
            if line.shifted_indent > shifted_indent_context[-1]:
                # indent
                shifted_indent_context.append(line.shifted_indent)
                parent_body = ancestor_bodies[-1][-1].body
                parent_body.append(node)
                ancestor_bodies.append(parent_body)
                continue
            while line.shifted_indent < shifted_indent_context[-1]:
                # dedent
                shifted_indent_context.pop()
                ancestor_bodies.pop()
                if not shifted_indent_context:
                    raise IndentError('less than the indent of first line'
                            , get_line_info_for_exception(line))
            if line.shifted_indent != shifted_indent_context[-1]:
                raise IndentError('mismatch indent'
                        , get_line_info_for_exception(line))
            ancestor_bodies[-1].append(node)
        return
    def __undo_block_dedent(self):
        #6) undo block dedent
        #    verify paired op and payload
        #    ensure no stmt between pair dedent beyond the pair
        #    will remove <<< >>>
        #    will insert ".."
        lines = []
        pair_stack = [] # ((old_left_most, old_offset, new_shifted_indent), open)
        offset = 0
        left_most_offseted_indent = 0
        for line in self.lines:
            op = line.op
            indent = line.indent
            if is_block_dedent_open(op):
                open = line
                old_offset = offset
                old_left_most = left_most_offseted_indent
                del offset, left_most_offseted_indent
                L = len(op) - 2
                assert L >= 0
                # tri = old_offset, old_left_most, shifted_indent = tri
                shifted_indent = None; del shifted_indent

                if is_block_dedent_open__d(op):
                    # this open using new_offset, old_left_most
                    # and block using new_offset, new_left_most
                    new_offset = old_offset + L
                    shifted_indent = new_offset + indent
                    new_left_most = shifted_indent

                    line = line.copy(shifted_indent=shifted_indent
                                    , op='..', payload = '')
                    if not line.shifted_indent >= old_left_most:
                        raise logic-error

                elif is_block_dedent_open__i(op):
                    # this open using old_offset, old_left_most
                    # and block using new_offset, new_left_most
                    new_offset = old_offset - L
                    shifted_indent = old_offset + indent
                    new_left_most = shifted_indent

                    line = line.copy(shifted_indent=shifted_indent
                                    , op='..', payload = '')
                    if not line.shifted_indent >= old_left_most:
                        raise logic-error

                tri = old_offset, old_left_most, shifted_indent
                pair_stack.append((tri, open)) # line is ".." not open now
                offset = new_offset
                left_most_offseted_indent = new_left_most

            elif is_block_dedent_close(op):
                if not pair_stack: raise BlockDedentError('no open'
                                        , get_line_info_for_exception(line))
                tri, open = pair_stack.pop()
                old_offset, old_left_most, shifted_indent = tri

                if not matched_block_dedent_open_close(open, line):
                    raise BlockDedentError('not matched open'
                            , get_line_info_for_exception(line))

                line = line.copy(shifted_indent=shifted_indent
                                , op='..', payload = '')
                offset = old_offset
                left_most_offseted_indent = old_left_most
            else:
                line = line.copy(shifted_indent=line.indent+offset)
                if not line.shifted_indent >= left_most_offseted_indent:
                    raise BlockDedentError(
                        'some in the block dedent too much or '
                        'miss close'
                        , get_line_info_for_exception(line))
            lines.append(line)

        if pair_stack:
            _, line = pair_stack[-1]
            raise BlockDedentError('no close'
                    , get_line_info_for_exception(line))
        self.lines = lines
    def __remove_nop_if_there_are_siblings(self):
        #7) remove "[]" if the containing body is not empty after this action
        lines = self.lines
        reversed_lines = []
        def has_sibling(line):
            if lines:
                prev_line = lines[-1]
                if prev_line.shifted_indent == line.shifted_indent:
                    return True
            if reversed_lines:
                succ_line = reversed_lines[-1]
                if succ_line.shifted_indent == line.shifted_indent:
                    return True
            return False
        while lines:
            line = lines.pop()
            op = line.op
            if op == '[]' and has_sibling(line):
                del line
                continue
            reversed_lines.append(line)
        reversed_lines.reverse()
        self.lines = reversed_lines


    def __alias_2_fence(self):
        #5) alias "..~"/"." to "[]"
        def f(line):
            op = line.op
            if op == '.' or op == '..~':
                line = line.copy(op = '[]')
            return [line]
        self.__apply(f)
    def __merge(self):
        # 4) merge '\\ ' and '; '
        '''
        will remove "\\ " and "; "
        from last line to first line:
            if current op is "\\ " or "; ":
                while True:
                    upper = the upper op
                    assert upper have same indent
                    if upper is "[]":
                        remove upper line
                        continue
                    if upper is "." and current op is "; ":
                        remove upper line
                        continue
                    if upper is regex"[\\;#'"] ": # content ops
                        merge current payload to upper payload
                        # "; " will insert a newline
                        break
                    else:
                        raise
        '''
        # payload -> [payload] # reversed payload
        def f(line):
            payload = line.payload
            if line.op == '; ':
                payload = '\n' + payload
            return [line.copy(payload = [payload])]
        self.__apply(f)
        lines = self.lines
        def merge(line):
            return [line.copy(payload = ''.join(reversed(line.payload)))]
        # will call: self.__apply(merge)

        def get_upper(line):
            if not lines:
                raise ContinuationError('no upper'
                        , get_line_info_for_exception(line))
            upper = lines[-1]
            if upper.indent != line.indent:
                raise ContinuationError('no upper'
                        , get_line_info_for_exception(line))
            return upper
        reversed_lines = []
        while lines:
            line = lines.pop()
            op = line.op
            if op != '\\ ' and op != '; ':
                reversed_lines.append(line)
                continue
            while True:
                upper = get_upper(line)
                if upper.op == '[]':
                    lines.pop()
                    continue
                if upper.op == '.' and op == '; ':
                    lines.pop()
                    continue
                if not self.is_nonescape_continuable_op(upper.op):
                    raise ContinuationError('upper is not content op'
                            , get_line_info_for_exception(line))
                break
            # merge
            line.payload.extend(upper.payload)
            upper.payload = line.payload
            upper.line_no_end = line.line_no_end
            del line

        reversed_lines.reverse()
        self.lines = reversed_lines
        self.__apply(merge)

    def is_nonescape_nonleaf_content_op(self, op):
        return op in {'" ', '+ ', '- '}
    def is_nonescape_leaf_content_op(self, op):
        return op in {"' ", '# '}
    def is_nonescape_continuable_op(self, op):
        return op in {'\\ ', '; '} or self.is_nonescape_content_op(op)
    def is_nonescape_content_op(self, op):
        # r'[#'"+-] '
        # {'# ', '" ', "' ", '+ ', '- '}
        return self.is_nonescape_leaf_content_op(op) or \
            self.is_nonescape_nonleaf_content_op(op)


    def __remove_free_comment(self):
        # 3) remove free comments: op == '! '
        def f(line):
            op = line.op
            if op == '! ':
                return []
            return [line]
        self.__apply(f)

    def is_escape_op(self, op):
        return op[1:2] == '^'
    def escape_op2normal_op(self, op):
        assert self.is_escape_op(op)
        return op[0] + op[2:]
    def __escape(self):
        #2) escape "?^ "
        #    op like ";^ " will translated to "; "
        #    will verify "!^ " too
        def f(line):
            op = line.op
            if self.is_escape_op(op):
                try:
                    payload = self.__escape_payload__(line.payload)
                except Exception as e:
                    raise EscapeError(e, get_line_info_for_exception(line))
                line = line.copy(payload=payload, op=self.escape_op2normal_op(op))
            return [line]
        return self.__apply(f)
    def __escape_payload__(self, payload):
        # str -> str
        return escape(payload)
        raise NotImplementedError
    def __apply(self, f):
        self.lines = list(chain.from_iterable(map(f, self.lines)))

    def __alias_line_continuation(self):
        # 1) alias "\-+ "
        #   "\\-* " ==>> "\\ "
        #   "\\^-* " ==>> "\\^ "
        def f(line):
            if is_line_continuation_op(line.op):
                return [line.copy(op = '\\ ')]
            op = line.op
            if op[:2] == '\\^' and is_line_continuation_op('\\'+op[2:]):
                return [line.copy(op = '\\^ ')]
            return [line]
        self.__apply(f)





def _test():
    assert parse_text2simple_body('') == []
    assert parse_text2simple_body('  ') == []
    assert parse_text2simple_body(' \n  ') == []
    assert parse_text2simple_body(' \n ! ') == []
    assert parse_text2simple_body('" \n ! ') == [(3, '', [])]
    assert parse_text2simple_body('\' \n ! ') == [(1, '', None)]
    assert parse_text2simple_body('# \n ! ') == [(-1, '', None)]
    assert parse_text2simple_body('\' \n; ! ') == [(1, '\n! ', None)]
    assert parse_text2simple_body('\' \n\\ ! ') == [(1, '! ', None)]
    txt = '''
        " A
            ' B
            ' C
            " D
                " E0
                \\------ E1
                .
                ; E2
                .
                ..
            # c
          ! fafa
        # c

    '''
    pass
    assert parse_text2simple_body(txt) == \
            [(3, 'A',
              [(1, 'B', None),
               (1, 'C', None),
               (3, 'D', [(3, 'E0E1\nE2', [])]),
               (-1, 'c', None)]),
             (-1, 'c', None)]
    txt = '''
        " R
      <<<<<<< tg xxx
      # here
      ' A
      >>>>>>> tg xxx
            ' B
        '''
    assert parse_text2simple_body(txt) == \
        [(3, 'R', [(-1, 'here', None), (1, 'A', None), (1, 'B', None)])]
    return
    from pprint import pprint
    r = parse_text2simple_body(txt)
    pprint(r)
_test()




