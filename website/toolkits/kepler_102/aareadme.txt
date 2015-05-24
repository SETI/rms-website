PDS_VERSION_ID                  = PDS3
RECORD_TYPE                     = STREAM

OBJECT                          = TEXT
  PUBLICATION_DATE              = 2005-02-22
  NOTE                          = "AAREADME file containing a complete
overview of the PDS Rings Node's Kepler Library, version 1.0.2."
END_OBJECT                      = TEXT
END

**********************************************************************
                     PDS Rings Node Software Library
                       Part 1: THE KEPLER LIBRARY
                      Version 1.0.2, February 2005

                            Mark R. Showalter
**********************************************************************

1. INTRODUCTION

The Kepler Library comprises a set of C functions for calculating
various aspects of a satellite orbit, such as positions, orbital
rates, resonance locations, etc. It is designed to provide a high
degree of numeric accuracy and efficiency. The library also includes a
set of functions that are more easily called from FORTRAN programs.
Each routine is found in a separate file, given by the routine's name
and with a ".c" extension (all in lower case on UNIX systems). A
header in each routine describes what it does and how it is called,
and extensive comments within the code document the algorithms used.

1.1 Change History

Version 1.0 (8/95) Original release.

Version 1.0.1 (2/04) Adds support for Macintosh OS X. It also provides
a detached PDS label file "KEPLER.LBL" and a software catalog file
"SOFTWARE.CAT", making the library suitable for archiving on any PDS
volume.

Version 1.0.2 (2/05) Adds support for LINUX using the g77 compiler.

2. SUMMARY OF ROUTINES

2.1 Orbital rate calculations

The following routines are used to calculate the relationship between
orbital rate and semimajor axis in the gravitational field of an
arbitrary, oblate planet. They are fully accurate for gravitational
moments up to J20, and will work for even higher order terms if a
symbol in file "kepler.h" is re-defined. However, they neglect any
terms of order (e^2 J2) or (sin(i)^2 J2).

Kep_SetPlanet   Used to specify a planet's gravitational field.

Kep_Omega       Returns omega, the mean motion, as a function of mean
                orbital radius.

Kep_Kappa       Returns kappa, the radial (or eccentric) oscillation
                frequency, as a function of mean orbital radius.

Kep_Nu          Returns nu, the vertical (or inclined) oscillation
                frequency, as a function of mean orbital radius.

Kep_5Freq       Returns all five physically meaningful frequencies
                associated with an orbit of given radius: omega,
                kappa, nu, and the apsidal and nodal precession rates.
                This is significantly faster than multiple calls to
                the individual functions listed above.

Kep_Combo       Returns a "combination" frequency as a function of
                mean orbital radius. A combination frequency is
                defined to be the sum of omega, kappa and nu, each
                multiplied by an integer coefficient. It employs a
                trick to retain high accuracy when the coefficients
                sum to zero.

Kep_SolveA      Solves for the mean radius at which a specified
                combination frequency equals a given value. This
                powerful routine may be used to determine a satellite
                orbit based on its mean motion, or to solve for the
                locations of arbitrary resonances. (*)

For convenience, the following two functions are provided via C macro
definitions.

Kep_Apse        returns the apsidal precession rate, equivalent to
                omega minus kappa.

Kep_Node        returns the nodal regression rate, equivalent to omega
                minus nu.

2.2 Orbital trajectory calculations

The following set of routines are used to track the position and
orbital elements of a satellite in time. Positions will be accurate
for arbitrary e < 1 and sin(i) < 1, except to the extent that orbital
precession rates become less accurate for eccentric or inclined orbits
when the central body is oblate (see restrictions on orbital rates
above). Additional perturbations from the Sun or other nearby
satellites are not included.

Kep_SetOrbit    Used to specify the orbital elements of a satellite.

Kep_Precess     Returns the orbital elements of a satellite after
                precession to a new epoch.

Kep_MeanAnom    Returns a satellite's mean anomaly, given its
                eccentricity and true anomaly.

