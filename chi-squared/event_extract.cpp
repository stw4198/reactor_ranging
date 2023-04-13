#include <TROOT.h>
#include <TFile.h>
#include <TH1D.h>

TH1D* event_extract(const char* file,int num_events){

    TFile *in = new TFile(file,"READ");
    // if(!in->IsOpen()){
    //     printf("File %s does not exist.\n",file);
    //     return;
    // }

    TH1D* mce = (TH1D*)in->Get("mce"); 

    int nentries = mce->GetEntries();
    printf("There are %i entries\nEvents selected: %i\n",nentries,num_events);

    TH1D* mce_rand = new TH1D("mce_rand","mce_rand",1000,0,8.2);
    //TH1D* mce_rand = new TH1D("mce_rand","mce_rand",1000,0,100);

    if(num_events>nentries){
        num_events=nentries;
        printf("Setting number of events to %i\n",num_events);
    }

    for(int i=0; i<num_events; i++){
        float event = mce->GetRandom();
        mce_rand->Fill(event);
    }

    //mce_rand->Draw();

    double p[3] = { 0.25, 0.50, 0.75};
    double q[3];
    mce_rand->GetQuantiles(3,q,p);

    double IQR = q[2] - q[0];
    double n_pow = pow(nentries,1/3);
    double bin_width = 2*IQR/n_pow;

    double bins = 820/bin_width;
    int nbins = std::ceil(bins);
    printf("nbins = %i\n",nbins);

    // TH1D* mce_rebin = new TH1D("mce_rebin","mce_rebin",nbins,0,8.2);
    // for(int i=0; i<num_events; i++){
    //     float event = mce_rand->GetRandom();
    //     mce_rebin->Fill(event);
    // }
    TH1D *mce_rebin = dynamic_cast<TH1D*>(mce_rand->Rebin(1000/nbins,"mce_rebin"));
    
    int binmax = mce_rebin->GetMaximumBin();
    double maxcontent = mce_rebin->GetBinContent(binmax);

    printf("%f\n",maxcontent);

    //mce_rebin->Scale(1/mce_rebin->Integral());
    mce_rebin->Scale(1/maxcontent);
    // TCanvas * c1 = new TCanvas("c1");
    // mce_rebin->Draw();
    // c1->SaveAs("event_extract_test.png");
    // delete c1;

    // TFile *out = new TFile(Form("combined_%i_events.root",num_events),"RECREATE");
    // mce_rebin->Write();
    // out->Close();

    return mce_rebin;
    //return mce;

}