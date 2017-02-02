#include <cmath>

#include "numerical_recipes.h"

/** Function actually computing the blob value. */
double kaiser_value(double r, double a, double alpha, int m);

/** Function actually computing the blob Fourier transform. */
double kaiser_Fourier_value(double w, double a, double alpha, int m);

/** Function actually computing the blob integral */
double  basvolume(double a, double alpha, int m, int n);

/** Limit (z->0) of (1/z)^n I_n(z) (needed by basvolume)*/
double in_zeroarg(int n);

/** Limit (z->0) of (1/z)^(n+1/2) I_(n+1/2) (z) (needed by basvolume)*/
double inph_zeroarg(int n);

/** Bessel function I_(n+1/2) (x),  n = 0, 1, 2, ... */
double i_nph(int n, double x);

/** Bessel function I_n (x),  n = 0, 1, 2, ...
 Use ONLY for small values of n */
double i_n(int n, double x);
