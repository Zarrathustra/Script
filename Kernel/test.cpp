#include <iostream>

#include <gsl/gsl_sf_bessel.h>

#include "numerical_recipes.h"
#include "funcs.h"

using namespace std;

#define RADIUS 1.9
#define PF 2
#define ALPHA 15

//#define BESSEL_J_0
//#define BESSEL_I_0
//#define BESSEL_I_1
//#define BESSEL_I_3
//#define BESSEL_I_4

//#define MKB_FT
#define MKB_RL

int main()
{
#ifdef BESSEL_J_0
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessj0(i) << ", " << gsl_sf_bessel_J0(i) << endl;
#endif

#ifdef BESSEL_I_0
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessi0(i) << ", " << gsl_sf_bessel_I0(i) << endl;
#endif

#ifdef BESSEL_I_1
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessi1(i) << ", " << gsl_sf_bessel_I1(i) << endl;
#endif

#ifdef BESSEL_I_2
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessi2(i) << ", " << gsl_sf_bessel_In(2, i) << endl;
#endif

#ifdef BESSEL_I_3
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessi3(i) << ", " << gsl_sf_bessel_In(3, i) << endl;
#endif

#ifdef BESSEL_I_4
    for (double i = 0; i < 10; i += 0.01)
        cout << i << ", " << bessi4(i) << ", " << gsl_sf_bessel_In(4, i) << endl;
#endif

#ifdef MKB_FT
    for (double i = 0; i < 2; i += 0.01)
        cout << i << ", " << kaiser_value(i, PF * RADIUS, ALPHA, 0) << endl;
#endif

#ifdef MKB_RL
    for (double i = 0; i < 5; i += 0.01)
        cout << i << ", " << kaiser_Fourier_value(i, PF * RADIUS, ALPHA, 0) << endl;
#endif
}
