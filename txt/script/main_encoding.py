#main_encoding.py

from encoding import main

basedir = "/storage/emulated/0/Download/闪电下载/大明王朝1566/"
id = f"{basedir}gb字幕"
od = f"{basedir}u8字幕"

main([
	*'-ie gb18030 -oe utf8'.split()
	,'-id', id
	,'-od', od
	])



