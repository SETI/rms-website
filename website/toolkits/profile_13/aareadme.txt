PDS_VERSION_ID                  = PDS3
RECORD_TYPE                     = STREAM

OBJECT                          = TEXT
  PUBLICATION_DATE              = 2003-09-24
  NOTE                          = "AAREADME file containing a complete
overview of the PDS Rings Node's Profile Library, version 1.3."
END_OBJECT                      = TEXT
END

**********************************************************************
                    PDS Rings Node Software Library
                      Part 3: THE PROFILE LIBRARY
                      Version 1.3, September 2003

                           Mark R. Showalter

**********************************************************************

        TABLE OF CONTENTS

        1. INTRODUCTION
        1.1 Change History
        1.2 File Overview

        2. SUMMARY OF ROUTINES
        2.1 Objects
        2.2 Series
        2.3 Statistical series
        2.4 Functions
        2.5 Curves
        2.6 Point Spread Functions and Filters
        2.7 Labels
        2.8 RingLib Error Handling Routines
        2.9 Other Source Files

        3. EXAMPLES
        3.1 Program "ppsfilt.for"
        3.2 Program "ppsresam.for"

        4. USAGE

        5. BUILDING INSTRUCTIONS
        5.1 General Information
        5.2 Object Access Library
        5.3 UNIX Build Instructions
        5.4 VMS Build Instructions

1. INTRODUCTION

The Profile Toolkit comprises a set of C and FORTRAN routines for
manipulating ring profiles. The word profile is used here to describe
any sequence of numbers tabulated as a function of time, radius or any
other independent variable.

The toolkit includes routines for reading and manipulating
PDS-formatted data files, including the filtering and resampling of
data onto new sample grids. The routines keep track of the
relationships between profiles, enabling the user to understand the
statistical properties of derived data if the properties of the
original data are known. The toolkit also includes routines for
fitting curves to tabulated numbers, for the smooth interpolation of
geometric or calibration quantities associated with a data file.

The toolkit is designed using the principles of object-oriented
programming. The user freely creates objects by describing their
properties and relationships, without worrying about the details of
how they are implemented. This makes it possible to build extremely
sophisticated tools very easily.

1.1 Change History

VERSION 1.0

The original version was released in May 1998.

VERSION 1.1

Version 1.1 was released in January 2000. It contains a number of
relatively minor additions and changes.

First, the toolkit now includes a "Quick Mode" compile option that
eliminates much internal checking and can speed up performance
considerably. It is recommended that users always test their programs
initially using Standard Mode, and only rebuild using Quick Mode after
the software is fully debugged. Building instructions for both modes
are found in Section 5 below.

Second, the toolkit now includes a function Pro_StatRange() that
returns the range of samples in a statistical series that correlate
with a given series. This enables some resampling operations to run
much faster.

Third, the sample programs "ppsresam.for" and "ppsfilt.for" now print
commas between the columns of the data files they generate, yielding
files that are more compliant with PDS standards. Prior versions of
these programs are still included for comparison.

Finally, Version 1.1 includes a modified version of routine
"rprt_err.c", used by the PDS Object Access Library (OAL). This
routine suppresses unnecessary warning messages and should be used as
a replacement for the version distributed with OAL.

VERSION 1.2

Version 1.2 was released in September 2002. It corrects an error in
the way the sinc point spread function was used inside programs
PPSRESAM.FOR and PPSFILT.FOR.

It also provides a build script for Macintosh OS X, using GNU C and
the Absoft FORTRAN compiler.

VERSION 1.3

Version 1.3 was released in September 2003. It is substantially
reorganized for simpler distribution on a PDS archive volume.

It fixes a minor shortcoming of the example programs, in which the
incidence angle was read from the wrong file.

It also includes a modified version of routine "struct_l.c", used by
the PDS Object Access Library (OAL). This routine suppresses more
unnecessary warning messages and should be used as a replacement for
the version distributed with OAL.

1.2 File Overview

