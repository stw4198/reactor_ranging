#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>
#include <TH1D.h>
#include <TLeaf.h>
#include <iostream>

void merger(const char* file, const char* output){

    float rate = 0.068926642848;//0.27064593504273504 ;//1.867686063157895;
    float sig_rate = 0.126;//3.25903;//3.25903;
    float bg_rate = 0.706;//1.29705;//1.29705;
    float total_rate = sig_rate + bg_rate;
    //const char* file = "file";

    TFile *in = new TFile(file,"READ");
    if(!in->IsOpen()){
    printf("File %s does not exist.\n",file);
    return;
    }
    TTree *t = (TTree*)in->Get("data");
    //TH1D* mce = (TH1D*)like->Get("mc_energy");

    int nentries = t->GetEntries("subid==0");

    int max_energy = 10;
    float bin_width = 0.05;

    TH1D* mce = new TH1D("mce","mce",max_energy/bin_width,0,max_energy);
    TH1D* mcr = new TH1D("mcr","mcr",max_energy/bin_width,0,max_energy);
    //TH1D* mce = new TH1D("mce","mce",820,0,8.2);
    double p0 = 0.78442;
    double p1 = 0.0499966;

    std::vector<double> mce_txt;
    std::vector<double> mcr_txt;

    for(int i=0; i<nentries; i++){
        t->GetEntry(i);
        int subid = t->GetLeaf("subid")->GetValue(0);
        if(subid==0){
            mcr->Fill(p0+p1*t->GetLeaf("n100")->GetValue(0));
            mce->Fill(t->GetLeaf("mc_energy")->GetValue(0));
            mce_txt.push_back(t->GetLeaf("mc_energy")->GetValue(0));
            mcr_txt.push_back(p0+p1*t->GetLeaf("n100")->GetValue(0));
        }
    }

    //mce->Scale(1/mce->GetEntries());
    //mce->Scale(rate/total_rate);
    mce->Scale(rate/mce->GetEntries());

    //mcr->Scale(1/mcr->GetEntries());
    //mcr->Scale(rate/total_rate);
    mcr->Scale(rate/mcr->GetEntries());
    
    TFile *out = new TFile(Form("%s.root",output),"RECREATE");
    mce->Write();
    mcr->Write();
    in->Close();
    out->Close();

    std::ofstream outFile_r(Form("%s_r.txt",output));
    for(const auto &r : mcr_txt) outFile_r << r << "\n";
    std::ofstream outFile_e(Form("%s_e.txt",output));
    for(const auto &e : mce_txt) outFile_e << e << "\n";

}
