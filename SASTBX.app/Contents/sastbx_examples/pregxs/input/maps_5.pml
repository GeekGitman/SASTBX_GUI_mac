set bg_rgb,[1,1,1]
load querym5_3D0W.ccp4, map1
isomesh m1,map1,0.0883250907835
color blue, m1
png maps_5_view1
turn x, 90
png maps_5_view2
turn x,-90
turn y,90
png maps_5_view3