This release of the Rings Node Profile Library is organized as
follows:

    examples/    - A subdirectory containing sample programs and the
                   data files needed to run them. Use these programs
                   to confirm that the toolkit is working properly.

    oalsrc/      - A subdirectory containing replacement source code
                   for the PDS Object Access Library (OAL) 1.3. These
                   files should replace those of the same name in the
                   "source/" subdirectory of that toolkit. Note that
                   the archived version of OAL 1.3, as found on PDS
                   Rings Node archive volumes, already contains these
                   changes.

    source/      - A subdirectory containing all the source files for
                   Profile Library 1.3.

    aareadme.txt - This file.

    *.h          - C header files needed for user-written programs
                   that link with the Profile Library. Note that
                   identical copies of these files are also found in
                   the "source/" subdirectory.

    *.inc        - FORTRAN include files needed for user-written
                   programs that link with the Profile Library. Note
                   that identical copies of these files are also found
                   in the "source/" subdirectory.

    make*.com    - Simple shell scripts for building the Profile
                   Library on Sun/SGI, Macintosh OS X, Digital Unix,
                   and VMS.

    profile.a    - After building the toolkit, this is the name of the
    profile.olb    object library (.a for Unix, .olb for VMS).

    qprofile.a   - After building the toolkit, this is the name of the
    qprofile.olb   "Quick Mode" version of the object library. See
                   below for more information about Quick Mode.

    profile.lbl  - A PDS "combined-detached" label for all of the
                   files in this directory (except this one), which
                   has an attached label.

2. SUMMARY OF ROUTINES

Each routine in the Profile Toolkit is documented extensively in the
source code. The source files should be consulted for a detailed
description of how to use each routine. They are all found in the
"source/" subdirectory.

The fundamental unit manipulated in the Profile Toolkit is an object.
Each object has a class or type. The classes obey a hierarchy, in
which each object class inherits the properties and behaviors of its
superclass, while adding new properties of its own. The basic
hierarchy of Profile object classes is as follows:

                    Object
           ___________|___________
          |           |           |
        Series     Function     Label
          |           |
         Stat       Curve

For C programmers, all the Profile Toolkit routines have names
beginning with "Pro_". Some more basic components of the Rings Node
Library have names beginning with "RL_". For FORTRAN programmers, the
routine names are the same except that they have an "F" prepended. In
some circumstances, the numbers and types of the arguments differ
slightly between FORTRAN and C versions.

2.1 Objects

At the highest level, all objects share the basic properties that they
can be named, printed, and deleted. They also have X- and
Y-coordinates.

Defined in file object.c:
Pro_FreeObject     frees an object when it is no longer needed.
Pro_PrintObject    prints a description of an object.
Pro_ObjectName     returns the name of an object or coordinate.
Pro_RenameObject   changes the name of an object or coordinate.
Pro_ObjectDomain   returns the domain (X-limits) of an object.
Pro_ObjectOverlap  determines the domain of overlap of multiple
                   objects.

2.2 Series

Series objects augment the generic object class with the property that
they can be visualized as an indexed sequence of numbers. They all
have the property that, if given an integer index, they return a
numeric value. A series can also return a flag indicating that a
specific sample is invalid or unknown.

In addition, all series objects have a sampling parameter. This is a
floating-point number that varies linearly with the index, such as the
time in seconds when a sample was acquired.

Defined in file series.c:
Pro_SeriesValue    returns the value of a sample given the index.
Pro_SeriesIndices  returns the range of valid indices.
Pro_SeriesSampling returns the range and interval for the series'
                   sampling parameter.
Pro_SeriesIndex    converts from sampling parameter to index.
Pro_SeriesXValue   converts from index to sampling parameter.
Pro_WindowSeries   creates a new series that is identical to another
                   except that it has a narrower range of valid
                   indices.

Two specific implementations of the series object are provided:

Defined in file array.c:
Pro_ArraySeries    creates a new series object that returns the sample
                   values provided by the user in an array.

Defined in file column.c:
Pro_ColumnSeries   creates a new series object using the values found
                   in a column of a table or series in a PDS-labeled
                   data file.