Kep_TrueAnom    Returns a satellite's true anomaly, given its
                eccentricity and mean anomaly. (*)

Kep_Locate      Returns the planet-centered position and/or velocity of
                a satellite at a given time. (*)

2.3 Accuracy specification

In general, each routine will return values at the full
double-precision accuracy of the platform on which you are running.
However, for the routines marked with an asterisk (*) above, the user
has the option of reducing the accuracy of the result, and thereby
(perhaps) speeding up the computations.

Kep_SetError    Used to specify the approximate fractional accuracy of
                some of the above routines.

2.4 FORTRAN-compatible routines

By appending the letter "F" to the beginning of any of the above
routines, you will obtain the name of a FORTRAN-compatible equivalent.
Note that the arguments to these routines may differ slightly from the
C versions.

2.5 Internal routines

Several routines in the library have names beginning with "XKep_".
These are used internally by the other Kepler Library routines, but
are not intended for use outside the library. Documentation is
provided, but use them at your own risk.

3. EXAMPLES

Several additional programs are provided, which illustrate the use of
Kepler Library routines.

3.1 table3.f

This FORTRAN program illustrates the use of fKep_SolveA() to solve for
the location of resonances in Saturn's rings. It reproduces Table 3 of
Lissauer and Cuzzi, Resonances in Saturn's Rings, Astron. J. 87,
1051-1058. This table lists the Lindblad resonance locations of
1980S28 in units of Saturn radii.

3.2 solver.f

This FORTRAN program prompts the user for the "combination"
coefficients and then solves for either radius as a function of
frequency, or vice versa. It is set up for the Saturn system, but
could be used with any other planet by changing the gravity parameters
given in the source.

3.3 orbit.f

This simple FORTRAN program determines the coordinates of a satellite
at uniformly-spaced moments in time, based on its orbital elements.
Output may be directed either to the terminal or to a file. Once
again, it is set up for the Saturn system, but could be modified
easily.

3.4 Test programs

Several test programs written in C are also provided. They have names
beginning with "TKep_", and the remainder of the name indicates which
routine it is used to test (although, in general, these programs
actually test several library routines). These programs are used to
confirm that various sets of routines yield compatible results. They
may also provide the user with some guidance as to how to use these
routines.

4. USAGE

To use Kepler Library routines from within a C program, one should
include the file "kepler.h". This file provides a declaration
prototype for each function, and also defines the few routines treated
as macros. In addition, this file declares two special typedefs,
KEP_PLANET and KEP_ORBIT. The user need not concern him/herself with
the format of these types; they are simply used to hold information
describing a planetary gravity field, and may be treated as "black
boxes" by the user.

To call the routines from FORTRAN, no special include file is needed.

5. BUILDING INSTRUCTIONS

5.1 UNIX

This library has been tested on UNIX systems by DEC, Sun, and Silicon
Graphics. To build the library and test binaries on a Sun, type
        chmod +x makesun.com
        ./makesun.com
To build the library and binaries on a system by DEC or Silicon
Graphics, type
        chmod +x makedec.com
        ./makedec.com
To build the library and binaries under LINUX using the g77 compiler,
type
        chmod +x makeg77.com
        ./makeg77.com
In each case, the script file "make*.com" will compile each file and
build an archive file called "kepler.a". (Note that any pre-existent
file called "kepler.a" should be removed first). The test program
binaries are called "orbit", "solver" and "table3".

The commands "cc" and "f77" are used by these scripts (except makeg77,
where "g77" is called in place of "f77").  Be sure that your command
search path includes these before executing the script.

To use the library, include "kepler.a" among the files that appear on
a cc or f77 command line. Note that for C programs, you must also
include the "-lm" option to load in the C math libraries.

5.2 VMS (Vax or Alpha)

To build the library and executables on a Vax or Alpha using the VMS
operating system, type
        @MAKEVMS
This will compile each file and build an object library called
KEPLER.OLB. The test program binaries are called ORBIT.EXE, SOLVER.EXE
and TABLE3.EXE.

To use the library, include KEPLER/LIBRARY among the files in a LINK
command.

