cd source

cc -c -I../oal *.c
f77 -c *.for

ar crs ../profile.a *.o

rm *.o

cc -c -I../oal -DQUICK *.c
f77 -c *.for

ar crs ../qprofile.a *.o

rm *.o

cd ../examples

f77 -o ppsfilt ppsfilt.for ../profile.a ../oal.a
f77 -o ppsresam ppsresam.for ../profile.a ../oal.a

cd ..
