CXX = g++
CXXFLAGS = -std=c++11 -lgsl -I ./Eigen3 -Wno-deprecated-declarations  

all : Responsive_Sampling.exe

Responsive_Sampling.exe : Responsive_Sampling.o DirectionalStat.o Random.o
	${CXX} ${CXXFLAGS} $^ -o $@

Responsive_Sampling.o : Responsive_Sampling.cpp DirectionalStat.h
	${CXX} ${CXXFLAGS} -c $< -o $@

DirectionalStat.o : DirectionalStat.cpp DirectionalStat.h Random.h Typedef.h
	${CXX} ${CXXFLAGS} -c $< -o $@

Random.o : Random.cpp
	${CXX} ${CXXFLAGS} -c $< -o $@

clean :
	rm -rf *.o
	rm -rf *.exe
