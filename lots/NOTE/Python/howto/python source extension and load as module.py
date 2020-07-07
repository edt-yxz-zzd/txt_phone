'''
py36 - 31.5.6.3. Importing a source file directly
https://stackoverflow.com/questions/19009932/import-arbitrary-python-source-file-python-3-3



#spec = spec_from_loader("xxx.XXX", SourceFileLoader("xxx.XXX", "/path/to/XXX.weird_extension"), is_package=???)

#################
importlib.machinery.SOURCE_SUFFIXES
    .append('') # allow any suffixes???
    .append('.exe_py') # my suffix
    see:
        "NOTE\Python\howto\python startup configuration.txt"
'''

__all__ = '''
    load_as_package
    load_as_module
    load_as_module_or_package
    '''.split()

from importlib.util import (spec_from_loader, spec_from_file_location, module_from_spec)
from importlib.machinery import SourceFileLoader
import sys
from pathlib import Path


if False:
    assert Path('.').resolve() != Path('.')
    assert str(Path('.').resolve()) != str(Path('.'))
    assert Path('.').resolve().samefile(Path('.'))

def load_as_package(
    pkg_qname, pkg_source_path):
    #assert submodule_search_locations is not None
    return load_as_module_or_package(pkg_qname, pkg_source_path, True)

def load_as_module(module_qname, module_source_path):
    return load_as_module_or_package(module_qname, module_source_path, False)
def load_as_module_or_package(
    qname, source_path, is_package:bool):
    #assert maybe_submodule_search_locations is None or iter(maybe_submodule_search_locations)
    assert type(qname) is str
    if not (qname and qname[0] != '.'): raise ValueError

    if qname in sys.modules:
        try:
            return sys.modules[qname]
        except KeyError:
            pass


    def make_maybe_parent_bare(may_qname):
        if not may_qname: return None
        qname = may_qname
        maybe_parent_package_qname, may_sep, bare_name = qname.rpartition('.')
        # maybe_parent_package_qname may be ''
        if not maybe_parent_package_qname:
            maybe_parent_package_qname = None
        assert bare_name
        assert '.' not in bare_name
        return maybe_parent_package_qname, bare_name


    #is_package = maybe_submodule_search_locations is not None
    is_package = bool(is_package)
    maybe_submodule_search_locations = [] if is_package else None

    maybe_parent_package_qname, bare_name = make_maybe_parent_bare(qname)
    Nothing = object()
    if maybe_parent_package_qname:
        parent_package_qname = maybe_parent_package_qname
        if parent_package_qname not in sys.modules:
            # before exec_module to support relative import
            raise ImportError(f'import module_or_package={qname!r}, but parent_package={parent_package_qname!r} was not imported yet')

        parent_package = sys.modules[parent_package_qname]
        if getattr(parent_package, bare_name, Nothing) is not Nothing:
            raise ImportError(f'import module_or_package={qname!r}, but parent_package={parent_package_qname!r} has attribute {bare_name!r}')


    spec = spec_from_file_location(qname
                                , source_path
                                , submodule_search_locations
                                  = maybe_submodule_search_locations
                                )
    module = module_from_spec(spec)

    if is_package:
        submodule_search_locations = maybe_submodule_search_locations
        assert iter(submodule_search_locations)
        __package__ = qname
        __path__ = submodule_search_locations
    else:
        __package__ = maybe_parent_package_qname
        __path__ = None
    #rint(f'{module.__package__} == {__package__}')
    assert module.__package__ == __package__
    assert getattr(module, '__path__', None) is __path__
    if is_package:
        [parent_folder] = module.__path__
        assert Path(source_path).parent.samefile(Path(parent_folder))


    #sys.modules[qname] = module
    new_module = sys.modules.setdefault(qname, module)
        # before exec_module to support recursive import
        # before exec_module to support relative import if is_package
    if new_module is not module:
        return new_module
    try:
        if maybe_parent_package_qname:
            assert getattr(parent_package, bare_name, Nothing) is Nothing
            setattr(parent_package, bare_name, module)
        assert sys.modules[qname] is module
        assert not maybe_parent_package_qname or getattr(parent_package, bare_name, Nothing) is module

        try:
            spec.loader.exec_module(module)
        except:
            delattr(parent_package, bare_name)
            raise
    except:
        sys.modules.pop(qname)
        raise
    return module

def _f():
    import seed
    pkg_source_path = Path(seed.__file__).parent / "abc/__init__.py"
    pkg_qname = 'seed.abc'
    module_source_path = Path(seed.__file__).parent / "abc/abc.py"
    module_qname = 'seed.abc.abc'

    try:
        seed.abc
    except:
        pass
    else:
        raise logic-error

    m = load_as_package(pkg_qname, pkg_source_path)
    print(m)
    print(m.__path__)

    seed.abc

    m = load_as_module(module_qname, module_source_path)
    print(m)
    print(getattr(m, '__path__', None))
    seed.abc.abc


if __name__ == '__main__':
    _f()
