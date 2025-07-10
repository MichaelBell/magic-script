load combined.mag
flatten tt_um_flat
load tt_um_flat
select top cell
extract all
ext2sim labels on
ext2sim
extresist tolerance 1
extresist
ext2spice lvs
ext2spice cthresh 0 ; # values below 1.7 cause floating nodes (singular matrix in spice)
ext2spice extresist on
ext2spice
quit -noprompt
