


#############################################
#https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python
from tkinter import Tk, TclError
def copy_from_clipboard__ver1__good():
    # work for global clipboard!!
    # -> (str|None)
    # get a str or nothing
    r = Tk()
    r.withdraw()
    # _tkinter.TclError: CLIPBOARD selection doesn't exist or form "STRING" not defined

    try:
        result = r.clipboard_get()
    except TclError:
        result = None
    r.destroy()
    return result

    # both are the same
    try:
        result1 = r.selection_get(selection = "CLIPBOARD") #Get contents of clipboard
    except Exception as e:
        result1 = repr(e)
        result1 = None

    try:
        result2 = r.clipboard_get()
    except Exception as e:
        result2 = repr(e)
        result2 = None
    r.destroy()
    return (result1, result2)

def paste_to_clipboard__ver1__bad(s):
    # donot write to global clipboard!!!
    #   work for local clipboard
    assert type(s) is str

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(s)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
    return

copy_from_clipboard = copy_from_clipboard__ver1__good
paste_to_clipboard = paste_to_clipboard__ver1__bad
#######################################################
#http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/
import ctypes
import locale
global_encoding = 'utf_16_le' # error
global_encoding = 'gb18030' # success but...
global_encoding = locale.getpreferredencoding(False) # cp936 # success
def cygwinGetClipboard():
    ctypes.cdll.user32.OpenClipboard(0)
    pcontents = ctypes.cdll.user32.GetClipboardData(1) # 1 is CF_TEXT
    data = ctypes.c_char_p(pcontents).value
    #ctypes.cdll.kernel32.GlobalUnlock(pcontents)
    ctypes.cdll.user32.CloseClipboard()
    return data

def cygwinSetClipboard(text):
    text = str(text)
    GMEM_DDESHARE = 0x2000
    ctypes.cdll.user32.OpenClipboard(0)
    ctypes.cdll.user32.EmptyClipboard()

    try:
        # works on Python 2 (bytes() only takes one argument)
        hCd = ctypes.cdll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text))+1)
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        hCd = ctypes.cdll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text, global_encoding))+1)
    pchData = ctypes.cdll.kernel32.GlobalLock(hCd)

    try:
        # works on Python 2 (bytes() only takes one argument)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text))
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text, global_encoding))
    ctypes.cdll.kernel32.GlobalUnlock(hCd)
    ctypes.cdll.user32.SetClipboardData(1, hCd) # CF_TEXT=1
    ctypes.cdll.user32.CloseClipboard()

copy_from_clipboard__ver2__good = cygwinGetClipboard
paste_to_clipboard__ver2__good = cygwinSetClipboard
copy_from_clipboard = copy_from_clipboard__ver2__good
paste_to_clipboard = paste_to_clipboard__ver2__good
################################################
# win32 library
from win32clipboard import OpenClipboard, CloseClipboard, GetClipboardData, EmptyClipboard, SetClipboardData
from win32con import CF_TEXT, CF_UNICODETEXT
global_encoding = 'utf_16_le' # error
global_encoding = 'gb18030' # success but...
global_encoding = locale.getpreferredencoding(False) # cp936 # success
def copy_from_clipboard__ver3__good():
    # work!!
    # -> (None|str)
    OpenClipboard(0)
    try:
        #r = GetClipboardData(CF_TEXT).decode(global_encoding) # get clipboard data
        r = GetClipboardData(CF_UNICODETEXT) # get clipboard data
    except TypeError:
        # TypeError: Specified clipboard format is not available
        r = None
    else:
        r = r.split('\0')[0]
    CloseClipboard()
    assert r is None or (type(r) is str and '\0' not in r)
    return r

def paste_to_clipboard__ver3__good(s):
    if type(s) is not str: raise TypeError
    if '\0' in s: raise ValueError

    OpenClipboard(0)
    EmptyClipboard()
    #SetClipboardData(CF_TEXT, s.encode(global_encoding)) # set clipboard data
    SetClipboardData(CF_UNICODETEXT, s) # set clipboard data
    CloseClipboard()
copy_from_clipboard = copy_from_clipboard__ver3__good
paste_to_clipboard = paste_to_clipboard__ver3__good

######################################
def verify_text(s):
    return type(s) is str and '\0' not in s
def check_text(s):
    if type(s) is not str: raise TypeError
    if '\0' in s: raise ValueError
    return
try:
    raise BaseException
