test.exe : test.o numerical_recipes.o funcs.o
	g++ -lgsl test.o numerical_recipes.o funcs.o -o $@

test.o : test.cpp
	g++ -c test.cpp -o $@

numerical_recipes.o : numerical_recipes.h numerical_recipes.cpp
	g++ -c numerical_recipes.cpp -o $@

funcs.o : funcs.h funcs.cpp
	g++ -c funcs.cpp -o $@
