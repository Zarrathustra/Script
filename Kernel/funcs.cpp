#include "funcs.h"

double kaiser_value(double r, double a, double alpha, int m)
{
    double rda, rdas, arg, w;
    rda = r / a;
    rdas = rda * rda;
    if (rdas <= 1.0)
    {
        arg = alpha * sqrt(1.0 - rdas);
        if (m == 0)
        {
            w = bessi0(arg) / bessi0(alpha);
        }
        else if (m == 1)
        {
            w = sqrt (1.0 - rdas);
            if (alpha != 0.0)
                w *= bessi1(arg) / bessi1(alpha);
        }
        else if (m == 2)
        {
            w = sqrt (1.0 - rdas);
            w = w * w;
            if (alpha != 0.0)
                w *= bessi2(arg) / bessi2(alpha);
        }
        else if (m == 3)
        {
            w = sqrt (1.0 - rdas);
            w = w * w * w;
            if (alpha != 0.0)
                w *= bessi3(arg) / bessi3(alpha);
        }
        else if (m == 4)
        {
            w = sqrt (1.0 - rdas);
            w = w * w * w *w;
            if (alpha != 0.0)
                w *= bessi4(arg) / bessi4(alpha);
        }
    }
    else
        w = 0.0;
    return w;
}

double kaiser_Fourier_value(double w, double a, double alpha, int m)
{
    double sigma = sqrt(std::abs(alpha * alpha - (2. * M_PI * a * w) * (2. * M_PI * a * w)));
    if (m == 2)
    {
        if (2.*M_PI*a*w > alpha)
            return  pow(2.*M_PI, 3. / 2.)*pow(a, 3.)*pow(alpha, 2.)*bessj3_5(sigma)
                    / (bessi0(alpha)*pow(sigma, 3.5));
        else
            return  pow(2.*M_PI, 3. / 2.)*pow(a, 3.)*pow(alpha, 2.)*bessi3_5(sigma)
                    / (bessi0(alpha)*pow(sigma, 3.5));
    }
    else if (m == 0)
    {
        if (2*M_PI*a*w > alpha)
            return  pow(2.*M_PI, 3. / 2.)*pow(a, 3)*bessj1_5(sigma)
                    / (bessi0(alpha)*pow(sigma, 1.5));
        else
            return  pow(2.*M_PI, 3. / 2.)*pow(a, 3)*bessi1_5(sigma)
                    / (bessi0(alpha)*pow(sigma, 1.5));
    }
}

double  basvolume(double a, double alpha, int m, int n)
{
    double  hn, tpi, v;
    hn = 0.5 * n;
    tpi = 2.0 * M_PI;
    if (alpha == 0.0)
    {
        if ((n / 2)*2 == n)           /* n even                               */
            v = pow(tpi, hn) * in_zeroarg(n / 2 + m) / in_zeroarg(m);
        else                        /* n odd                                */
            v = pow(tpi, hn) * inph_zeroarg(n / 2 + m) / in_zeroarg(m);
    }
    else
    {                        /* alpha > 0.0                          */
        if ((n / 2)*2 == n)           /* n even                               */
            v = pow(tpi / alpha, hn) * i_n(n / 2 + m, alpha) / i_n(m, alpha);
        else                        /* n odd                                */
            v = pow(tpi / alpha, hn) * i_nph(n / 2 + m, alpha) / i_n(m, alpha);
    }
    return v * pow(a, (double)n);
}

double i_n(int n, double x)
{
    int i;
    double i_ns1, i_n, i_np1;
    if (n == 0)   return bessi0(x);
    if (n == 1)   return bessi1(x);
    if (x == 0.0) return 0.0;
    i_ns1 = bessi0(x);
    i_n   = bessi1(x);
    for (i = 1; i < n; i++)
    {
        i_np1 = i_ns1 - (2 * i) / x * i_n;
        i_ns1 = i_n;
        i_n   = i_np1;
    }
    return i_n;
}

double i_nph(int n, double x)
{
    int i;
    double r2dpix;
    double i_ns1, i_n, i_np1;
    if (x == 0.0) return 0.0;
    r2dpix = sqrt(2.0 / (M_PI * x));
    i_ns1 = r2dpix * cosh(x);
    i_n   = r2dpix * sinh(x);
    for (i = 1; i <= n; i++)
    {
        i_np1 = i_ns1 - (2 * i - 1) / x * i_n;
        i_ns1 = i_n;
        i_n   = i_np1;
    }
    return i_n;
}

double in_zeroarg(int n)
{
    int i;
    double fact;
    fact = 1.0;
    for (i = 1; i <= n; i++)
    {
        fact *= 0.5 / i;
    }
    return fact;
}

double inph_zeroarg(int n)
{
    int i;
    double fact;
    fact = 1.0;
    for (i = 1; i <= n; i++)
    {
        fact *= 1.0 / (2 * i + 1.0);
    }
    return fact*sqrt(2.0 / M_PI);
}
