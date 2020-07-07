

class VLine:
    # may be line, logic line, node content, leaf comment
    def __init__(self, line_no_begin, line_no_end, indent:int, op, payload, real_indent, shifted_indent:int=None):
        # for logic line
        self.line_no_begin = line_no_begin
        self.line_no_end = line_no_end

        self.indent = indent
        self.op = op
        self.payload = payload

        self.shifted_indent = shifted_indent
    def get_args(self):
        return (self.line_no_begin, self.line_no_end
                , self.indent, self.op, self.payload, self.shifted_indent)
    def copy(self, **kwargs):
        d = dict(line_no_begin=self.line_no_begin, line_no_end=self.line_no_end
                , indent=self.indent, op=self.op, payload=self.payload
                , shifted_indent=self.shifted_indent)
        d.update(kwargs)
        return type(self)(**d)

class Line(VLine):pass
class LogicLine(VLine):pass
class NodeContent(VLine):
    # node content or leaf comment
    pass

class Node:
    def __init__(self, parent:'Maybe Node', content:'Maybe str'):
        self.__content = content
        self.__children = []

        self.__enter_body = False
        self.__exit_body = False
        self.__parent = None
        if parent is not None:
            parent.add_child(self)
    @property
    def parent(self):
        return self.__parent
    @property
    def content(self):
        return self.__content

    def __len__(self):
        return len(self.__children)
    def __getitem__(self, i):
        return self.__children[i]
    def add_children(self, children):
        for child in children:
            self.add_child(child)
    def enter(self):
        return self.__enter_body
    def set_enter(self):
        if self.__enter_body: raise logic-error
        self.__enter_body = True
    def exit(self):
        return self.__exit_body
    def set_exit(self):
        if self.__exit_body: raise logic-error
        self.__exit_body = True
    def add_child(self, child):
        if not self.__enter_body or self.__exit_body:
            raise logic-error
        if child.__parent is None:
            self.__children.append(child)
            child.__parent = self
        raise ValueError('child had parent)




class ParseError(Exception):
    def __init__(self, msg, line_no):
        super().__init__(msg)
        self.line_no = line_no
class ContinuationError(ParseError):pass
class IndentError(ParseError):pass
class BlockDedentError(ParseError):pass

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
    # r'<* "
    return op[-1] == ' ' and all_are_the_char(op[:-1], '<')
def is_block_dedent_close(op):
    # r'>* "
    return op[-1] == ' ' and all_are_the_char(op[:-1], '>')
def is_block_dedent_op(op):
    return is_block_dedent_close(op) or is_block_dedent_open(op)

def is_line_continuation_op(op):
    # r'\\-* '
    return (op[0] == '\\' and op[-1] == ' '
        and all_are_the_char('-', op[1:-1])
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



def text2tree(text:str):
    lines = text.split('\n') # not ".splitlines()"
    pairs = map(seperate_indent, lines)

    '''
    bug: line_no
    # remove white lines
    # pairs : [(indent, (op, maybe_space, payload))]
    pairs = ((indent, seperate_op(tail)) for (indent, tail) in pairs if tail)
    '''

    # remove white lines
    # remove free comments: op == '#! '
    _lines = []
    #for line_no, (indent, (op, payload)) in enumerate(pairs):
    for line_no, (indent, tail) in enumerate(pairs):
        # remove white lines
        if not tail: continue

        op, payload = seperate_op(tail)
        # remove free comments: op == '#! '
        if op == '#! ': continue

        _line = Line(line_no, line_no+1, len(indent), op, payload)
        _lines.append(_line)
    pass
    ###############################
    # replace "' " by ".." + "; " + ".."
    # replace r"\\-* " by r"\\ "
    old_lines = lines
    lines = []
    for _line in _lines:
        op = _line.op
        if op == "' ":
            dotdot = _line.copy(op='..', payload='')
            new = _line.copy(op='; ')
            lines += [dotdot, new, dotdot]
        elif is_line_continuation_op(op):
            new = _line.copy(op='\\ ')
            lines.append(new)
        else:
            lines.append(_line)
    _lines = lines
    ###############################
    # shift <<< >>> block using ^^^ ...
    opens = []
    lines = []
    offset = 0
    for _line in _lines:
        op = _line.op
        if is_block_dedent_open(op):
            inner_indent = _line.indent
            offset = calc_offset(offset, op)
            outer_indent = inner_indent + offset
            shifted_indent = outer_indent
            # replaced by ^^^
            line = _line.copy(shifted_indent=shifted_indent, op='^^^', payload='')
            opens.append(_line)
            lines.append(line)
        elif is_block_dedent_close(op):
            if not opens:
                raise BlockDedentError('missing open', _line.line_no)
            open = opens.pop()
            if open.indent != _line.indent:
                raise BlockDedentError('open and close have diff indent', _line.line_no)
            if len(open.op) != len(_line.op) or open.payload != _line.payload:
                raise BlockDedentError('open and close mismatch', _line.line_no)
            # replaced by ...
            inner_indent = _line.indent
            outer_indent = inner_indent + offset
            shifted_indent = outer_indent
            line = _line.copy(shifted_indent=shifted_indent, op='...', payload='')
            lines.append(line)
            offset = calc_offset(offset, op)
        else:
            line = _line.copy(shifted_indent=_line.indent + offset)
            lines.append(line)
        assert offset >= 0

    if opens:
        open_line = opens[-1]
        raise BlockDedentError('missing close', open_line.line_no)
    _lines = lines
    ###############################
    # body
    #   have no body: "# ", "...", "^^^"
    #   "."/".." if has body, then upper sibling must exist, remove the '.'/'..'
    #   "^^^" has parent, be first op
    #   "..." has parent, be last op
    #   "\\ " has a upper sibling which is one of "; ", "# ", "\\ "
    def has_body(i, _lines):
        return (i+1 < len(_lines)
            and _lines[i].shifted_indent < _lines[i+1].shifted_indent
            )
    def has_upper_sibling(i, _lines):
        # immediate upper sibling
        return i-1>=0 and _lines[i].shifted_indent == _lines[i-1].shifted_indent
    lines = []
    can_have_body = False
    for i, _line in enumerate(_lines):
        lines.append(_line)
        op = _line.op
        if has_upper_sibling(i, _lines):
            can_have_body = False
        elif op in {'# ', '...', '^^^'}:
            can_have_body = False

        if op in {'# ', '...', '^^^'} and has_body(i, _lines):
            raise OpError('cannot have body', _line.line_no)
        if op == '^^^':
            if i-1 < 0:
                raise OpError('"^^^" should have parent', _line.line_no)
            if _lines[i-1].shifted_indent >= _line.shifted_indent:
                raise OpError('"^^^" not the first op in a body',_line.line_no)
        elif op == '...':
            if i+1 < len(_lines) and _lines[i+1].shifted_indent >= _line.shifted_indent:
                raise OpError('"..." not the last op in a body',_line.line_no)
        elif op in ['.', '..'] and has_body(i, _lines):
            while op in ('.', '..'):
                if not has_upper_sibling(i, _lines):
                    raise OpError(
                        '"."/".." can not have body without a immediate upper sibling'
                        , _line.line_no)
                lines.pop()
            # skip: append === remove
            lines.pop()
            pass
        elif op == '\\ ':
            if not has_upper_sibling(i, _lines):
                raise OpError(
                    '"\\ " should be under some upper sibling', _line.line_no)
            if _lines[i-1].op not in ["; ", "# ", "\\ "]:
                raise OpError(
                    '"\\ " should be under "; " or "# " or "\\ "', _line.line_no)
    #########################
    # indent


























    # is_block_dedent_op?
    # begin_indent, end_indent
    # if dedent out indent context, then add new virtual node
    indentss = [] # push by <<<; pop by >>>
    opens = []
    indents = [0] # indent context # not support virtual node
    # root = Node(None, [], None)
    # parent = root
    offset = 0
    siblings = []
    stop = '' # '' or '.' or '..'
    def flush():pass
    def enter_body():
        for node in reversed(siblings):
            op = node.content.op
            if op in {'.', '..'}: continue
            if is_block_dedent_op(op):
                raise IndentError('body of block_dedent_op', _line.line_no)
            if op == '# ':
                raise IndentError('body of comment', _line.line_no)

        if not siblings:
            raise IndentError('enter body without a parent')
    def push_indent_context(indent):
        nonlocal indents
        indentss.append(indents)
        indents = [indent]
    def pop_indent_context():
        nonlocal indents
        indents = indentss.pop()
    for _line in _lines:
        op = _line.op
        if is_block_dedent_open(op):
            end_indent = _line.indent
            doffset = calc_doffset(op)
            begin_indent = end_indent + doffset
            if indents[-1] < begin_indent:
                # indent to begin_indent and then shift to end_indent
                offset += doffset
                push_indent_context(end_indent)
            else:
                raise BlockDedentError('open should be first op of a body')


    ###############################
    set_shifted_indent_and_test_block_dedent__well_pair_and_nonnegative_offset(_lines)
    # shifted_indent of _lines are offsetted
    # test indent
    if not _lines: return Node(None, [], None)
    min_shifted_indents = find_min_shifted_indents_for_virtual_nodes(_lines)
    test_block_dedent_whole_body(_lines)
    test_well_dedent(_lines)


def calc_doffset(op):
    if is_block_dedent_open(op):
        assert len(op) >= 2
        #offset += len(op) - 2
        return len(op) - 2
    elif is_block_dedent_close(op)
        assert len(op) >= 2
        # offset -= len(op) - 2
        return 2 - len(op)
        # offset < 0 ==>> error
    return offset

def calc_offset(offset, op):
    if is_block_dedent_open(op):
        assert len(op) >= 2
        offset += len(op) - 2
    elif is_block_dedent_close(op)
        assert len(op) >= 2
        offset -= len(op) - 2
        # offset < 0 ==>> error
    return offset
def set_shifted_indent_and_test_block_dedent__well_pair_and_nonnegative_offset(_lines):
    # test <<< >>> pair; not consider whole indent a body
    # set shifted_indent of _lines
    # shift indent by <<<< >>>>


    opens = [] # [(Line, op)]
    offset = 0
    for _line in _lines:
        op = _line.op
        offset = calc_offset(offset, op)
        if is_block_dedent_open(op):
            opens.append((_line, op))
        elif is_block_dedent_close(op):
            if not opens:
                raise BlockDedentError(
                    'missing open for block dedent close', _line.line_no)
            _open_line, open = opens.pop()
            if len(open) != len(close):
                raise BlockDedentError(
                    'block dedent open mismatch block dedent close'
                    , _line.line_no)
            pass
        if offset < 0:
            raise logic-error # I think this would be prevent by pair mismatch
            raise BlockDedentError('offset < 0', _line.line_no)

        ###### set shifted_indent
        _line.shifted_indent += _line.indent + offset
    if opens:
        open_line, _ = opens.pop()
        raise BlockDedentError(
            'missing close for block dedent open', open_line.line_no)
    return

def find_min_shifted_indents_for_virtual_nodes(_lines):
    # _lines not empty
    # min_shifted_indents are sorted
    # min_shifted_indents[-1] == _lines[0].shifted_indent
    assert _lines
    min_shifted_indent = _lines[0].shifted_indent
    min_shifted_indents = [min_shifted_indent]
    for _line in _lines:
        if _line.shifted_indent < min_shifted_indent:
            min_shifted_indent = _line.shifted_indent
            min_shifted_indents.append(prev_min_indent)
    min_shifted_indents.reverse()
    return min_shifted_indents

def test_block_dedent_whole_body(_lines):
    for i, _line in enumerate(_lines):
        op = _line.op
        if is_block_dedent_open(op):
            if i > 0:
                prev = _lines[i-1]
                if not prev.shifted_indent < _line.shifted_indent:
                    raise BlockDedentError('not first op of body', _line.line_no)
        elif is_block_dedent_close(op):
            if i+1 < len(_lines):
                succ = _lines[i+1]
                if not succ.shifted_indent < _line.shifted_indent:
                    raise BlockDedentError('not last op of body', _line.line_no)
def test_well_dedent(min_shifted_indents, _lines)
    assert min_shifted_indents
    assert _lines

    indents = list(min_shifted_indents)
    for _line in _lines:
        op = _line.op

        indent = _line.shifted_indent
        if indent > indents[-1]:
            # indent
            indents.append(indent)
            continue
        while indent < indents[-1]:
            # dedent
            indents.pop()
        if indent != indents[-1]:
            raise IndentError('indent error', _line.line_no)
    # no indent error
    return

    # group continuous _lines by indent
    groups = []
    prev_indent = 'not equal to any indent'
    for _line in _lines:
        if _line.indent == prev_indent:
            groups[-1].append(_line)
        else:
            groups.append([_line])
            prev_indent = _line.indent
    pass

    # join_logic_lines
    logic_line_groups = list(map(join_lines_to_logic_lines, groups))

    # cancel ops: '.', '\\ '
    node_content_groups = list(map(join_multi_logic_lines_to_contents, logic_line_groups))

    # remain ops: "; ", "# ", "<* ", ">* "

    # match block dedent pairs
    # dedent whole body; not just dedent a partial body
    # # undo dedent # maynot need
    # make tree


    # match block dedent pairs
    block_dedent_open_no2close_no = {} # line_no map
    root = Node(None, [], None, None, None)
    opens = []
    first_child_of_root = None
    for g in node_content_groups:
        for content in g:
            op = content.op
            if op == '; ':
                # content
                if first_child_of_root is None:
                    first_child_of_root = Node(root, [], content, None, None)

















def join_lines_to_logic_lines(_line_group:[Line])
    # join multi-line to a logic line
    # result are of same type; but without '\\ '
    # there may be a leading ". " op per body, no other ". "
    sep = ''

    logic_lines = []
    prev_lines = None # [_line]
    prev_op = None
    def flush_prev_logic_line():
        if prev_op is None: return
        logic_line = LogicLine(
            prev_lines[0].line_no_begin, prev_lines[-1].line_no_end
            , prev_lines[0].indent, prev_lines[0].op
            , sep.join(_line.payload for _line in prev_lines)
            )
        logic_lines.append(logic_line)

    for _line in _line_group:
        op = _line.op
        payload = _line.payload

        if is_line_continuation_op(op):
            # to join to prev logic line
            if prev_op is None:
                raise ContinuationError(
                    'line continuation "\\ " without prev line'
                    , _line.line_no_begin)
            if prev_op not in {'; ', '# '}:
                raise ContinuationError(
                    'line continuation "\\ "\'s prev op is not "; " or "# "'
                    , _line.line_no_begin)
            prev_lines.append(payload)
            continue

        # flush prev logic line
        flush_prev_logic_line()

        # update: prev_op, prev_lines
        # begin a new logic line
        prev_op = op
        prev_lines = [payload]
        if logic_lines and op == '.':
            # set no prev for continuation
            # test logic_lines to ensure the result body is not empty
            assert payload == ''
            prev_op = None
            prev_lines = None
    else:
        flush_prev_logic_line()
    pass
    return logic_lines

















def join_multi_logic_lines_to_contents(logic_line_group:[LogicLine])
    # join multi-line to a node content/comment
    # result are of same type; but now the payload contains "\n"
    # "' " disappeared
    sep = '\n'

    # group by op
    logic_line_groups = []
    prev_op = ' not op'
    for logic_line in logic_line_group:
        if logic_line.op == prev_op:
            logic_line_groups[-1].append(logic_line)
        else:
            logic_line_groups.append([logic_line])
            prev_op = logic_line.op
    del logic_line

    # join multi-logic-line-node-content
    node_contents = []
    for g in logic_line_groups:
        op = g[0].op
        if op == "' " or is_block_dedent_op(op):
            # single logic line
            if op == "' ":
                op = "; "
            for logic_line in g:
                content = NodeContent(*logic_line.get_args())
                content.op = op
                node_contents.append(content)
            del logic_line
        elif op == '; ' or op == '# ':
            # multi logic line
            content = NodeContent(
                g[0].line_no_begin, g[-1].line_no_end
                , g[0].indent, g[0].op
                , sep.join(logic_line.payload for logic_line in g)
                )
            node_contents.append(content)

        else:
            raise OpError('unknown op: {!r}'.format(op), g[0].line_no)
    return node_contents

