
(*) Nota: Revised version v2.1 of phesat95.exe on November 1994



              ----------------------------------

                                 PHESAT95                                
                     Saturnian events of the 1995 period      
                                                                                  

                     ftp anonymous server :   ftp.bdl.fr
                     ==========================

              ----------------------------------

  This set of files contains data concerning the events
occurring in the Saturnian satellites system from 1992 to 1999.
A part of these predictions have been published in:

Arlot, J.E. and Thuillot, W.: 1993, Eclipses and Mutual events of the first
eight Saturnian satellites during the 1993-1996 period. Icarus 105, 427.



1. Description of the files:
   ------------------------

1.1 ascii sequential files:
    
    The following files are avalaible under their compressed version (compressed 
thanks to the gzip command). Use the gunzip command to uncompress them. You will 
obtain:
    
    TABLE4.dat:   selected dates of eclipses by Saturn 
                  (table 4 extracted from Arlot and Thuillot, 1993)
    TABLE5.dat:   selected dates of mutual events of the Saturnian satellites
                  (table 5 extracted from Arlot and Thuillot, 1993)
    ECL95.dat:    data for the eclipses by Saturn from 1992 to 1998
    PH92 to 99:   data for the whole set of events involving the planet
                  from 1992 to 1999 (transits, umbra, occultations and
                  eclipses)
    PHM95.DAT:    data concerning the mutual eclipses and occultations
                  from the end of 1994 to the beginning of 1997


1.2 compressed set of PC files:

	phenpc.exe is a self extractor PC file. Copy it on the hard disk of 
your PC and run phenpc. You will obtain the following files:

(*) PHESAT95.exe: PC software to be used in order to read selected records
                  from the previous files. This selection is made thanks to
                  parameters such as heigth of Saturn above the horizon,
                  height of the Sun, distance to the planet...
    SATURN.INI:   setup file used by Phesat95.exe
    SATURN.HLP:   help  file used by Phesat95.exe
    HAUSA92 to 99:files of planetary positions used by Phesat95.exe (don't
                  modify them) .
    HAUSO92 to 99:files of solar positions used by Phesat95.exe (don't
                  modifythem)
    LONGIT.DAT:   file used by Phesat95.exe which contain the names and
                  coordinates of the different sites from where you
                  could compute the local conditions of observation.
                  Insert your own coordinates in it thanks to any editor
                  or thanks to the L command of phesat95.exe.



2. Description of the data:
   -----------------------

Instead of using the Phesat95.exe software to get the selected data you can
directly read these data in the files PH92.DAT to PH99.DAT, ECL95.DAT or
PHM95.DAT. These files contain records with the following format.

In all these files, the satellites are numbered as following:

       1: Mimas
       2: Encelade
       3: Thetys
       4: Dione
       5: Rhea
       6: Titan
       7: Hyperion
       8: Iapetus

File PHx.DAT: eclipses, shadows, transits and occultations

       Y M D  H M S   PHEN   X     Y          D    E     MO   SU
    1992 9 3  14143.0 1ECR   0.74  0.75      33    1.0   73  152

Y M D: year month day
H M S: hour minute second in Terrestrial Time (TT):
       date of the mid eclipse (50% light flux drop) or mid event
       (bissection of the satellite or its umbra by the edge of Saturn).
       Substract TT-TU values (about 60 seconds) in order to get the
       TU dates
PHEN:  type of phenomenon: 1ECR means eclipse of Mimas reappearence.
       ECD and ECR means eclipse disappearence and reappearence
       OCD and OCR means occultation disappearence and reappearence
       TRI and TRE means transit ingress and egress
       SHI and SHE means transit of the shadow ingress and egress
X Y:   differential coordinates of the satellites in radius of Saturn in
       the saturnocentric frame with X axis to the  East, Y axis to the North
D:     semi-duration of the phenomenon. You have to substract and add this
       duration to the H M S value in order to get the first and last
       contacts.
E:     distance of the satellite to the edge of Saturn in arcseconds.
MO SU: distance of the satellite to the Moon and Sun in degrees.
    



