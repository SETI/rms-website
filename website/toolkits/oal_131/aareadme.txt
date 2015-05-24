PDS_VERSION_ID                  = PDS3
RECORD_TYPE                     = STREAM

OBJECT                          = TEXT
  PUBLICATION_DATE              = 2003-09-24
  NOTE                          = "General overview of this archived
version of the PDS Object Access Library 1.3.1."
END_OBJECT                      = TEXT
END

                      PDS OBJECT ACCESS LIBRARY 1.3.1
                           PDS ARCHIVE VERSION

                            Mark R. Showalter
                             PDS Rings Node
                             September 2003

This is a version of the PDS Object Access Library (OAL) 1.3 which has
been modified to work seamlessly with the Profile Library of the PDS
Rings Node.

Note that this is NOT the most up-to-date version of the Object Access
Library. For that latest version, consult the software download page at the
PDS Central Node, http://pds.jpl.nasa.govtools/software_download.cfm.

The following changes have been applied:

(a) Files have been renamed to comply with PDS archiving conventions.
Specifically, files names have been converted to old PDS "8.3" file
naming conventions. Also, a brief PDS label has been provided for
every file. This makes the directory tree suitable for including on
any PDS archive volume.

(b) The source has been adapted to build on Macintosh OS X.

(c) Several source modules have been modified to suppress an
unnecessary warning message. This is needed for the library to work
suitably with the Profile Toolkit of the PDS Rings Node.

(d) This brief overview file has been added.

FILES

This directory tree originated in the PDS archive distribution of
Object Access Library 1.3, found on line at:
    ftp://starhawk.jpl.nasa.gov/tools/other_tools/SunOS/source/oal/
in compressed Unix tar file "oalV13.tar.Z". The tar file contains all
of the files in this OAL directory tree.

This root directory contains a variety of documentation files and four
subdirectories:
    examples/ - example files.
    fortran/  - interface routines so the toolkit can be called from
                programs written in FORTRAN-77.
    idl/      - nterface routines so the toolkit can be called from
                programs written in IDL.
    source/   - the C source code and build scripts.

Each subdirectory now contains a single combined-detached label file
"xxx.lbl", where "xxx" is replaced by the name of the subdirectory.
This label describes (briefly) all the other files in the subdirectory
(except those that have their own labels). In the cases where files
have been renamed, the label indicates the original file name.

In cases where we have modified the contents of a file, the original
file is included with a "1" appended to the name. The only modified
files are in the "source/" subdirectory.

UNIX BUILD INSTRUCTIONS

(1) In the source subdirectory, edit the file "makefile.mak" to
include the appropriate definition file "*.def" for the given
operating system. The choices are:

    Sun Sparc/SunOS and Solaris: sunnonans.def or sunsparc.def
    Silicon Graphics/Irix:       sgiiris.def
    Dec 3100/Ultrix:             decultrx.def
    Dec Alpha/OSF:               decalpha.def
    Mac OS X:                    macosx.def

(2) If the library has already been built, delete the file "oal.a".

(3) Execute the make file by typing:
    make -f makefile.mak

This will build the library file "oal.a" and also two test programs
"t_images.exe" and "t_tables.exe".

This procedure does not build the FORTRAN or IDL interface routines.
Consult the User's Guide for more information.

USAGE

To link another program with the library, include "oal.a" in the
list of files passed to the compiler. Also include "oal.h" in
each file tha calls OA Library routines. Both of these files are
found in the "source/" subdirectory.

