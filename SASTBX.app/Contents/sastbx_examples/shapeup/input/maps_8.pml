set bg_rgb,[1,1,1]
load /Users/Song/sastbx/gui/sasqt/sastbx_examples/shapeup/output/bio32m8_1B33.ccp4, map1
isomesh m1,map1,0.0835381346552
color blue, m1
png maps_8_view1
turn x, 90
png maps_8_view2
turn x,-90
turn y,90
png maps_8_view3
