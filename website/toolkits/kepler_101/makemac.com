cc -c \
kep_5freq.c \
kep_combo.c \
kep_kappa.c \
kep_locate.c \
kep_meananom.c \
kep_nu.c \
kep_omega.c \
kep_precess.c \
kep_seterror.c \
kep_setorbit.c \
kep_setplanet.c \
kep_solvea.c \
kep_trueanom.c \
xkep_jseries.c \
xkep_meananom.c \
xkep_trueanom.c \
fkep_5freq.c \
fkep_apse.c \
fkep_combo.c \
fkep_kappa.c \
fkep_locate.c \
fkep_meananom.c \
fkep_node.c \
fkep_nu.c \
fkep_omega.c \
fkep_precess.c \
fkep_seterror.c \
fkep_setorbit.c \
fkep_setplanet.c \
fkep_solvea.c \
fkep_trueanom.c

ar cr kepler.a \
kep_5freq.o \
kep_combo.o \
kep_kappa.o \
kep_locate.o \
kep_meananom.o \
kep_nu.o \
kep_omega.o \
kep_precess.o \
kep_seterror.o \
kep_setorbit.o \
kep_setplanet.o \
kep_solvea.o \
kep_trueanom.o \
xkep_jseries.o \
xkep_meananom.o \
xkep_trueanom.o \
fkep_5freq.o \
fkep_apse.o \
fkep_combo.o \
fkep_kappa.o \
fkep_locate.o \
fkep_meananom.o \
fkep_node.o \
fkep_nu.o \
fkep_omega.o \
fkep_precess.o \
fkep_seterror.o \
fkep_setorbit.o \
fkep_setplanet.o \
fkep_solvea.o \
fkep_trueanom.o

ranlib kepler.a
rm kep_*.o xkep_*.o fkep_*.o

f77 -f -o orbit.bin  orbit.for  kepler.a
f77 -f -o solver.bin solver.for kepler.a
f77 -f -o table3.bin table3.for kepler.a
