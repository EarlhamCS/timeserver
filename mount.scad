devL = 58;
devW = 49;
devH = 20;
mntL = 72;
mntW = (mntL / devL) * devW; //55;
mntH = 115;

zeroL = 0.25;
oneL = 0.50;
twoL = 0.75;

oneRate = 0.3;
twoRate = 0.1;

rotate ([180,0,0]) difference () {
    union () { 
         color("blue") { cube([mntL, mntW, mntH]); }
         translate ([0.5 * mntL, 0.5 * mntW, 0.5 * mntH]) { sphere(r=devW) ; }
    }
    translate ([0.5 * (mntL - devL),
                0.5 * (mntW - devW),
			   0]) {  cube([devL, devW, devH]) ;}
}
