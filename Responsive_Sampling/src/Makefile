CXX = g++
CXXFLAGS = -std=c++11 -lgsl

SRCS = $(wildcard *.cpp)  
EXES = $(patsubst %cpp, %exe, $(SRCS))  

all : ${EXES}

%.exe : %.cpp
	${CXX} ${CXXFLAGS} $< -o $@

clean :
	rm -rf *.exe
