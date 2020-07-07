# find 全角 "..."
assert "…" == "\u2026"

rg = range
pr=print
def sw(a):
	pr(a, end='')


pr(chr(0x2026))

def f():
	off = 0xa0+1
	for i in rg(17):
		for j in rg(94):
			bs=bytes([off+i, off+j])
			try:
				ch=bs.decode('gbk')
			except:
				pr();pr(i);pr(j)
				raise
			sw(ch)
		pr()

f()


"""
/storage/emulated/0 $ cd /sdcard/0my_files/txt/script/      /storage/emulated/0/0my_files/txt/script $ python find_sym.py                                                           　、。·ˉˇ¨〃々—～‖…‘’“”〔〕〈〉《》「」『』〖〗【】±×÷∶∧∨∑∏∪∩∈∷√⊥∥∠⌒⊙∫∮≡≌≈∽∝≠≮≯≤≥∞∵∴♂♀°′″℃＄¤￠￡‰§№☆★○●◎◇◆□■△▲※→←↑↓〓  ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹTraceback (most recent call last):                  File "find_sym.py", line 16, in <module>                      f()                                                       File "find_sym.py", line 12, in f                             ch=bs.decode('gbk')                                     UnicodeDecodeError: 'gbk' codec can't decode byte 0xa2 in position 0: illegal multibyte sequence                        /storage/emulated/0/0my_files/txt/script $ python find_sym.py                                                           　、。·ˉˇ¨〃々—～‖…‘’“”〔〕〈〉《》「」『』〖〗【】±×÷∶∧∨∑∏∪∩∈∷√⊥∥∠⌒⊙∫∮≡≌≈∽∝≠≮≯≤≥∞∵∴♂♀°′″℃＄¤￠￡‰§№☆★○●◎◇◆□■△▲※→←↑↓〓  ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ                                                  1                                                           10                                                          Traceback (most recent call last):
  File "find_sym.py", line 20, in <module>
    f()
  File "find_sym.py", line 13, in f
    ch=bs.decode('gbk')
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa2 in position 0: illegal multibyte sequence
/storage/emulated/0/0my_files/txt/script $
"""
