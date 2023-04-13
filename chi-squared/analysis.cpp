#include <TROOT.h>
#include <TFile.h>
#include <TH1D.h>
#include "TGraphErrors.h"
#include "func.h"
#include <vector>
#include <iostream>

#include "event_extract.cpp"

double range(const char* file, int events){

    //gROOT->SetBatch(kTRUE);

    TH1D* mce = event_extract(file,events); //loop events
    int nentries = mce->GetEntries();
    printf("There are %i entries\n",nentries);

    int nbins = mce->GetNbinsX();

    printf("There are %i bins\n",nbins);

    const char* script_command = Form("/bin/python3 /home/stw4198/Documents/WATCHMAN/ranging/efficiency-check/efficiency_correction.py %i",nbins);
    std::system(script_command);

    std::ifstream is("corrections.txt");
    std::istream_iterator<double> start(is), end;
    std::vector<double> correction_factor(start, end);

    std::vector<double> en = LinearSpacedArray(0,8.2,nbins);
    //std::vector<double> l = LinearSpacedArray(0,500,501);
    //std::vector<double> l = LinearSpacedArray(0,200,2001);
    //std::vector<double> l = LinearSpacedArray(10,70,5);
    //std::vector<double> l = LinearSpacedArray(0,50,51);
    std::vector<double> l = LinearSpacedArray(0,100,1001);

    double likelihood_final = 1e6;//large
    double range;

    for(int j=0;j<l.size();j++){
        TCanvas * c1 = new TCanvas("c1");
        TLegend *legend = new TLegend(0.85,0.5,0.98,0.98);
        TH1D* reactor_hist = new TH1D("reactor_hist","reactor_hist",nbins,0,8.2);

        std::vector<double> likelihood;
        double bin_value;
        for(int i=0;i<en.size();i++){
            bin_value = mce->GetXaxis()->GetBinCenter(i);
            if(bin_value>=0){
            double phi_en = phi(U_l(en[i]+q_ibd),U_h(en[i]+q_ibd),Pu_l(en[i]+q_ibd),Pu_h(en[i]+q_ibd));
            double sig_en = sigma(Ee(en[i]+q_ibd),pe(Ee(en[i]+q_ibd)));
            double osc_en = p(p21(l[j],en[i]+q_ibd),p31(l[j],en[i]+q_ibd),p32(l[j],en[i]+q_ibd));
            reactor_hist->AddBinContent(i,phi_en*sig_en*osc_en);
            }
        }

        int binmax = reactor_hist->GetMaximumBin();
        double maxcontent = reactor_hist->GetBinContent(binmax);

        reactor_hist->Scale(1/maxcontent);

        for(int i=0;i<en.size();i++){
            bin_value = mce->GetXaxis()->GetBinCenter(i);
            if(bin_value>=0){
                double energy_bin = mce->GetBinContent(i);
                double reactor_flux = reactor_hist->GetBinContent(i);
                if(en[i]>0){
                likelihood.push_back(pow(energy_bin - reactor_flux,2)/reactor_flux);
                }
            }
        }

        double likelihood_total = std::accumulate(likelihood.begin(),likelihood.end(),0.0);

        if(likelihood_total<likelihood_final){
            range = l[j];
            likelihood_final=likelihood_total;
        }
        
        gStyle->SetOptStat(0);
        reactor_hist->GetXaxis()->SetTitle("Positron Kinetic Energy [MeV]");
        reactor_hist->SetTitle("");
        reactor_hist->SetLineColor(1);
        reactor_hist->SetLineWidth(2);
        mce->SetLineColor(2);
        legend->AddEntry(reactor_hist,"PDF");
        legend->AddEntry(mce,"Data");
        reactor_hist->Draw();
        mce->Draw("same");
        legend->Draw();
        c1->SaveAs(Form("hartlepool/hartlepool_%f.png",l[j]));
        
        delete reactor_hist;
        delete legend;
        delete c1;
    }

    printf("Range = %f km (metric = %f)\n\n",range,likelihood_final);

    return range;

}

// Linear interpolation
std::vector<double> LinearSpacedArray(double a, double b, std::size_t N)
{
    double h = (b - a) / static_cast<double>(N-1);
    std::vector<double> xs(N);
    std::vector<double>::iterator x;
    double val;
    for (x = xs.begin(), val = a; x != xs.end(); ++x, val += h) {
        *x = val;
    }
    return xs;
}

std::vector<double> range_err(const char* file, int events, int repeats){

    gROOT->SetBatch(kTRUE);

    double range_val;
    std::vector<double> range_val_vec;    

    //int repeats = 100;

    for (int i=0;i<repeats;i++){
        range_val = range(file,events);
        range_val_vec.push_back(range_val);
    }

    double sum = std::accumulate(range_val_vec.begin(), range_val_vec.end(), 0.0);
    double mean = sum/repeats;

    double var = 0.;
  
    for (int i = 0; i < repeats; i++){
        var += pow(range_val_vec[i]-mean,2);
    }

    var /= repeats;
    double sdev = sqrt(var);

    printf("\n\nRange = %.1f +/- %.1f km\n\n",mean,sdev);

    // std::ofstream results_file;
    // results_file.open ("results.txt", std::ios_base::app);
    // results_file << "File: " << file << " " << "Range = " << mean << " +/- " << sdev << "\n";
    // results_file.close();
  
    std::vector<double> result;
    result.push_back(mean);
    result.push_back(sdev);
    return result;

}

void range_dist(const char* file, int repeats){

    gROOT->SetBatch(kTRUE);

    int step = 50;
    int first_step = 1600;
    int final_step = 1800;

    std::vector<double> nevents = LinearSpacedArray(first_step,final_step,(final_step-first_step+step)/step);

    std::vector<double> ranges;
    std::vector<double> errors;

    for(int j=0; j<nevents.size(); j++){

        std::vector<double> result = range_err(file,nevents[j],repeats);

        ranges.push_back(result[0]);
        errors.push_back(result[1]);

    }
    for(int i=0; i<ranges.size(); i++){
        printf("Range (%f events) = %f +/- %f\n",nevents[i],ranges[i],errors[i]);
    }

    const int n = ranges.size();

    double rate = 3.26456/2;

    double ranges_arr[n];
    std::copy(ranges.begin(),ranges.end(),ranges_arr);
    double error_arr[n];
    std::copy(errors.begin(),errors.end(),error_arr);
    for(int i=0; i<n; i++){error_arr[i] = ranges[i] * pow( pow(errors[i],2)/pow(ranges[i],2) + pow(0.027,2) + 1/nevents[i],0.5);}
    double events_arr[n];
    std::copy(nevents.begin(),nevents.end(),events_arr);
    double events_err[n];
    for(int i=0; i<n; i++){events_err[i]=0;}
    double months[n];
    for(int i=0; i<n; i++){months[i]=events_arr[i]/(rate*365.25/12);}

    TCanvas *canvas = new TCanvas("canvas", "canvas");
    auto graph = new TGraphErrors(n,months,ranges_arr,events_err,error_arr);
    graph->GetXaxis()->SetTitle("Months of Observation");
    graph->GetYaxis()->SetTitle("Observed Range [km]");
    graph->SetTitle("");
    graph->Draw();
    canvas->SaveAs("hartlepool_res_events.pdf");

}