except:
    pass

CF_UNICODETEXT = 13
GMEM_MOVEABLE=0x0002
def mine_cygwinGetClipboard():
    # -> (None|str)
    if not ctypes.cdll.user32.OpenClipboard(0): raise Exception
    try:
        hMem = ctypes.cdll.user32.GetClipboardData(CF_UNICODETEXT)
        if not hMem: return None
        try:
            buffer_ptr = ctypes.c_wchar_p(ctypes.cdll.kernel32.GlobalLock(hMem))
            try:
                if not buffer_ptr: raise Exception
                text = buffer_ptr.value
            finally:
                ctypes.cdll.kernel32.GlobalUnlock(hMem)
        finally:
            # bug:ctypes.cdll.kernel32.GlobalFree(hMem)
            pass
    finally:
        ctypes.cdll.user32.CloseClipboard()
    #text = wdata.decode('utf_16_le')
    return text
def mine_cygwinSetClipboard(text):
    check_text(text)
    #text += '\U00101F1F' # used to let "len(wdata) > len(text)+1"
    #
    #bug: one python.char ==>> one or two c.wchar
    #   wdata = ctypes.create_unicode_buffer(text, len(text)+1)
    #   assert wdata[len(text)] == '\0'
    #
    wdata = ctypes.create_unicode_buffer(text+'\0')
    assert wdata[-1] == '\0'
    assert len(wdata) >= len(text)+1
    num_bytes = ctypes.sizeof(wdata)
    #bug?: assert num_bytes == 2*len(wdata)
    #print(f'wdata.value={wdata.value!r}')

    ctypes.cdll.user32.OpenClipboard(0)
    try:
        ctypes.cdll.user32.EmptyClipboard()
        hMem = ctypes.cdll.kernel32.GlobalAlloc(GMEM_MOVEABLE, num_bytes)
        if not hMem: raise Exception
        try:
            buffer_ptr = ctypes.c_wchar_p(ctypes.cdll.kernel32.GlobalLock(hMem))
            if not buffer_ptr: raise Exception
            try:
                # bug: strncpy at most n, will trunc if '\0'
                #   ctypes.cdll.msvcrt.strncpy(buffer_ptr, wdata, num_bytes)
                # no wmemcpy??
                #   ctypes.cdll.msvcrt.wmemcpy(buffer_ptr, wdata, len(wdata))
                ctypes.cdll.msvcrt.memcpy(buffer_ptr, wdata, num_bytes)
            finally:
                ctypes.cdll.kernel32.GlobalUnlock(hMem)
            #print(f'buffer_ptr.value={buffer_ptr.value!r}')
        except:# BaseException:
            ctypes.cdll.kernel32.GlobalFree(hMem)
            raise
        ctypes.cdll.user32.SetClipboardData(CF_UNICODETEXT, hMem)
    finally:
        ctypes.cdll.user32.CloseClipboard()
copy_from_clipboard__ver4__good = mine_cygwinGetClipboard
paste_to_clipboard__ver4__good = mine_cygwinSetClipboard
copy_from_clipboard = copy_from_clipboard__ver4__good
paste_to_clipboard = paste_to_clipboard__ver4__good


#############################
def show_result(result):
    print(repr(result))
    return
    r1, r2 = result
    print(repr(r1))
    print('-'*70)
    print(repr(r2))
def main():
    import sys
    s = copy_from_clipboard()
    show_result(s)
    print()
    print('='*70)
    print()
    #paste_to_clipboard(str(sys.argv)+'-\n1\n\r2\r3\r\n4\0abc')
    #   \0 will be truncated
    paste_to_clipboard(str(sys.argv)+'-\n1\n\r2\r3\r\n4')
    s = copy_from_clipboard()
    show_result(s)
    print()


version = 4
if version == 1:
    copy_from_clipboard = copy_from_clipboard__ver1__good
    paste_to_clipboard = paste_to_clipboard__ver1__bad ######### bad
elif version == 2:
    copy_from_clipboard = copy_from_clipboard__ver2__good
    paste_to_clipboard = paste_to_clipboard__ver2__good
elif version == 3:
    copy_from_clipboard = copy_from_clipboard__ver3__good
    paste_to_clipboard = paste_to_clipboard__ver3__good
elif version == 4:
    copy_from_clipboard = copy_from_clipboard__ver4__good
    paste_to_clipboard = paste_to_clipboard__ver4__good

main()


