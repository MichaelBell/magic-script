from magic import *

mag = MagicCell(120, -220, 310)

a_contact = Rect(20, -60, 20, 30)
mag.make_cmos(50, a_contact)

mag.ndiffc.append(Rect(22, -150, 20, 40))
mag.locali.append(Rect(12, -190, 38, 90))
mag.ndiffc.append(Rect(73, -150, 20, 40))

mag.pdiffc.append(Rect(23, 50, 20, 40))
mag.locali.append(Rect(12, 40, 38, 80))
mag.pdiffc.append(Rect(73, 50, 20, 40))

mag.locali.append(Rect(68, -160, 35, 260))

na_contact = Rect(120, -75, 30, 20)
mag.make_cmos(160, na_contact)
mag.locali.append(Rect(100, -85, 20, 40))

mag.ndiffc.append(Rect(132, -150, 20, 40))
mag.locali.append(Rect(122, -190, 38, 85))
mag.ndiffc.append(Rect(183, -150, 20, 40))
mag.locali.append(Rect(178, -160, 30, 170))

mag.pdiffc.append(Rect(132, 50, 20, 40))
mag.locali.append(Rect(127, -25, 30, 125))
mag.pdiffc.append(Rect(183, 50, 20, 40))
mag.locali.append(Rect(175, 40, 125, 60))
mag.locali.append(Rect(157, -25, 21, 35))

t3_x = 210
mag.poly.append(Rect(t3_x, mag.poly_min, 15, 160))
a_contn = Rect(t3_x+15, -60, 20, 30)
mag.poly.append(a_contn.expanded_by(10))
mag.polycont.append(a_contn)
mag.locali.append(Rect(t3_x+15, -70, 30, 50))
mag.nmos.append(Rect(t3_x, mag.poly_min+20, 15, mag.nmos_h))
mag.ndiff.append(Rect(t3_x-32, mag.poly_min+20, 79, mag.nmos_h))

mag.ndiffc.append(Rect(t3_x+23, -150, 20, 40))
mag.locali.append(Rect(t3_x+15, -160, 50, 60))
mag.locali.append(Rect(275, -160, 25, 260))


mag.viali.append(a_contact)
mag.viali.append(a_contn)
mag.metal1.append(Rect(10, -70, 245, 50))
mag.labels.append(Label("metal1", a_contact.expanded_by(10), "A"))
mag.labels.append(Label("locali", Rect(175, 40, 125, 60), "B"))
mag.labels.append(Label("locali", Rect(178, -160, 30, 60), "X"))

with open("and.mag", "w") as f:
    mag.write(f)
