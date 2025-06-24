import time

class Rect:
    def __init__(self, x, y, w=0, h=0):
        self.x = x
        self.y = y
        self.tx = x + w
        self.ty = y + h

    def expanded_by(self, amount):
        r = Rect(self.x - amount, self.y - amount)
        r.tx = self.tx + amount
        r.ty = self.ty + amount
        return r

class Label:
    def __init__(self, layer, r, name):
        self.layer = layer
        self.r = r
        self.name = name

class MagicCell:
    def __init__(self, pwr_y, gnd_y, width, spacing=90):
        self.nwell = []
        self.nmos = []
        self.pmos = []
        self.ndiff = []
        self.pdiff = []
        self.ndiffc = []
        self.pdiffc = []
        self.poly = []
        self.polycont = []
        self.locali = []
        self.viali = []
        self.metal1 = []
        self.labels = []

        self.metal1.append(Rect(-30, pwr_y-20, width+60, 70))
        self.metal1.append(Rect(-30, gnd_y-20, width+60, 70))
        self.locali.append(Rect(0, pwr_y, width, 30))
        self.locali.append(Rect(0, gnd_y, width, 30))
        for x in range(0, width, spacing):
            self.viali.append(Rect(x, pwr_y, 30, 30))
            self.viali.append(Rect(x, gnd_y, 30, 30))
        self.labels.append(Label("metal1", Rect(0, pwr_y, width, 30), "VPWR"))
        self.labels.append(Label("metal1", Rect(0, gnd_y, width, 30), "VGND"))

        self.poly_min = gnd_y + 40
        self.nmos_h = 65
        self.pmos_h = 100 # Pmos y = 0
        self.poly_h = pwr_y - 5 - self.poly_min

        nwell_r = Rect(-30, -20, width+60, pwr_y+40)
        self.nwell.append(nwell_r)
        self.labels.append(Label("nwell", nwell_r, "NWELL"))

    def write(self, file):
        def fprint(s):
            print(s, file=file)
        def fprint_rects(rects):
            for r in rects:
                fprint(f"rect {r.x} {r.y} {r.tx} {r.ty}")

        fprint("magic")
        fprint("tech sky130A")
        fprint(f"timestamp {int(time.time())}")
        fprint("<< nwell >>")
        fprint_rects(self.nwell)
        fprint("<< nmos >>")
        fprint_rects(self.nmos)
        fprint("<< pmos >>")
        fprint_rects(self.pmos)
        fprint("<< ndiff >>")
        fprint_rects(self.ndiff)
        fprint("<< pdiff >>")
        fprint_rects(self.pdiff)
        fprint("<< ndiffc >>")
        fprint_rects(self.ndiffc)
        fprint("<< pdiffc >>")
        fprint_rects(self.pdiffc)
        fprint("<< poly >>")
        fprint_rects(self.poly)
        fprint("<< polycont >>")
        fprint_rects(self.polycont)
        fprint("<< locali >>")
        fprint_rects(self.locali)
        fprint("<< viali >>")
        fprint_rects(self.viali)
        fprint("<< metal1 >>")
        fprint_rects(self.metal1)

        fprint("<< labels >>")
        for l in self.labels:
            fprint(f"rlabel {l.layer} {l.r.x} {l.r.y} {l.r.tx} {l.r.ty} 1 {l.name}")
        fprint("<< name >>")

    def make_cmos(self, x, contact_rect, add_pdiff=True, add_ndiff=True):
        self.poly.append(Rect(x, self.poly_min, 15, self.poly_h))
        self.poly.append(contact_rect.expanded_by(10))
        self.polycont.append(contact_rect)
        self.locali.append(contact_rect.expanded_by(10))
        self.nmos.append(Rect(x, self.poly_min+20, 15, self.nmos_h))
        self.pmos.append(Rect(x, 0, 15, self.pmos_h))
        if add_pdiff:
            self.pdiff.append(Rect(x-50, 0, 115, self.pmos_h))
        if add_ndiff:
            self.ndiff.append(Rect(x-50, self.poly_min+20, 115, self.nmos_h))

if __name__ == "__main__":
    mag = MagicCell(120, -220, 240)
    a_contact = Rect(20, -60, 30, 20)
    b_contact = Rect(160, -60, 30, 20)
    mag.make_cmos(60, a_contact)
    mag.make_cmos(140, b_contact)
    mag.labels.append(Label("locali", a_contact.expanded_by(10), "A"))
    mag.labels.append(Label("locali", b_contact.expanded_by(10), "B"))

    mag.ndiffc.append(Rect(20, -150, 20, 40))
    mag.locali.append(Rect(10, -190, 40, 90))
    mag.ndiffc.append(Rect(100, -150, 20, 40))
    mag.ndiffc.append(Rect(180, -150, 20, 40))
    mag.locali.append(Rect(170, -190, 40, 90))

    mag.pdiffc.append(Rect(20, 50, 20, 40))
    mag.locali.append(Rect(10, 40, 40, 80))
    mag.pdiffc.append(Rect(180, 50, 20, 40))

    mag.locali.append(Rect(90, -160, 40, 260))
    mag.locali.append(Rect(130, 40, 120, 60))
    mag.labels.append(Label("locali", Rect(130, 40, 120, 60), "X"))

    with open("nor.mag", "w") as f:
        mag.write(f)