For PDS COLUMN objects with multiple ITEMs, the derived series can
include any single item from each column or, alternatively, all the
ITEMs under the assumption that the file is organized as multiple
samples per row.

2.3 Statistical series

A statistical series (often abbreviated "stat") extends the properties
of a series with a new routine that gives the covariance between any
pair of samples (or variance of any single sample).

Defined in file stat.c:
Pro_StatCovar      returns the covariance between two samples.
Pro_StatRange      returns the range of samples that correlate with a
                   given sample.

Several implementations of statistical series are supported, all of
which involve the use of another series object.

Defined in file fixed.c:
Pro_FixedStat      creates a stat series in which the sample values
                   match those of another series, while the
                   covariances are just a function of the distance
                   between samples.

Defined in file filtered.c:
Pro_FilteredStat   creates a stat series in which each sample is a
                   weighted sum of the nearby samples in another stat
                   series. The set of coefficients is fixed.

Defined in file resample.c:
Pro_ResampledStat  creates a stat series which resamples another stat
                   series onto a new sample grid. For example, the
                   user can take data sampled uniformly in time and
                   resample it uniformly in intercept radius on the
                   ring plane.
Pro_ResampledSize  returns the size of a buffer appropriate when
                   resampling a buffered statistical series.

Defined in file weighted.c:
Pro_WeightedStat   creates a stat series in which each sample is a
                   weighted sum of samples from another stat series.
                   The user must provide a general routine that
                   returns the set of coefficients on old series
                   samples that go into each new sample. This routine
                   has no FORTRAN equivalent.

2.4 Functions

A function object returns a floating-point number y given another
floating-point number x. The function works within a certain specified
domain; attempts to evaluate the function for x-values outside this
domain raise an error condition.

Defined in file function.c:
Pro_FuncValue      returns the value of y given x.
Pro_WindowFunc     creates a new function that is identical to another
                   except that it has a narrower domain.

Several implementations of the function object are provided:

Defined in file lspline.c:
Pro_LSplineFunc    creates a function which interpolates linearly
                   between the nearest samples of a series object.

Defined in file software.c:
Pro_SoftFunc       creates a function object that returns the value of
                   a C or FORTRAN function coded by the user.
Pro_SoftFunc1      creates a function object that performs a
                   calculation on the result of another function.
Pro_SoftFunc2      creates a function object that performs a
                   calculation on the results of two other functions.

Defined in file composit.c:
Pro_CompFunc       creates a function object that applies one function
                   object to the result of another function object,
                   i.e. y = f(g(x))

Defined in file slope.c:
Pro_SlopeFunc      creates a function that returns the slope of a
                   curve object. (See below).

2.5 Curves

Curve objects extend the behavior of functions by adding the property
that, at any location within the domain, the slope of the function can
also be computed and returned.

Curve objects are generally smooth and continuous. Because of this
property, curves are invertible, meaning that a routine is provided to
return the best value of x given y. For curve inversions, the user
must also specify the segment of the curve to be inverted. Segments
are numbered from one, starting at the lower endpoint of the domain
and separated by extrema and inflection points in the file, up to the
upper endpoint of the domain.

Pro_CurveValue     returns the y-value and, optionally, the slope at
                   x.
Pro_CurveInverse   returns the x-value within a specified segment such
                   the f(x) equals, as closely as possible, the given
                   value of y.
Pro_CurveSegments  returns the number of curve segments within the
                   domain.
Pro_CurveExtremum  returns the location x and value y of the endpoint
                   of an extremum.

Two specific curve implementations are provided:

Defined in file spline.c:
Pro_SplineCurve    creates a curve that uses cubic splines to
                   interpolate between samples tabulated in a series.

Defined in file inverse.c:
Pro_InverseCurve   creates a curve that inverts the behavior of a
                   curve by exchanging the x and y coordinates.

2.6 Point Spread Functions and Filters

The Profile Toolkit provides a few convenient routines to assist the
user in describing the statistical properties of series samples and in
determining filter coefficients.

A point spread function (abbreviated PSF) describes the sensitivity of
an individual series sample to a theoretical, infinitesimal feature in
the data, as a function of the distance between the sample's center
point and the feature. Three PSFs are currently supported: boxcar,
triangle and sinc.

