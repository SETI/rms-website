cc -c \
dates.c \
format.c \
juldates.c \
leapsecs.c \
parse.c \
seconds.c \
tai_et.c \
utc_tai.c
f77 -f -c fjulian.for

cc -c fortran.c rlerrors.c rlmemory.c
f77 -f -c fstrings.for

ar cr julian.a \
dates.o \
format.o \
juldates.o \
leapsecs.o \
parse.o \
seconds.o \
tai_et.o \
utc_tai.o \
fjulian.o \
fortran.o \
rlerrors.o \
rlmemory.o \
fstrings.o \

ranlib julian.a

rm *.o

f77 -f -o tconvert tconvert.for julian.a
