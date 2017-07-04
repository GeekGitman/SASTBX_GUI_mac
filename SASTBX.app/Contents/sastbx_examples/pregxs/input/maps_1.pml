set bg_rgb,[1,1,1]
load querym1_3IBM.ccp4, map1
isomesh m1,map1,0.0867656778411
color blue, m1
png maps_1_view1
turn x, 90
png maps_1_view2
turn x,-90
turn y,90
png maps_1_view3
