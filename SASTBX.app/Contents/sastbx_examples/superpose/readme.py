sastbx.superpose fix=fixed_file typef=type [pdb | nlm | map ] mov=moving_file typem=type nmax=nmax
四项都是必须的输入项
输入：Desktop/a.pdb,/Documents/b.pdb
输出：Desktop/a_za.nlm,Desktop/a_za.pdb, 
	Documents/b_za.nlm,Documents/b_za.pdb

输入：Desktop/a.pdb /Documents/b.nlm
输出：Desktop/a_za.nlm,Desktop/a_za.pdb, 
     Documents/b_za.nlm
namx有默认值：20
===============================================
默认在与输入相同的文件夹中。
更改为到指定输出：
sastbx.superpose: sastbx.python sastbx/source/sastbx/zernike_model/zalign.py
不太好改：
在gui里面：
在获取输入的时候就可以获取文件夹，然后从该文件里面移动输入到目的文件夹中。
=============================
20170522
在/sastbx/source/sastbx/zernike_model/zalign.py
中修改了输出文件

map:xplor
