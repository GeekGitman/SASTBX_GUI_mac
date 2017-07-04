set bg_rgb,[1,1,1]
load querym2_1MFT.ccp4, map1
isomesh m1,map1,0.0910810630522
color blue, m1
png maps_2_view1
turn x, 90
png maps_2_view2
turn x,-90
turn y,90
png maps_2_view3
