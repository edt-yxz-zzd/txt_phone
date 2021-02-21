


this:
  script/draw_tri_planar_graphs.py.data/hand_draw-readme.txt
final output:
  /sdcard/0my_files/git_repos/txt_phone/txt/script/draw_tri_planar_graphs.py.data/hand_draw-plantri-adc3m3-4d16d~sz306-png.zip


====
view ../../python3_src/c_external/plantri/readme.txt
  生成 平面图 ascii:4点 至 16点
view script/draw_tri_planar_graphs.py
  平面图 ascii -> 生成 平面图 dot/svg/png
  # 'script/draw_tri_planar_graphs.py.data/plantri-adc3m3-[4-16]d--dot-svg+script+data.7z'
  # /sdcard/0my_files/tmp/dot/plantri-adc3m3-[4-16]d--png/*.png
      # '/sdcard/0my_files/tmp/dot/plantri-adc3m3-[4-16]d--png/[0000000]4 bcd,adc,abd,acb.png'
view script/info_tri_planar_graphs.py
  平面图 ascii -> 生成 平面图 相关信息: 有向边同构等价类，点同构等价类，删一边后的子图同构等价类
  # script/info_tri_planar_graphs.py.data/info_tri_planar_graphs_4_16_ver2.7z
  view /sdcard/0my_files/tmp/info_tri_planar_graphs_4_16_ver2.txt
view script/pngs2blackwhite.py
  png二值化
  view others/app/termux/py_pip/purepng.txt


apk
  DroidVim @com.droidvim
    阅读 平面图 相关信息
    view /sdcard/0my_files/tmp/info_tri_planar_graphs_4_16_ver2.txt
  快图浏览 @com.alensw.PicFolder
    浏览 平面图 png: 由dot生成的直线风格 平面图png
    # /sdcard/0my_files/tmp/dot/plantri-adc3m3-[4-16]d--png/*.png
  Paint Pro / Paint @com.electricsheep.paintpro
    手动画图:平面图 的 临时 草图
  Pixly @com.meltinglogic.pixly
    手动画图:平面图 的 点阵图/像素图

步骤:
  平面图是否有 不平凡自同构？是否有 不动点（在所有自同构下）？
    <<==点同构等价类
  *没有 不平凡自同构
    选择 一个好识别的 删一边后的子图 为 底本（优先:好识别+三角形变点）
    快图浏览:本图 直线风格png，想象 删除对应边后的子图 与 底本 如何同构
    Pixly:在底本上添加一边

  *有 不平凡自同构 + 没有 不动点
    ？？必有 镜像边
      （镜像边=不平凡自同构边，即 有向边 与 自己的反向边 等价）
      ？？证明: 非空连通图若有不平凡自同构，则有全局不动点或有局部镜像边
      错！！
      反例:
        '[0000173]16 bcd,aef,afg,agh,bij,bjc,ckd,dlm,emn,eof,gpl,hkp,hni,imo,jnp,kol'
        '[0000253]16 bcd,aef,agh,aie,bdj,bkl,clm,cni,dho,epk,fjm,fmg,glk,hpo,inp,jon'
    但 大概率有镜像边，删除镜像边后仍对称的子图底本优先考虑
    如何快速定位 镜像边？
      每个图的相关信息 各占两行
      第二行 每个有向边同构等价类只以数值最小者代表
      如果 同一无向边的两条有向边同时出现在删边代表集里，则 不是 镜像边
      否则 很有可能是，也可能 另一方向的有向边的类的代表边 选了另一条
  *有 不平凡自同构 + 有 不动点
    三连通平面图只有以下两种自同构
    *旋转对称
      以某一对称中心不动点为中心起笔
    *镜像对称
      以通过不动点的虚拟对称轴为中心起笔
    Paint 画草图


png二值化
  由于实际操作中的种种原因，png白色真白，但黑色不黑，用python::purepng库 使png颜色 二值化
  由于 Pixly 不支持 bitdepth=1, 这里 只用 bitdepth=8
  由于 Pixly 将 greyscale=True 保存的图 读作 alpha 通道，这里 只用 greyscale=False




