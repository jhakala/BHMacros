{

TF1 *f2 = new TF1("f2","1.97e6 * pow(1 + x/7e3, -39.59) / pow(x/7e3, -1.803 - 0.9371*log(x/7e3))",1200,7000);

TF1 *f3 = new TF1("f3","0.701 * 3.333e9 * pow(1 + x/7e3, -50.24) / pow(x/7e3, -6.448 - 1.863*log(x/7e3))",1200,7000);

TF1 *f = new TF1("f","(f3-f2)/f3",1200,7000);

f2->SetLineColor(1);
f3->SetLineColor(2);
f->SetLineColor(4);
f2->Draw();
f3->Draw("same");
f->Draw("same");
}
