{
//point 1

//method we used:
//rl = roostats_limit(12083, 532, 0.736, 0.073, 227.7, 110.6, 213, kFALSE, 1, "cls", "my.png",12345);
//cout<<" "<<endl;
//cl95 = rl.GetObservedLimit();

//cout<<"cl95 "<<cl95<<endl;

//result => [roostats_cl95]: 95% C.L. upper limit: 0.0169905


//alternate
//rl = roostats_cl95(12083, 532, 0.736, 0.073, 227.7, 110.6, 213, kFALSE, 1, "cls", "my.png",12345);
//result => [roostats_cl95]: 95% C.L. upper limit: 0.0169905


//bayesian
//rl = roostats_cl95(12083, 532, 0.736, 0.073, 227.7, 110.6, 213, kFALSE, 1, "bayesian", "")
//result => [roostats_cl95]: 95% C.L. upper limit: 0.013402
//cla = roostats_cla(12083, 532, 1.0, 0.1, 227.7, 110.6, 1)

//point 4
//BH5_BM-MD3.0_M5.0_n4       1.438e-03 3 4200    0.410 7.11889e+00        4  8.243e+00  1.505e+01  1.738e-03  1.536e-03

//rl = roostats_limit(12083, 532, 0.410, 0.041, 8.243, 15.05, 4, kFALSE, 1, "cls", "my.png",12345);
//cla = rl.GetExpectedLimit();

//cout<<"cla "<<cla<<endl;

cl95 = roostats_cl95(12083, 532, 0.410, 0.041, 8.243, 15.05, 4, kFALSE, 1, "bayesian", "");
cout<<"bayesian cl95 "<<cl95<<endl;


//result (Double_t)1.52936624233553282e-03

cla  = roostats_cl95(12083, 532, 0.410, 0.041, 8.243, 15.05, 1);
cout<<"bayesian cla "<<cla<<endl;


//result (Double_t)9.24103785895148450e-04

cla_zero  = roostats_cl95(12083, 532, 0.410, 0.041, 8.243, 0.0, 1);
cout<<"bayesian cla zero bkg uncert "<<cla_zero<<endl;

//result (Double_t)9.24103785895148450e-04

}
