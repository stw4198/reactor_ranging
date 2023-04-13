#ifndef FUNC_H
#define FUNC_H

std::vector<double> LinearSpacedArray(double a, double b, std::size_t N);

//----------------------------------------------------------------------------------------------------------------------//
//Defining the functions used to generate the Probability Distribution Functions from theory

//Flux: thi(E)
double U_l(double e) {return 0.7248*exp(3.217-3.111*e+1.395*pow(e,2)-0.369*pow(e,3)+0.04445*pow(e,4)-0.002053*pow(e,5));}
double U_h(double e) {return 0.042*exp(0.4833+0.1927*e-0.1283*pow(e,2)-0.006762*pow(e,3)+0.002233*pow(e,4)-0.0001536*pow(e,5));}

double Pu_l(double e) {return 0.2127*exp(6.413-7.432*e+3.535*pow(e,2)-0.8820*pow(e,3)+0.1025*pow(e,4)-0.00455*pow(e,5));}
double Pu_h(double e) {return 0.0205*exp(3.251-3.204*e+1.428*pow(e,2)-0.3675*pow(e,3)+0.04254*pow(e,4)-0.001896*pow(e,5));}

double phi(double ul, double uh, double pul, double puh) {return ul + uh + pul + puh;}

//Cross-Section: sigma(E)
double m_e = 0.51099895;//MeV
double m_n = 939.5654205;//MeV
double m_p = 938.27208816;//MeV
double delta = m_n - m_p;//MeV

double q_ibd = (m_n + m_e) - m_p;//MeV

double Ee(double e) {return e - delta;}
double pe(double ee) {return sqrt(pow(ee,2)-pow(m_e,2));}

double sigma(double ee, double pe) {return ee*pe;}

//oscillations: P(E)
double theta_13 = 0.149;//0.15;//rad
double theta_12 = 0.587;//0.59;//rad
double theta_23 = 0.831;//rad

//Mass (from PDG)
double m_21 = 7.53e-5;//eV^2
double m_32 = 2.453e-3;//eV^2
double m_32_inv = -2.536e-3;//ev^2 inverted
double m_31 = m_21+m_32;//2.52e-3;//eV^2 known?
double m_31_inv = m_21+m_32_inv;//ev^2

double p21(double l, double e) {return pow(cos(theta_13),4)*pow(sin(2*theta_12),2)*pow(sin((1.27*m_21*l)/(e/1000)),2);}
double p31(double l, double e) {return pow(cos(theta_12),2)*pow(sin(2*theta_13),2)*pow(sin((1.27*m_31*l)/(e/1000)),2);}
double p32(double l, double e) {return pow(sin(theta_12),2)*pow(sin(2*theta_13),2)*pow(sin((1.27*m_32*l)/(e/1000)),2);}

double p(double p21, double p31, double p32) {return 1-p21-p31-p32;}

//Combined function F(L/E):
double f(double sig, double flux, double osc) {return sig*flux*osc;}

//Pi
double pi = 2*asin(1);//pi

#endif