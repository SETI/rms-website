cd source

cc -c -I../oal *.c
f77 -c -f *.for

ar cr ../profile.a *.o
ranlib ../profile.a

rm *.o

cc -c -I../oal -DQUICK *.c
f77 -c -f *.for

ar cr ../qprofile.a *.o
ranlib ../qprofile.a

rm *.o

cd ../examples

f77 -f -o ppsfilt ppsfilt.for ../profile.a ../oal.a
f77 -f -o ppsresam ppsresam.for ../profile.a ../oal.a

cd ..
