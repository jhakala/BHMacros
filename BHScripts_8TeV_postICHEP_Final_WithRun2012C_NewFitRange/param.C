{

Float_t p0[4] = {14.3,15.4,15.8,14.1};
Float_t p1[4] = {-39.4,-42.7,-47.0,-38.5};
Float_t p2[4] = {1.6e-3,2.1e-3,3.0e-3,1.0e-3};

Float_t e0[4] = {8.6e-2,7e-2,7.6e-2,9.9e-2};
Float_t e1[4] = {5.6e-1,4.6e-1,5.0e-1,6.5e-1};
Float_t e2[4] = {1.5e-4,1.3e-4,1.4e-4,1.8e-4};

Float_t n[4] = {2,3,4,5};
Float_t m[4] = {0};

TGraphErrors *gr0 = new TGraphErrors(4,n,p2,m,e2);
gr0->SetMarkerStyle(20);
gr0->Draw("Ape");

}
