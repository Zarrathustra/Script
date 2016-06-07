#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

#include <gsl/gsl_statistics.h>
#include <gsl/gsl_cdf.h>
#include <gsl/gsl_randist.h>

#define CONF_ALPHA 0.05

using namespace std;

double Gaussian2DConfidenceArea(const double s0,
                                const double s1)
{
    //return s0 * s1;
    return 2 * M_PI * s0 * s1 * gsl_cdf_chisq_Qinv(CONF_ALPHA, 2);
};

int main()
{
    ifstream file = ifstream("../Data/Particle_Sample.par");

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

    /***
    int n = xTrans.size();
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

    double s0 = gsl_stats_sd(&xTrans[0], 1, xTrans.size());
    double s1 = gsl_stats_sd(&yTrans[0], 1, yTrans.size());

    printf("s0 = %10f, s1 = %10f\n", s0, s1);

    printf("gsl_cdf_chisq_Qinv(CONF_ALPHA, 2) = %10f\n",
           gsl_cdf_chisq_Qinv(CONF_ALPHA, 2));

    printf("Confidence Area of Translation: %10f\n",
           Gaussian2DConfidenceArea(s0, s1));

    return 0;
}
