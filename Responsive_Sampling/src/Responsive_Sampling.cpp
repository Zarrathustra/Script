#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

#include <gsl/gsl_statistics.h>
#include <gsl/gsl_cdf.h>
#include <gsl/gsl_randist.h>

#include "DirectionalStat.h"

#define CONF_ALPHA 0.05

using namespace std;

double Gaussian2DConfidenceArea(const double s0,
                                const double s1)
{
    return M_PI * s0 * s1 * gsl_cdf_chisq_Qinv(CONF_ALPHA, 2);
};

double Gaussian3DConfidenceArea(const double s0,
                                const double s1,
                                const double s2)
{
    return M_PI * s0 * s1 * s2 * gsl_cdf_chisq_Qinv(CONF_ALPHA, 3);
};

/**
 * Confidence Area Size of ACG.
 * Note: ACG is an axial distribution. Thus, this function returns the size of one modal.
 * lf : loose factor
 */
double ACG4DConfidenceArea(const double rVari)
{
    return Gaussian3DConfidenceArea(1.0 / rVari, 1.0 / rVari, 1.0 / rVari);
};

int main(int argc, char* argv[])
{
    ifstream file = ifstream(argv[1]);

    vector<double> xTrans;
    vector<double> yTrans;
    vector<double> w;
    vector<double> x;
    vector<double> y;
    vector<double> z;
    vector<double> W;

    double tmp[7];
    while (!file.eof())
    {
        file >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3] >> tmp[4] >> tmp[5] >> tmp[6];
        /***
        printf("%10f %10f %10f %10f %10f %10f %10f\n",
               tmp[0],
               tmp[1],
               tmp[2],
               tmp[3],
               tmp[4],
               tmp[5],
               tmp[6]);
        ***/
        xTrans.push_back(tmp[0]);
        yTrans.push_back(tmp[1]);
        w.push_back(tmp[2]);
        x.push_back(tmp[3]);
        y.push_back(tmp[4]);
        z.push_back(tmp[5]);
        W.push_back(tmp[6]);
    }

    int n = xTrans.size();

    /***
    for (int i = 0; i < n; i++)
    {
        printf("%10f %10f %10f %10f %10f %10f %10f\n",
               xTrans[i],
               yTrans[i],
               w[i],
               x[i],
               y[i],
               z[i],
               W[i]);
    }
    ***/

    /***
    double s0 = gsl_stats_sd(&xTrans[0], 1, xTrans.size());
    double s1 = gsl_stats_sd(&yTrans[0], 1, yTrans.size());

    printf("s0 = %10f, s1 = %10f\n", s0, s1);

    printf("gsl_cdf_chisq_Qinv(CONF_ALPHA, 2) = %10f\n",
           gsl_cdf_chisq_Qinv(CONF_ALPHA, 2));

    printf("Confidence Area of Translation: %10f\n",
           Gaussian2DConfidenceArea(s0, s1));

    printf("Sampling Points of Translation: %d\n",
           (int)(2 * 2 / Gaussian2DConfidenceArea(s0, s1)));
    ***/

    mat4 m(n, 4);
    for (int i = 0; i < n; i++)
    {
        m(i, 0) = w[i];
        m(i, 1) = x[i];
        m(i, 2) = y[i];
        m(i, 3) = z[i];
    }

    double k0, k1;
    inferACG(k0, k1, m);

    printf("k0 = %10f, k1 = %10f\n", k0, k1);

    printf("Confidence Area of Rotation: %.15f\n",
           ACG4DConfidenceArea(sqrt(k0 / k1)));

    printf("Sampling Points of Rotation: %12f\n",
           (2 * M_PI / ACG4DConfidenceArea(sqrt(k0 / k1))));

    printf("Sqrt of Sampling Points of Rotation: %12f\n",
           sqrt((2 * M_PI / ACG4DConfidenceArea(sqrt(k0 / k1)))));

    return 0;
}