A "boxcar" PSF has a constant value within a certain distance of the
origin, but is zero outside that domain. If it has unit width, this
means that a sample is uniformly sensitive to any point feature that
falls less than half-way to either adjacent sample, but completely
insensitive to features further away than that.

Defined in file boxcar.c:
Pro_BoxcarFunc     creates a boxcar PSF.
Pro_BoxcarInfo     returns the parameters of a boxcar PSF.

A "triangle" PSF has a peak value at the origin and decreases linearly
to zero in either direction. If it has a full width of two, this means
that a sample is most sensitive to a point feature falling at its
center, completely insensitive to features falling at the center of
its neighbors, and has linearly variable sensitivity between these
limits.

Defined in file triangle.c:
Pro_TriangleFunc   creates a triangle PSF.
Pro_TriangleInfo   returns the parameters of a triangle PSF.

A "sinc" PSF has sensitivity that varies as sin(pi*x)/(pi*x). This is
what one expects when a series contains infinitesimally local samples
of a function that contains no signal of spatial wavelength shorter
than twice the spacing between samples.

Defined in file sinc.c:
Pro_SincFunc       creates a sinc PSF.
Pro_SincInfo       returns the parameters of a sinc PSF.

In addition to the PSF routines, the Profile Toolkit includes a handy
routine for determining a set of filter coefficients. Filtering a
profile can be understood as converting the data from one PSF to
another.

Defined in file psffilt.c:
Pro_PSFFilter      returns the best set of filter coefficients to
                   convert from one PSF to another.

2.7 Labels

A label object is simply the Profile Toolkit's name for its internal
representation for the PDS label of a data file. A label object has
the property that the user is able to look up information about the
data file and use this information to read and manipulate the numbers
found. The Profile Toolkit only recognizes data objects identified as
a TABLE or a SERIES in a PDS label.

Note that a label object does not make use of the coordinate name and
domain properties of other Profile Toolkit objects such as series and
functions.

Defined in file label.c:
Pro_OpenLabel      opens a PDS label or data file and constructs a
                   label object.
Pro_LabelCount     returns the number of TABLEs and SERIES in a label,
                   the number of COLUMNs in a TABLE or SERIES, or the
                   number of ITEMs in a COLUMN.
Pro_LabelName      returns the name of a TABLE, SERIES or COLUMN.
Pro_LabelXName     returns the sampling parameter name of a TABLE or
                   SERIES.
Pro_LabelFind      finds a TABLE, SERIES or COLUMN based on its name.
Pro_LabelSampling  returns the sampling of a TABLE, SERIES or COLUMN.
Pro_LabelInt       returns the integer value of a keyword from the PDS
                   label.
Pro_LabelFloat     returns the floating-point value of a keyword from
                   the PDS label.
Pro_LabelString    returns the string value of a keyword from the PDS
                   label.

2.8 RingLib Error Handling Routines

In addition, the Profile Toolkit provides a general mechanism for
dealing with error conditions. Each routine raises one of a specific
set of error conditions when something goes wrong. Users have complete
control over what to do in response to any of these conditions. By
default, the program will print an error message and abort. However,
users can decide on a condition-by-condition whether to print, hide or
redirect the message, and whether to abort or continue the program
afterward.

RL_RaiseError      raises a particular error condition.
RL_PipeErrors      redirects error messages to a file or the terminal.
RL_TestError       tests the most recent error condition.
RL_ClearError      clears the most recent error condition.
RL_TestError1      tests for a particular error condition.
RL_ClearError1     clears a particular error condition.
RL_SetErrorType    defines what should happen when a particular error
                   condition gets raised.
RL_GetErrorType    returns information about what happens when a
                   particular error condition gets raised.

The error conditions raised are identified by character strings. The
complete set of error conditions raised by the Profile Toolkit is as
follows:

PRO_CLASS_ERROR         if one attempts to apply an operation to an
                        object of the wrong type.
