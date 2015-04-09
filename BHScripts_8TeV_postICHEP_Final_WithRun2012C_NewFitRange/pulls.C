{

gROOT->SetStyle("Plain");
gStyle->SetOptStat(11111);

TFile *_file0 = TFile::Open("Results_1577invpb/Templates.root");

Data_N2->Sumw2();
Background_N2->Sumw2();
histoTemplateN2_0->Sumw2();
histoTemplateN3_0->Sumw2();

TH1F *ratio_data = new TH1F("ratio_data","",100,0,10000);
ratio_data->Divide(Data_N2,Background_N2);

TH1F *ratio_fits = new TH1F("ratio_fits","",100,0,10000);

TCanvas *c = new TCanvas("c","",800,600);
c->SetLogy(1);
c->cd();

Data_N2->GetXaxis()->SetRangeUser(1200,2800);
Data_N2->SetMinimum(0.1);
Data_N2->SetMarkerStyle(20);
Data_N2->Draw("PE0");
Background_N2->SetMarkerStyle(0);
Background_N2->Draw("plainsamehisto");
ratio_data->Draw("sameE1");
ratio_fits->SetLineColor(2);

for (i = 13; i< 30; ++i) {
  cout<<"ST-median "<<(i-0.5)*100
      <<" Data "<<Data_N2->GetBinContent(i)
      <<" +/- "<<Data_N2->GetBinError(i)
      <<" ; Background "<<Background_N2->GetBinContent(i)
      <<" +/- "<<Background_N2->GetBinError(i)<<endl;
  ratio_fits->SetBinContent(i,templateN3_0->Eval((i-1)*100)/templateN2_0->Eval((i-1)*100));
  
}
ratio_fits->Draw("same");


}
