$ library/create kepler
$
$ cc KEP_5FREQ
$ cc KEP_COMBO
$ cc KEP_KAPPA
$ cc KEP_LOCATE
$ cc KEP_MEANANOM
$ cc KEP_NU
$ cc KEP_OMEGA
$ cc KEP_PRECESS
$ cc KEP_SETERROR
$ cc KEP_SETORBIT
$ cc KEP_SETPLANET
$ cc KEP_SOLVEA
$ cc KEP_TRUEANOM
$ library/insert kepler kep_*
$ delete/noconfirm/nolog kep_*.obj;*
$
$ cc XKEP_JSERIES
$ cc XKEP_MEANANOM
$ cc XKEP_TRUEANOM
$ library/insert kepler xkep_*
$ delete/noconfirm/nolog xkep_*.obj;*
$
$ cc FKEP_5FREQ
$ cc FKEP_APSE
$ cc FKEP_COMBO
$ cc FKEP_KAPPA
$ cc FKEP_LOCATE
$ cc FKEP_MEANANOM
$ cc FKEP_NODE
$ cc FKEP_NU
$ cc FKEP_OMEGA
$ cc FKEP_PRECESS
$ cc FKEP_SETERROR
$ cc FKEP_SETORBIT
$ cc FKEP_SETPLANET
$ cc FKEP_SOLVEA
$ cc FKEP_TRUEANOM
$ library/insert kepler fkep_*
$ delete/noconfirm/nolog fkep_*.obj;*
$
$ library/compress=blocks:30 kepler
$ purge kepler.olb
$
$ fortran orbit.for
$ link orbit,kepler/library
$ delete/noconfirm/nolog orbit.obj;*
$
$ fortran solver.for
$ link solver,kepler/library
$ delete/noconfirm/nolog solver.obj;*
$
$ fortran table3.for
$ link table3,kepler/library
$ delete/noconfirm/nolog table3.obj;*