PRO_COORD_MISMATCH      if coordinate names that should match do not.
PRO_DOMAIN_ERROR        if a number falls outside its allowed range.
PRO_EMPTY_DOMAIN        if the domain of an object is empty.
PRO_EVALUATION_FAILURE  if a quantity cannot be evaluated.
PRO_NOT_FOUND           if something cannot be found by name.
PRO_SETUP_FAILURE       if an object cannot be created.

Two other error conditions are raised by lower-level routines.

RL_MEMORY_ERROR         if needed memory cannot be allocated. Note:
                        it is very unwise to proceed after this error
                        occurs; results will be unpredictable.
FORTRAN_POINTER_ERROR   if an object pointer in a FORTRAN program is
                        not valid.

2.9 Other Source Files

The following files contain additional source code in the form of
routines that are generally not to be called directly by the user.
Files that are specific to the Profile Toolkit are as follows:

errors.c       Profile routines to construct standardized error
               messages.
fprofile.for   FORTRAN interfaces to Profile Toolkit routines that
               pass character strings as arguments.

In addition, these files contain generic RingLib routines.

rlmemory.c     RingLib routines to manage memory.
fortran.c      Ringlib routines to convert between FORTRAN integers
               and C pointers.
fortran.h      C header file for fortran.c.
ringlib.h      C header file for RingLib.
fringlib.for   FORTRAN interfaces to Ringlib routines that pass
               character strings as arguments.
fstrings.for   Ringlib routines to convert string representations
               between FORTRAN and C.

3. EXAMPLES

Two sample programs are provided with the toolkit, along with their
needed data files. They are found in the "examples/" subdirectory.

3.1 Program "ppsfilt.for"

This FORTRAN program illustrates the use of the data filtering
capabilities of the toolkit. It generates a smoothed, ASCII-formatted
data file containing a segment of the Voyager PPS data set, calibrated
and listed with its radial scale.

File "filtout.tab" contains the output from a sample run of the
program, using data files "ppsdata.dat", "ppsgeom.tab" and
"ppscalib.tab", also included. These are versions of the PDS-formatted
files containing the data, geometry and calibration information from
the Voyager PPS ring occultation experiment at Saturn, volume VG_2801.
Consult the source code for an explanation of how to regenerate this
file.

3.2 Program "ppsresam.for"

This FORTRAN program illustrates the use of the data resampling
capabilities of the toolkit. It generates a smoothed, ASCII-formatted
data file containing a segment of the Voyager PPS data set, calibrated
and listed with its radial scale. Unlike program "ppsfilt.for", this
program resamples the data onto a uniform radius grid. It is also
significantly slower.

File "resamout.tab" contains the output from a sample run of the
program, using data files "ppsdata.dat", "ppsgeom.tab" and
"ppscalib.tab", discussed above. Consult the source code for an
explanation of how to regenerate this file.

4. USAGE

The file "profile.h" should be included in all C programs using the
Profile Toolkit. This file declares prototypes for every routine in
the toolkit, and also defines a few useful types, symbols and
constants. All Profile objects should be declared of type PRO_OBJECT*.
The toolkit is built atop PDS's Object Access Library (OAL), which is
also needed when linking programs.

Within the Profile Toolkit and the remainder of the Rings Node
Software Library, special data types are defined to "hide" some
variations among implementations of C from one platform to the next.
These special data types are as follows:
    RL_INT4 = a four-byte signed integer.
    RL_BOOL = an integer taking on only values TRUE=1 and FALSE=0.
    RL_FLT4 = a single-precision (four-byte) floating point number.
    RL_FLT8 = a double-precision (eight-byte) floating point number.
    RL_CHAR = a one-byte character.
    RL_VOID = used in the context of "void *" as a pointer to a
              structure of arbitrary type.
These types are defined in the include file "ringlib.h", which is
included automatically by "profile.h".

For FORTRAN programmers, the file "fprofile.inc" is provided. It
declares the type of every function within the toolkit and also
defines some useful parameters. All object pointers should be declared
integer*4.

5. BUILDING INSTRUCTIONS

5.1 General Information

