$!******************************************************************************
$! This VMS command file builds the Julian object library JULIAN.OLB and the
$! sample program TCONVERT.EXE.  Further information can be found in the file
$! AAREADME.TXT.
$!
$! Mark Showalter, PDS Rings Node, December 1995
$! Revised 6/98 by MRS to conform to RingLib naming conventions.
$!******************************************************************************
$
$!******************************************************************************
$! Compile Julian Library routines written in C
$!******************************************************************************
$
$ cc DATES.C
$ cc FORMAT.C
$ cc JULDATES.C
$ cc LEAPSECS.C
$ cc PARSE.C
$ cc SECONDS.C
$ cc TAI_ET.C
$ cc UTC_TAI.C
$
$!******************************************************************************
$! Compile Julian Library routines written in FORTRAN
$!******************************************************************************
$
$ fortran FJULIAN.FOR/separate_compilation
$
$!******************************************************************************
$! Compile RingLib routines
$!******************************************************************************
$
$ cc FORTRAN.C
$ cc RLERRORS.C
$ cc RLMEMORY.C
$ fortran FSTRINGS.FOR/separate_compilation
$
$!******************************************************************************
$! Create library
$!******************************************************************************
$
$ library/create JULIAN
$ library/insert JULIAN *.OBJ
$ library/compress=blocks:30 JULIAN
$ purge JULIAN.OLB
$
$!******************************************************************************
$! Build TCONVERT program
$!******************************************************************************
$
$ fortran TCONVERT
$ link TCONVERT,JULIAN/library,SYS$LIBRARY:VAXCRTL/library
$
$!******************************************************************************
$! Delete object files
$!******************************************************************************
$
$ delete/noconfirm/nolog *.OBJ;*
