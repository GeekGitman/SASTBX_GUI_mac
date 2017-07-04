set bg_rgb,[1,1,1]
load querym3_2C1L.ccp4, map1
isomesh m1,map1,0.0916108560852
color blue, m1
png maps_3_view1
turn x, 90
png maps_3_view2
turn x,-90
turn y,90
png maps_3_view3
