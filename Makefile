NAME ?= ha

all: sim

%.mag: %.py magic.py
	python $<

magic: $(NAME).mag
	# PDK_ROOT env var must be set correctly for this to work
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $(NAME).mag
	# now in the command window type:
	# extract
	# ext2spice lvs
	# ext2spice cthresh 0
	# ext2spice

combined: combined.mag ha.mag ha_flip.mag
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc combined.mag

tt_um_flat.spice: combined.mag ha.mag ha_flip.mag
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc -noconsole -dnull ext2spice.tcl

simulation.spice: pre.spice tt_um_flat.spice post.spice
    # magic puts subckt and end around extract, so remove it
	echo ".lib '$(PDK_ROOT)/sky130A/libs.tech/ngspice/sky130.lib.spice' tt" > pdk_lib.spice
	#sed -i -e 's/.ends//' tt_um_flat.spice
	#sed -i -e 's/.subckt tt_um_flat//' tt_um_flat.spice
	# build a simulation with pre and post.spice
	cat $^ > $@

sim: simulation.spice
	# run the simulation
	ngspice $^

clean:
	rm -f $(NAME).spice model.spice $(NAME).ext

phony: clean
