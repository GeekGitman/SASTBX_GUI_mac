set bg_rgb,[1,1,1]
load querym6_2ZNL.ccp4, map1
isomesh m1,map1,0.094458497413
color blue, m1
png maps_6_view1
turn x, 90
png maps_6_view2
turn x,-90
turn y,90
png maps_6_view3
