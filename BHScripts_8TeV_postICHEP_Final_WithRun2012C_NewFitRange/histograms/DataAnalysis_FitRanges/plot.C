{
gStyle->SetPadTopMargin(0.05);
gStyle->SetPadRightMargin(0.05);

TFile *f1 = TFile::Open("Templates_1300_2800/Templates.root");
TH1F *n2_c = (TH1F*)f1->Get("Data_N2");
TH1F *n3_c = (TH1F*)f1->Get("Data_N3");
//TH1F *n4_c = (TH1F*)f1->Get("Data_N4");
//TH1F *n5_c = (TH1F*)f1->Get("Data_N5");
TH1F *n3up_c = (TH1F*)f1->Get("Data_N3up");
TH1F *n4up_c = (TH1F*)f1->Get("Data_N4up");
TH1F *n5up_c = (TH1F*)f1->Get("Data_N5up");
TH1F *n6up_c = (TH1F*)f1->Get("Data_N6up");
TH1F *n7up_c = (TH1F*)f1->Get("Data_N7up");
TH1F *n8up_c = (TH1F*)f1->Get("Data_N8up");

TH1F *bkg2_c = (TH1F*)f1->Get("Background_N2");
TH1F *bkg3_c = (TH1F*)f1->Get("Background_N3");
//TH1F *bkg4_c = (TH1F*)f1->Get("Background_N4");
//TH1F *bkg5_c = (TH1F*)f1->Get("Background_N5");
TH1F *bkg3up_c = (TH1F*)f1->Get("Background_N3up");
TH1F *bkg4up_c = (TH1F*)f1->Get("Background_N4up");
TH1F *bkg5up_c = (TH1F*)f1->Get("Background_N5up");
TH1F *bkg6up_c = (TH1F*)f1->Get("Background_N6up");
TH1F *bkg7up_c = (TH1F*)f1->Get("Background_N7up");
TH1F *bkg8up_c = (TH1F*)f1->Get("Background_N8up");


n2_c->SetMarkerStyle(20);
n3_c->SetMarkerStyle(20);
n3up_c->SetMarkerStyle(20);
n4up_c->SetMarkerStyle(20);
n5up_c->SetMarkerStyle(20);
n6up_c->SetMarkerStyle(20);
n7up_c->SetMarkerStyle(20);
n8up_c->SetMarkerStyle(20);


bkg2_c->SetLineWidth(2);
bkg3_c->SetLineWidth(2);
//bkg4_c->SetLineWidth(2);
//bkg5_c->SetLineWidth(2);
bkg3up_c->SetLineWidth(2);
bkg4up_c->SetLineWidth(2);
bkg5up_c->SetLineWidth(2);
bkg6up_c->SetLineWidth(2);
bkg7up_c->SetLineWidth(2);
bkg8up_c->SetLineWidth(2);


TCanvas *c = new TCanvas("c","",500,500);
c->Divide(2,2);

c->cd(1);
c->cd(1)->SetLogy(1);
n2_c->GetXaxis()->SetRangeUser(1500,5000);
n2_c->Draw("PE");
bkg2_c->Draw("histosameC");
TLegend *legend = new TLegend(0.40,0.55,0.60,0.80,"Fit: 1300_2800 GeV","brNDC");
legend->SetTextSize(0.035);
legend->SetTextFont(42);
legend->SetFillColor(0);
legend->SetLineColor(0);
legend->AddEntry(n2_c,"Run2012A data (4.62 fb^{-1})","p");
legend->AddEntry(bkg2_c,"Background Run2012A","l");
legend->Draw();

c->cd(2);
c->cd(2)->SetLogy(1);
n3_c->GetXaxis()->SetRangeUser(1500,5000);
n3_c->Draw("PE");
bkg3_c->Draw("histosameC");

/*
c->cd(3);
c->cd(3)->SetLogy(1);
n4_c->GetXaxis()->SetRangeUser(1500,5000);
n4_c->Draw("PE");
bkg4_c->Draw("histosameC");

c->cd(4);
c->cd(4)->SetLogy(1);
n5_c->GetXaxis()->SetRangeUser(1500,5000);
n5_c->Draw("PE");
bkg5_c->Draw("histosameC");
*/

c->Update();
c->Print("ST_Excl_Fit_1300_2800.pdf");

TCanvas *c1 = new TCanvas("c1","",1200,600);
c1->Divide(3,2);

c1->cd(1);
c1->cd(1)->SetLogy(1);
n3up_c->GetXaxis()->SetRangeUser(1500,5000);
n3up_c->Draw("PE");
bkg3up_c->Draw("histosameC");
TLegend *legend = new TLegend(0.40,0.55,0.60,0.80,"Fit: 1300_2800 GeV","brNDC");
legend->SetTextSize(0.035);
legend->SetTextFont(42);
legend->SetFillColor(0);
legend->SetLineColor(0);
legend->AddEntry(n2_c,"Run2012A","p");
legend->AddEntry(bkg2_c,"Background Run2012A","l");
legend->Draw();

c1->cd(2);
c1->cd(2)->SetLogy(1);
n4up_c->GetXaxis()->SetRangeUser(1500,5000);
n4up_c->Draw("PE");
bkg4up_c->Draw("histosameC");

c1->cd(3);
c1->cd(3)->SetLogy(1);
n5up_c->GetXaxis()->SetRangeUser(1500,5000);
n5up_c->Draw("PE");
bkg5up_c->Draw("histosameC");

c1->cd(4);
c1->cd(4)->SetLogy(1);
n6up_c->GetXaxis()->SetRangeUser(1500,5000);
n6up_c->Draw("PE");
bkg6up_c->Draw("histosameC");

c1->cd(5);
c1->cd(5)->SetLogy(1);
n7up_c->GetXaxis()->SetRangeUser(1500,5000);
n7up_c->Draw("PE");
bkg7up_c->Draw("histosameC");

c1->cd(6);
c1->cd(6)->SetLogy(1);
n8up_c->GetXaxis()->SetRangeUser(1500,5000);
n8up_c->Draw("PE");
bkg8up_c->Draw("histosameC");

c1->Update();
c1->Print("ST_Incl_Fit_1300_2800.pdf");

}