File PHM95.DAT: mutual events.

    Y  M  D  A PHE B T   H1 M1 S1   H2 M2 S2   H3 M3 S3   H4 M4 S4  H5 M5 S5    H6 M6 S6   H7 M7 S7   LF         D  SA   I     I'    M    S
 1994 11 24  3 ECL 2 P   11 37  5   11 38  0              11 46  7              11 54  9   11 55  4   0.563   1079  0.5  0.069 0.115 154  94
 1995  1 13  2 ECL 3 P    8 14 54    8 18 36               8 50  5               9 21 54    9 24 53   0.185   4199  1.9  0.054 0.116  95  46


Y M D:    year month day
A PHE B T: satellite A eclipses (PHE is ECL) or occults (PHE is OCC)
           satellite B. This phenomenon is of type T. Parameter T can be:
           C means Conjunction: grazing mutual occultation.The time H4 M4 S4
                                gives the time of least distance.
           A means Annular
           P means Partial
           T means Total
           p means by the penumbra (mutual eclipses)
H1 M1 S1: date of the first contact with the penumbra during a mutual
          eclipse. This time and the following times are in Terrestrial Time
          scale (TT): substract TT-TU values (about 60 seconds) in order to
          get the TU values.
H2 M2 S2: date of the first contact with the umbra (EC) or with the
          satellite (OC) during the ingress.
H3 M3 S3: date of the second contact
H4 M4 S4: hour minute second in Terrestrial Time (TT):
          date of the mid event (maximum of light flux drop)

H5 M5 S5: date of the first contact with the umbra (EC) or with the
          satellite (OC) during the egress
H6 M6 S6: date of the second contact
H7 M7 S7: date of the last contact with the penumbra during a mutual
          eclipse.
LF:       light flux drop (from 0 to 1)
D:        duration in seconds
SA:       distance from the center of Saturn in Saturnian radius
I:        impact parameter in arcseconds (distance between the two centers
          for occultations or between the eclipsed center and the axis of
          the umbra cone)
I':       sum of the radii in arcseconds (to appreciate how far from the
          grazing phenomenon is I)
M:        angular distance of the Moon in degrees
S:        angular distance of the sun in degrees




3. Campaign of observation:
   ------------------------



                                IMPORTANT

               Call for the observation of the Saturnian events
               ------------------------------------------------

These predictions will allow you to observe rare phenomena which occur
every 15 years. We have organized an international campaign to collect this
type of data which are of high interest for dynamical studies and space
exploration of the Saturnian satellites system.

We are interested to receive the observations of the eclipses by Saturn and
the mutual events. Photometric or CCD observations are welcome but visual
observation may also be of interest.

Be careful to the time scale!
----------------------------

For the analysis we need to get a timing of the events in the Universal Time
scale. We wish an accuracy better than 1 seconde of time.

Well equiped observers can get lightcurves or CCD images from which
photometric analysis will allow us to get physical parameters concerning
the surface of the satellites and positional measurements. A high positional
precision can be obtained from such records (down to 100 km). A complete set
of photometric measurement must include measurements of reference stars (solar
spectral type or other satelites) and measurements of the involved satellites
before and after the phenomenon.

Visual observations could be light flux measurements versus UT timing if
you practise light flux measurements by comparison with other satellites
or stars. If you don't practise this method, measure the time of the
mid event (50% light flux drop) for the eclipses and measure the time of
maximum of light flux drop for the mutual events.



              ----------------------------------------------- 

                              CONTACT ADDRESS
                                 _________

               For any further informations please contact us
               to the following address:


               J.E. Arlot and W. Thuillot

               PHESAT95 Campaign
               Bureau des Longitudes
               Unite Associee au CNRS 707
               77 Avenue Denfert  Rochereau
               F-75014 PARIS (France)

               Phone   :   (33) 1 40 51 22 70
               Fax     :   (33) 1 46 33 28 34
               E-Mail  :   thuillot@bdl.fr / arlot@bdl.fr
              -----------------------------------------------
              (c) 1992,1994 Bureau des Longitudes v2.1