A single set of source files generates both the Standard Mode and
Quick Mode object files. The difference is that Quick Mode object code
is generated when the C macro "QUICK" is defined at the time of
compilation. The build scripts described below generate both versions
of the object libraries.

The difference is that when the library is compiled using "Quick"
Mode, the code performs less self-checking so it runs faster; see
Section 1.1 above. In general, user programs will not need to be
modified to execute in Quick Mode; all the user will have to do is
re-load the program with the "Quick" version of the Profile Library.

5.2 Object Access Library

Several components of the Profile Library make use of the Object
Access Library (OAL), distributed by the PDS Central Node. It can be
obtained from
    ftp://starhawk.jpl.nasa.gov/tools/other_tools/SunOS/source/oal/
in compressed Unix tar file oalV13.tar.Z. In spite of the directory
name, the library builds successfully on many different platforms
under multiple operating systems. Follow the instructions provided
with that library.

However, when building OAL, it is recommended that you replace the
files "source/rprt_err.c" and "source/struct_l.c" with the versions
found in the "oalsrc/" subdirectory accompanying this library. These
revised versions suppress a large number of warnings and
informational messages that interfere with the performance of the
Profile Library.

NOTE: As a simpler alternative, the version of the OAL toolkit found
on Rings Node archive volumes already contains these changes in the
"software/oal/source" subdirectory. Also, an included file
"software/oal/aareadme.txt" contains a very streamlined description of
how to build the toolkit.

5.3 UNIX Build Instructions

To build the tools, you must have already built the PDS Object Access
Library. This directory must contain a copy of the library "oal.a", or
else a symbolic link to the library. The directory must also contain a
subdirectory "oal" containing the C include files "*.h" for the OAL,
or else a symbolic link to the directory. By default, these files
reside in the "source/" subdirectory of the OAL library tree.

For example, if the OAL is in a parallel directory called "oal/", then
these commands will create the necessary links:
    ln -s ../oal/source/oal.a oal.a
    ln -s ../oal/source oal

This library has been tested on UNIX systems by DEC, Sun, and Silicon
Graphics and Macintosh OS X. To build the library and test binaries
on a Sun, type
    chmod +x makesun.com
    makesun.com
To build the library and binaries on a system by DEC or Silicon
Graphics, type
    chmod +x makedec.com
    makedec.com
To build the library and binaries on a Macintosh under OS X, type
    chmod +x makemac.com
    makemac.com
The script file "make*.com" will compile each file and build two
archive files called "profile.a" and "qprofile.a". (Note that any
pre-existent files called "profile.a" and "qprofile.a" should be
removed first). The sample program binaries are called "ppsfilt" and
"ppsresam" and are found in the "examples/" subdirectory.

Note that the commands "cc" and "f77" are used by these scripts. Be
sure that your command search path includes these before executing the
script.

To use the library, include either "profile.a" (for Standard Mode) or
"qprofile.a" (for Quick Mode) among the files that appear on a cc or
f77 command line. Also include "oal.a". Note that for C programs, you
must also include the "-lm" option to load in the C math libraries.

5.4 VMS Build Instructions

To build the tools, you must have already built the PDS Object Access
Library. You must then define a logical symbol "OAL", which points to
the directory/directories containing the PDS Object Access Library
"OAL.OLB" and the C include files *.h for that library.

For example, if the OAL is in a parallel directory called OAL.DIR,
then this command will define the necessary symbol:
    DEFINE OAL [-.OAL.SOURCE]

To build the library and executables on a Vax or Alpha using the VMS
operating system, type
    @MAKELIB
This will compile each file and build two object libraries called
PROFILE.OLB and QPROFILE.OLB. The sample program binaries are called
PPSFILT.EXE and PPSRESAM.EXE.

To use the library, specify PROFILE/LIBRARY (for Standard Mode) or
QPROFILE/LIBRARY (for Quick Mode) among the files in a LINK command.
You must also include OAL:OAL/LIBRARY. For programs written in
FORTRAN, you must also include SYS$LIBRARY:VAXCRTL/LIBRARY because the
C libraries are not linked in by default.

