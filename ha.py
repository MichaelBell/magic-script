from magic import *

mag = MagicCell(120, -185, 360, 0)

spacing = 100

a_contact = Rect(85, -41, 30, 17)
mag.make_cmos(25, a_contact, li_rect=Rect(82, -49, 36, 33))

mag.ndiffc.append(Rect(0, -115, 17, 40))  # -
mag.locali.append(Rect(0, -125, 17, 60))
mag.viali.append(Rect(0, -115, 17, 40))
mag.metal1.append(Rect(-3, -121, 83, 52))

mag.ndiffc.append(Rect(48, -110, 17, 40)) # ~A

mag.pdiffc.append(Rect(0, 20, 17, 60))    # +
mag.locali.append(Rect(0, 10, 17, 80))
mag.viali.append(Rect(0, 20, 17, 60))
mag.metal1.append(Rect(-3, 14, 23, 72))

mag.pdiffc.append(Rect(48, 20, 17, 60))   # ~A

mag.locali.append(Rect(48, -120, 17, 210))

mag.poly.append(Rect(40, -51, spacing-15, 37))
mag.viali.append(Rect(82, -41, 17, 17))
mag.metal1.append(Rect(55, -47, 47, 29))
mag.metal1.append(Rect(55, -47, 20, 167))

mag.make_cmos(25+spacing, None)

mag.ndiffc.append(Rect(0+spacing, -110, 17, 30))   # B
mag.locali.append(Rect(0+spacing, -120, 17, 50))
mag.viali.append(Rect(0+spacing, -110, 17, 30))
mag.metal1.append(Rect(0+spacing-3, -120, 23, 58))
mag.ndiffc.append(Rect(48+spacing, -110, 17, 20))  # Co
mag.locali.append(Rect(48+spacing, -120, 17, 40))
mag.viali.append(Rect(48+spacing, -120, 17, 20))
mag.metal1.append(Rect(45+spacing, -126, 23, 32))

mag.pdiffc.append(Rect(0+spacing, 50, 17, 30))     # B
mag.locali.append(Rect(0+spacing, 40, 17, 50))
mag.viali.append(Rect(0+spacing, 40, 17, 30))
mag.metal1.append(Rect(0+spacing-3, 0, 23, 80))
mag.pdiffc.append(Rect(48+spacing, 50, 17, 30))    # S
mag.locali.append(Rect(48+spacing, 40, 17, 50))
mag.viali.append(Rect(48+spacing, 50, 17, 30))
mag.metal1.append(Rect(45+spacing, 44, 23, 42))

mag.metal1.append(Rect(116, -80, 17, 112))  # B
mag.metal1.append(Rect(147, -120, 21, 120)) # Co

mag.locali.append(Rect(65, 1, 110, 17)) # ~A
mag.locali.append(Rect(158, -49, 17, 50))
mag.polycont.append(Rect(185, -41, 30, 17))
mag.locali.append(Rect(175, -49, 50, 33))

mag.poly.append(Rect(173, -145, 15, 131))
mag.nmos.append(Rect(173, -125, 15, 65))
mag.ndiff.append(Rect(173-29, -125, 73, 65))

mag.ndiffc.append(Rect(23+173, -115, 17, 35))  # -
mag.locali.append(Rect(23+173, -125, 17, 55))
mag.viali.append(Rect(23+173, -115, 17, 35))
mag.metal1.append(Rect(20+173, -121, 26, 47))

mag.poly.append(Rect(173+15, -51, spacing-15, 37))

mag.poly.append(Rect(273, -145, 15, 131))
mag.nmos.append(Rect(273, -125, 15, 65))
mag.ndiff.append(Rect(273-29, -125, 73, 65))

mag.ndiffc.append(Rect(273-25, -110, 17, 30))   # B
mag.locali.append(Rect(273-25, -120, 17, 50))
mag.viali.append(Rect(273-25, -110, 17, 30))
mag.metal1.append(Rect(273-28, -120, 26, 190))

mag.poly.append(Rect(225, -15, 15, 130))
mag.pmos.append(Rect(225, 0, 15, 100))    # B
mag.pdiff.append(Rect(225-29, 0, 73, 100))

mag.pdiffc.append(Rect(0+200, 20, 17, 60))     # Co
mag.locali.append(Rect(0+200, 10, 17, 80))
mag.viali.append(Rect(0+200, 20, 17, 40))
mag.metal1.append(Rect(0+200-3, 0, 23, 70))
mag.pdiffc.append(Rect(48+200, 20, 17, 60))    # B
mag.locali.append(Rect(48+200, -15, 17, 105))
mag.viali.append(Rect(48+200, 20, 17, 40))

mag.metal1.append(Rect(168, -20, 52, 20)) # Co

mag.make_cmos(325, Rect(335, -41, 17, 17), li_rect=Rect(325, -44, 37, 23))

mag.locali.append(Rect(265, -15, 77, 17)) # B
mag.locali.append(Rect(325, -21, 17, 6))

mag.ndiffc.append(Rect(298, -120, 19, 17))   # S
mag.locali.append(Rect(298, -128, 19, 30))
mag.viali.append(Rect(298, -120, 19, 25))
mag.metal1.append(Rect(295, -126, 25, 211))

mag.pdiffc.append(Rect(300, 50, 17, 30))    # S
mag.locali.append(Rect(298, 40, 19, 50))
mag.viali.append(Rect(298, 50, 19, 30))

mag.metal1.append(Rect(145, 85, 175, 20)) # S

mag.locali.append(Rect(225, -49, 83, 17))  # ~A

mag.ndiffc.append(Rect(348, -110, 17, 30))   # ~A
mag.locali.append(Rect(348, -120, 17, 59))
mag.locali.append(Rect(291, -61, 17, 12))
mag.locali.append(Rect(291, -78, 65, 17))


mag.pdiffc.append(Rect(348, 50, 17, 30))    # A
mag.locali.append(Rect(348, 40, 17, 50))
mag.viali.append(Rect(348, 50, 17, 30))
mag.metal1.append(Rect(345, 44, 23, 76))

mag.metal1.append(Rect(55, 120, 313, 15))  # A

mag.via1.append(Rect(97, 6, 26, 26))     # B
mag.metal2.append(Rect(97, 0, 174, 38))
mag.via1.append(Rect(245, 6, 26, 26))

mag.via1.append(Rect(50, -115, 26, 30))  # -
mag.metal2.append(Rect(50, -125, 169, 50))
mag.via1.append(Rect(193, -115, 26, 30))

mag.labels.append(Label("metal1", Rect(55, 120, 313, 15), "A"))
mag.labels.append(Label("metal2", Rect(97, 0, 174, 38), "B"))
mag.labels.append(Label("metal1", Rect(295, -126, 25, 211), "S"))
mag.labels.append(Label("metal1", Rect(147, -120, 21, 120), "C"))
mag.labels.append(Label("metal1", Rect(-3, 14, 23, 72), "VPWR"))
mag.labels.append(Label("metal2", Rect(50, -125, 169, 50), "VGND"))

with open("ha.mag", "w") as f:
    mag.write(f)
