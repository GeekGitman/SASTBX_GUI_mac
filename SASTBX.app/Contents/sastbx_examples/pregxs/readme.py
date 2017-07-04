sastbx.pregxs data=saxs.dat d_max=50

data和d_max是必须的参数
其中：data的格式是：q i sigma三列
d_max: Maximum distance in particle

可选参数：
scan=True/False 默认为false When True, a dmax scan will be performed
output=output_prefix 默认为：
pregxsbest.qii和pregxsbest.pr 位置与输入的data处于相同文件夹下
data.json和qii.json与输入文件saxs.dat处于相同的文件夹下面

例子：
sastbx.pregxs data=saxs.dat d_max=50 output=/Users/Song/Desktop/pregxs
则 
pregxsbest.qii和pregxsbest.pr位置在/Users/Song/Desktop/下面
data.json和qii.json与输入文件saxs.dat处于相同的文件夹下面
======================================================
更改 sastbx/source/sastbx/pr/pregxs.py
重新定向data.json和qii.json的输出位置:
131,132,138,139
"data.json"加了前缀：params.pregxs.output 
write_pr_json(params.pregxs.output+"data.json", scanner.r, scanner.average_pr)


sastbx.pregxs data=saxs.dat d_max=50 scan=False output=/Desktop/pregxs/pregxs
result:
=============
pregxsbest.pr
pregxsbest.qii 
pregxsdata.json
pregxsqii.json

sastbx.pregxs data=saxs.dat d_max=50 scan=True output=/Desktop/pregxs/pregxs
result:
=================
pregxsaverage.pr
pregxsdata.json
pregxsqii.json
