{
gStyle->SetPadTopMargin(0.05);
gStyle->SetPadRightMargin(0.05);

TFile *f1 = TFile::Open("Templates_1200_2800/TemplatesRun2011Combined.root");
TH1F *n2_c = (TH1F*)f1->Get("Data_N2");
TH1F *n3_c = (TH1F*)f1->Get("Data_N3");
TH1F *n4_c = (TH1F*)f1->Get("Data_N4");
TH1F *n5_c = (TH1F*)f1->Get("Data_N5");
TH1F *n3up_c = (TH1F*)f1->Get("Data_N3up");
TH1F *n4up_c = (TH1F*)f1->Get("Data_N4up");
TH1F *n5up_c = (TH1F*)f1->Get("Data_N5up");
TH1F *n6up_c = (TH1F*)f1->Get("Data_N6up");
TH1F *n7up_c = (TH1F*)f1->Get("Data_N7up");
TH1F *n8up_c = (TH1F*)f1->Get("Data_N8up");

TH1F *bkg2_c = (TH1F*)f1->Get("Background_N2");
TH1F *bkg3_c = (TH1F*)f1->Get("Background_N3");
TH1F *bkg4_c = (TH1F*)f1->Get("Background_N4");
TH1F *bkg5_c = (TH1F*)f1->Get("Background_N5");
TH1F *bkg3up_c = (TH1F*)f1->Get("Background_N3up");
TH1F *bkg4up_c = (TH1F*)f1->Get("Background_N4up");
TH1F *bkg5up_c = (TH1F*)f1->Get("Background_N5up");
TH1F *bkg6up_c = (TH1F*)f1->Get("Background_N6up");
TH1F *bkg7up_c = (TH1F*)f1->Get("Background_N7up");
TH1F *bkg8up_c = (TH1F*)f1->Get("Background_N8up");

TFile *f2 = TFile::Open("Templates_1200_2800/TemplatesRun2011A.root");
TH1F *n2_a = (TH1F*)f2->Get("Data_N2");
TH1F *n3_a = (TH1F*)f2->Get("Data_N3");
TH1F *n4_a = (TH1F*)f2->Get("Data_N4");
TH1F *n5_a = (TH1F*)f2->Get("Data_N5");
TH1F *n3up_a = (TH1F*)f2->Get("Data_N3up");
TH1F *n4up_a = (TH1F*)f2->Get("Data_N4up");
TH1F *n5up_a = (TH1F*)f2->Get("Data_N5up");
TH1F *n6up_a = (TH1F*)f2->Get("Data_N6up");
TH1F *n7up_a = (TH1F*)f2->Get("Data_N7up");
TH1F *n8up_a = (TH1F*)f2->Get("Data_N8up");

TFile *f3 = TFile::Open("Templates_1200_2800/TemplatesRun2011B.root");
TH1F *n2_b = (TH1F*)f3->Get("Data_N2");
TH1F *n3_b = (TH1F*)f3->Get("Data_N3");
TH1F *n4_b = (TH1F*)f3->Get("Data_N4");
TH1F *n5_b = (TH1F*)f3->Get("Data_N5");
TH1F *n3up_b = (TH1F*)f3->Get("Data_N3up");
TH1F *n4up_b = (TH1F*)f3->Get("Data_N4up");
TH1F *n5up_b = (TH1F*)f3->Get("Data_N5up");
TH1F *n6up_b = (TH1F*)f3->Get("Data_N6up");
TH1F *n7up_b = (TH1F*)f3->Get("Data_N7up");
TH1F *n8up_b = (TH1F*)f3->Get("Data_N8up");

n2_c->SetMarkerStyle(20);
n3_c->SetMarkerStyle(20);
n3up_c->SetMarkerStyle(20);
n4up_c->SetMarkerStyle(20);
n5up_c->SetMarkerStyle(20);
n6up_c->SetMarkerStyle(20);
n7up_c->SetMarkerStyle(20);
n8up_c->SetMarkerStyle(20);

n2_a->SetLineColor(2);
n2_b->SetLineColor(4);
n3_a->SetLineColor(2);
n3_b->SetLineColor(4);
n4_a->SetLineColor(2);
n4_b->SetLineColor(4);
n5_a->SetLineColor(2);
n5_b->SetLineColor(4);
n3up_a->SetLineColor(2);
n3up_b->SetLineColor(4);
n4up_a->SetLineColor(2);
n4up_b->SetLineColor(4);
n5up_a->SetLineColor(2);
n5up_b->SetLineColor(4);
n6up_a->SetLineColor(2);
n6up_b->SetLineColor(4);
n7up_a->SetLineColor(2);
n7up_b->SetLineColor(4);
n8up_a->SetLineColor(2);
n8up_b->SetLineColor(4);
n2_a->SetLineWidth(2);
n2_b->SetLineWidth(2);
n3_a->SetLineWidth(2);
n3_b->SetLineWidth(2);
n4_a->SetLineWidth(2);
n4_b->SetLineWidth(2);
n5_a->SetLineWidth(2);
n5_b->SetLineWidth(2);
n3up_a->SetLineWidth(2);
n3up_b->SetLineWidth(2);
n4up_a->SetLineWidth(2);
n4up_b->SetLineWidth(2);
n5up_a->SetLineWidth(2);
n5up_b->SetLineWidth(2);
n6up_a->SetLineWidth(2);
n6up_b->SetLineWidth(2);
n7up_a->SetLineWidth(2);
n7up_b->SetLineWidth(2);
n8up_a->SetLineWidth(2);
n8up_b->SetLineWidth(2);

n2_a->SetLineStyle(2);
n2_b->SetLineStyle(3);
n3_a->SetLineStyle(2);
n3_b->SetLineStyle(3);
n4_a->SetLineStyle(2);
n4_b->SetLineStyle(3);
n5_a->SetLineStyle(2);
n5_b->SetLineStyle(3);
n3up_a->SetLineStyle(2);
n3up_b->SetLineStyle(3);
n4up_a->SetLineStyle(2);
n4up_b->SetLineStyle(3);
n5up_a->SetLineStyle(2);
n5up_b->SetLineStyle(3);
n6up_a->SetLineStyle(2);
n6up_b->SetLineStyle(3);
n7up_a->SetLineStyle(2);
n7up_b->SetLineStyle(3);
n8up_a->SetLineStyle(2);
n8up_b->SetLineStyle(3);
bkg2_c->SetLineWidth(2);
bkg3_c->SetLineWidth(2);
bkg4_c->SetLineWidth(2);
bkg5_c->SetLineWidth(2);
bkg3up_c->SetLineWidth(2);
bkg4up_c->SetLineWidth(2);
bkg5up_c->SetLineWidth(2);
bkg6up_c->SetLineWidth(2);
bkg7up_c->SetLineWidth(2);
bkg8up_c->SetLineWidth(2);

/*
TCanvas *c = new TCanvas("c","",500,500);
c->Divide(2,2);

c->cd(1);
c->cd(1)->SetLogy(1);
n2_c->GetXaxis()->SetRangeUser(800,4000);
n2_c->Draw("PE");
n2_a->Draw("same");
n2_b->Draw("same");
bkg2_c->Draw("histosameC");
TLegend *legend = new TLegend(0.40,0.55,0.60,0.80,"Fit: 1200_2800 GeV","brNDC");
legend->SetTextSize(0.035);
legend->SetTextFont(42);
legend->SetFillColor(0);
legend->SetLineColor(0);
legend->AddEntry(n2_c,"Run2011A+Run2011B data (4.62 fb^{-1})","p");
legend->AddEntry(n2_a,"Run2011A data (2.18 fb^{-1})","l");
legend->AddEntry(n2_b,"Run2011B data (2.44 fb^{-1})","l");
legend->AddEntry(bkg2_c,"Background Run2011A+Run2011B","l");
legend->Draw();

c->cd(2);
c->cd(2)->SetLogy(1);
n3_c->GetXaxis()->SetRangeUser(800,4000);
n3_c->Draw("PE");
n3_a->Draw("same");
n3_b->Draw("same");
bkg3_c->Draw("histosameC");

c->cd(3);
c->cd(3)->SetLogy(1);
n4_c->GetXaxis()->SetRangeUser(800,4000);
n4_c->Draw("PE");
n4_a->Draw("same");
n4_b->Draw("same");
bkg4_c->Draw("histosameC");

c->cd(4);
c->cd(4)->SetLogy(1);
n5_c->GetXaxis()->SetRangeUser(800,4000);
n5_c->Draw("PE");
n5_a->Draw("same");
n5_b->Draw("same");
bkg5_c->Draw("histosameC");

c->Update();
c->Print("ST_Excl_Fit_1200_2800.pdf");
*/
n3up_a->Sumw2();
n3up_b->Sumw2();
n3up_c->Sumw2();
n3up_c->Divide(n3up_b,n3up_a,1,1);

n4up_a->Sumw2();
n4up_b->Sumw2();
n4up_c->Sumw2();
n4up_c->Divide(n4up_b,n4up_a,1,1);

n5up_a->Sumw2();
n5up_b->Sumw2();
n5up_c->Sumw2();
n5up_c->Divide(n5up_b,n5up_a,1,1);

n6up_a->Sumw2();
n6up_b->Sumw2();
n6up_c->Sumw2();
n6up_c->Divide(n6up_b,n6up_a,1,1);

n7up_a->Sumw2();
n7up_b->Sumw2();
n7up_c->Sumw2();
n7up_c->Divide(n7up_b,n7up_a,1,1);

n8up_a->Sumw2();
n8up_b->Sumw2();
n8up_c->Sumw2();
n8up_c->Divide(n8up_b,n8up_a,1,1);


TCanvas *c1 = new TCanvas("c1","",1200,600);
c1->Divide(3,2);

c1->cd(1);
c1->cd(1)->SetLogy(1);
n3up_c->GetXaxis()->SetRangeUser(800,4000);
n3up_c->Draw("PE");
//n3up_a->Draw("same");
//n3up_b->Draw("same");
//bkg3up_c->Draw("histosameC");
TLegend *legend = new TLegend(0.40,0.70,0.60,0.80,"","brNDC");
legend->SetTextSize(0.045);
legend->SetTextFont(42);
legend->SetFillColor(0);
legend->SetLineColor(0);
legend->AddEntry(n2_c,"Run2011B / Run2011A ratio","p");
//legend->AddEntry(n2_a,"Run2011A data (2.18 fb^{-1})","l");
//legend->AddEntry(n2_b,"Run2011B data (2.44 fb^{-1})","l");
//legend->AddEntry(bkg2_c,"Background Run2011A+Run2011B","l");
legend->Draw();

c1->cd(2);
c1->cd(2)->SetLogy(1);
n4up_c->GetXaxis()->SetRangeUser(800,4000);
n4up_c->Draw("PE");

c1->cd(3);
c1->cd(3)->SetLogy(1);
n5up_c->GetXaxis()->SetRangeUser(800,4000);
n5up_c->Draw("PE");

c1->cd(4);
c1->cd(4)->SetLogy(1);
n6up_c->GetXaxis()->SetRangeUser(800,4000);
n6up_c->Draw("PE");

c1->cd(5);
c1->cd(5)->SetLogy(1);
n7up_c->GetXaxis()->SetRangeUser(800,4000);
n7up_c->Draw("PE");

c1->cd(6);
c1->cd(6)->SetLogy(1);
n8up_c->GetXaxis()->SetRangeUser(800,4000);
n8up_c->Draw("PE");

c1->Update();
//c1->Print("ST_Incl_Fit_1200_2800.pdf");

}
