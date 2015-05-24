cd source

cc -c -I../oal -D_NO_PROTO *.c
f77 -c *.for

ar cr ../profile.a *.o
ranlib ../profile.a

rm *.o

cc -c -I../oal -D_NO_PROTO -DQUICK *.c
f77 -c *.for

ar cr ../qprofile.a *.o
ranlib ../qprofile.a

rm *.o

cd ../examples

f77 -o ppsfilt ppsfilt.for ../profile.a ../oal.a
f77 -o ppsresam ppsresam.for ../profile.a ../oal.a

cd ..
