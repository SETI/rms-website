$ set default [.source]
$
$ cc COLUMN/include=OAL:
$ cc LABEL/include=OAL:
$ cc ARRAY
$ cc BOXCAR
$ cc BUFFERED
$ cc COMPOSIT
$ cc CURVE
$ cc ERRORS
$ cc FILTERED
$ cc FIXED
$ cc FUNCTION
$ cc INVERSE
$ cc LSPLINE
$ cc OBJECT
$ cc PSFFILT
$ cc RESAMPLE
$ cc SERIES
$ cc SINC
$ cc SLOPE
$ cc SOFTWARE
$ cc SPLINE
$ cc STAT
$ cc TRIANGLE
$ cc WEIGHTED
$ cc FORTRAN
$ cc RLERRORS
$ cc RLMEMORY
$
$ fortran FPROFILE/separate
$ fortran FRINGLIB/separate
$ fortran FSTRINGS/separate
$
$ library/create [-]PROFILE *
$ library/compress [-]PROFILE
$ purge [-]PROFILE.OLB
$
$ delete/noconfirm *.OBJ;*
$
$ cc/define=QUICK COLUMN/include=OAL:
$ cc/define=QUICK LABEL/include=OAL:
$ cc/define=QUICK ARRAY
$ cc/define=QUICK BOXCAR
$ cc/define=QUICK BUFFERED
$ cc/define=QUICK COMPOSIT
$ cc/define=QUICK CURVE
$ cc/define=QUICK ERRORS
$ cc/define=QUICK FILTERED
$ cc/define=QUICK FIXED
$ cc/define=QUICK FUNCTION
$ cc/define=QUICK INVERSE
$ cc/define=QUICK LSPLINE
$ cc/define=QUICK OBJECT
$ cc/define=QUICK PSFFILT
$ cc/define=QUICK RESAMPLE
$ cc/define=QUICK SERIES
$ cc/define=QUICK SINC
$ cc/define=QUICK SLOPE
$ cc/define=QUICK SOFTWARE
$ cc/define=QUICK SPLINE
$ cc/define=QUICK STAT
$ cc/define=QUICK TRIANGLE
$ cc/define=QUICK WEIGHTED
$ cc/define=QUICK FORTRAN
$ cc/define=QUICK RLERRORS
$ cc/define=QUICK RLMEMORY
$
$ fortran FPROFILE/separate
$ fortran FRINGLIB/separate
$ fortran FSTRINGS/separate
$
$ library/create [-]QPROFILE *
$ library/compress [-]QPROFILE
$ purge [-]QPROFILE.OLB
$
$ delete/noconfirm *.OBJ;*/nolog
$
$ set default [-.EXAMPLES]
$
$ fortran PPSFILT
$ link PPSFILT, [-]QPROFILE/lib, OAL:OAL/lib, SYS$LIBRARY:VAXCRTL/lib
$
$ fortran PPSRESAM
$ link PPSRESAM, [-]QPROFILE/lib, OAL:OAL/lib, SYS$LIBRARY:VAXCRTL/lib
$
$ delete/noconfirm *.OBJ;*/nolog
$
$ set default [-]
