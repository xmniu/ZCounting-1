#include <iostream>
#include <string>
#include <map>
#include <tuple>
#include <stdexcept>
#include <iomanip>                  // functions to format standard I/O
//#include <fstream>                  // functions for file I/O
//#include <sstream>                  // class for parsing strings

//(66,116), 27, 2.4: 2.0908e+06/6.11118e+06     0.342
//(66,116), 27, 0.9: 516500/6.11118e+06         0.0845
//(66,116), 30, 2.4: 1.84394e+06/6.11118e+06    0.302
//(66,116), 30, 0.9: 484740/6.11118e+06         0.0793

//76X
//6.11118e+06 1.84394e+06
//484740, 713373, 645823
//const std::vector<float> genAcc = {0.301732, 0.079320, 0.116732, 0.105679};//pre-FSR generator level acceptance
//92X
//8.72492e+06 2.6231e+06
//679707, 1.02256e+06, 920835
const std::vector<float> genAcc = {0.300644, 0.077904, 0.117200, 0.105541};//pre-FSR generator level acceptance

std::vector<float> getMCMuEff(int nPU){
  // for 92X
  if(nPU == 25)      {std::vector<float> v = {0.916812,0.864108,0.988003,0.995065,1,1};return v;}
  else if(nPU == 26) {std::vector<float> v = {0.916368,0.863343,0.988028,0.99503,0.98752,0.996296};return v;}
  else if(nPU == 27) {std::vector<float> v = {0.915927,0.862565,0.98806,0.994997,0.987571,0.996184};return v;}
  else if(nPU == 28) {std::vector<float> v = {0.915486,0.861772,0.9881,0.994966,0.987622,0.99607};return v;}
  else if(nPU == 29) {std::vector<float> v = {0.915043,0.860963,0.988147,0.994937,0.987674,0.995952};return v;}
  else if(nPU == 30) {std::vector<float> v = {0.914596,0.860137,0.988199,0.994909,0.987725,0.995833};return v;}
  else if(nPU == 31) {std::vector<float> v = {0.914143,0.859294,0.988256,0.994884,0.987777,0.995714};return v;}
  else if(nPU == 32) {std::vector<float> v = {0.91368,0.858434,0.988316,0.994861,0.987829,0.995595};return v;}
  else if(nPU == 33) {std::vector<float> v = {0.913207,0.857559,0.988379,0.99484,0.987883,0.995477};return v;}
  else if(nPU == 34) {std::vector<float> v = {0.912722,0.85667,0.988443,0.99482,0.987939,0.995361};return v;}
  else if(nPU == 35) {std::vector<float> v = {0.912226,0.855769,0.988507,0.994802,0.987997,0.995248};return v;}
  else if(nPU == 36) {std::vector<float> v = {0.911717,0.85486,0.988569,0.994785,0.98806,0.995137};return v;}
  else if(nPU == 37) {std::vector<float> v = {0.911198,0.853944,0.988628,0.994767,0.988127,0.99503};return v;}
  else if(nPU == 38) {std::vector<float> v = {0.91067,0.853026,0.988682,0.99475,0.9882,0.994927};return v;}
  else if(nPU == 39) {std::vector<float> v = {0.910135,0.852106,0.98873,0.994731,0.988279,0.994829};return v;}
  else if(nPU == 40) {std::vector<float> v = {0.909594,0.85119,0.988771,0.994711,0.988366,0.994735};return v;}
  else if(nPU == 41) {std::vector<float> v = {0.90905,0.850278,0.988805,0.994689,0.988462,0.994646};return v;}
  else if(nPU == 42) {std::vector<float> v = {0.908506,0.849374,0.988833,0.994665,0.988567,0.994563};return v;}
  else if(nPU == 43) {std::vector<float> v = {0.907962,0.848477,0.988855,0.994639,0.988681,0.994486};return v;}
  else if(nPU == 44) {std::vector<float> v = {0.907422,0.847587,0.988873,0.994612,0.988806,0.994416};return v;}
  else if(nPU == 45) {std::vector<float> v = {0.906886,0.846703,0.988889,0.994583,0.988939,0.994354};return v;}
  else if(nPU == 46) {std::vector<float> v = {0.906357,0.845819,0.988905,0.994553,0.989081,0.9943};return v;}
  else if(nPU == 47) {std::vector<float> v = {0.905835,0.844931,0.988924,0.994521,0.98923,0.994254};return v;}
  else if(nPU == 48) {std::vector<float> v = {0.90532,0.844031,0.988948,0.99449,0.989384,0.994218};return v;}
  else if(nPU == 49) {std::vector<float> v = {0.904813,0.843111,0.988978,0.994458,0.989542,0.994192};return v;}
  else std::invalid_argument("nPU");
}


std::vector<float> getMCZCount(int nPU){
  if(nPU == 25)      {std::vector<float> v = {8.74288e+06,631754,956812,866734}; return v;}
  else if(nPU == 26) {std::vector<float> v = {8.71053e+06,631386,957147,866691}; return v;}
  else if(nPU == 27) {std::vector<float> v = {8.59043e+06,631763,954960,865095}; return v;}
  else if(nPU == 28) {std::vector<float> v = {8.51673e+06,631576,955618,865423}; return v;}
  else if(nPU == 29) {std::vector<float> v = {8.67048e+06,631508,955294,865093}; return v;}
  else if(nPU == 30) {std::vector<float> v = {8.60522e+06,631416,954842,864628}; return v;}
  else if(nPU == 31) {std::vector<float> v = {8.72445e+06,630523,952077,862289}; return v;}
  else if(nPU == 32) {std::vector<float> v = {8.59199e+06,631139,951926,862174}; return v;}
  else if(nPU == 33) {std::vector<float> v = {8.70557e+06,631082,950625,860996}; return v;}
  else if(nPU == 34) {std::vector<float> v = {8.6169e+06,631250,950797,860860}; return v;}
  else if(nPU == 36) {std::vector<float> v = {8.60468e+06,630887,949820,859152}; return v;}
  else if(nPU == 37) {std::vector<float> v = {8.64297e+06,630400,948859,857697}; return v;}
  else if(nPU == 38) {std::vector<float> v = {8.6408e+06,630403,947874,856273}; return v;}
  else if(nPU == 39) {std::vector<float> v = {8.64463e+06,631131,946801,854931}; return v;}
  else if(nPU == 40) {std::vector<float> v = {8.63092e+06,631420,947889,854910}; return v;}
  else if(nPU == 41) {std::vector<float> v = {8.64061e+06,630610,945831,852258}; return v;}
  else if(nPU == 42) {std::vector<float> v = {8.66215e+06,631077,945210,851033}; return v;}
  else if(nPU == 43) {std::vector<float> v = {8.61586e+06,631527,944289,849561}; return v;}
  else if(nPU == 44) {std::vector<float> v = {8.61865e+06,631679,945173,849299}; return v;}
  else if(nPU == 45) {std::vector<float> v = {8.72167e+06,631560,944206,847719}; return v;}
  else if(nPU == 46) {std::vector<float> v = {8.66502e+06,631229,942332,845477}; return v;}
  else if(nPU == 47) {std::vector<float> v = {8.64944e+06,631644,942478,844979}; return v;}
  else if(nPU == 48) {std::vector<float> v = {8.69703e+06,630828,941190,843214}; return v;}
  else if(nPU == 49) {std::vector<float> v = {8.65393e+06,630447,940593,842165}; return v;}
  else std::invalid_argument("nPU");
}

float effFormula(float effHLT1, float effHLT2, float effSIT1, float effSIT2, float effSta1, float effSta2){
  return (1. - (1. - effHLT1)*(1. - effHLT2))* effSIT1*effSIT2 * effSta1*effSta2;
}

float calculateZEfficiency(
  int   dimuRegion,	// 0 for inclusive, 1 for barrel-barrel, 2 for barrel-endcap, 3 for endcap-endcap 
  float meanPileup,
  float dtHLTEffB, float dtHLTEffE, float dtSITEffB, float dtSITEffE, float dtStaEffB, float dtStaEffE
){

  auto vMCZCount = getMCZCount(int(meanPileup));
  auto vMCMuEff  = getMCMuEff(int(meanPileup));

  float nEvtsv = vMCZCount[0];
  float nSelCorrv = 0.;

  if(dimuRegion == 0){

    float dtZEffBB = effFormula( dtHLTEffB, dtHLTEffB, dtSITEffB, dtSITEffB, dtStaEffB, dtStaEffB );
    float dtZEffBE = effFormula( dtHLTEffB, dtHLTEffE, dtSITEffB, dtSITEffE, dtStaEffB, dtStaEffE );
    float dtZEffEE = effFormula( dtHLTEffE, dtHLTEffE, dtSITEffE, dtSITEffE, dtStaEffE, dtStaEffE );

    float mcZEffBB = effFormula( vMCMuEff.at(0), vMCMuEff.at(0), vMCMuEff.at(2), vMCMuEff.at(2), vMCMuEff.at(4), vMCMuEff.at(4) );
    float mcZEffBE = effFormula( vMCMuEff.at(0), vMCMuEff.at(1), vMCMuEff.at(2), vMCMuEff.at(3), vMCMuEff.at(4), vMCMuEff.at(5) );
    float mcZEffEE = effFormula( vMCMuEff.at(1), vMCMuEff.at(1), vMCMuEff.at(3), vMCMuEff.at(3), vMCMuEff.at(5), vMCMuEff.at(5) );

    float corrBB = dtZEffBB/mcZEffBB;
    float corrBE = dtZEffBE/mcZEffBE;
    float corrEE = dtZEffEE/mcZEffEE;

    nSelCorrv = vMCZCount[1] * corrBB + vMCZCount[2] * corrBE + vMCZCount[3] * corrEE;  

  }
  else if(dimuRegion == 1){

    float dtZEffBB = effFormula( dtHLTEffB, dtHLTEffB, dtSITEffB, dtSITEffB, dtStaEffB, dtStaEffB );
    float mcZEffBB = effFormula( vMCMuEff.at(0), vMCMuEff.at(0), vMCMuEff.at(2), vMCMuEff.at(2), vMCMuEff.at(4), vMCMuEff.at(4) );
    float corrBB = dtZEffBB/mcZEffBB;

    nSelCorrv = vMCZCount[1] * corrBB;

  }
  else if(dimuRegion == 2){

    float dtZEffBE = effFormula( dtHLTEffB, dtHLTEffE, dtSITEffB, dtSITEffE, dtStaEffB, dtStaEffE );
    float mcZEffBE = effFormula( vMCMuEff.at(0), vMCMuEff.at(1), vMCMuEff.at(2), vMCMuEff.at(3), vMCMuEff.at(4), vMCMuEff.at(5) );
    Float_t corrBE = dtZEffBE/mcZEffBE;

    nSelCorrv = vMCZCount[2] * corrBE;

  }
  else if(dimuRegion == 3){

    Float_t dtZEffEE = effFormula( dtHLTEffE, dtHLTEffE, dtSITEffE, dtSITEffE, dtStaEffE, dtStaEffE );
    Float_t mcZEffEE = effFormula( vMCMuEff.at(1), vMCMuEff.at(1), vMCMuEff.at(3), vMCMuEff.at(3), vMCMuEff.at(5), vMCMuEff.at(5) );
    Float_t corrEE = dtZEffEE/mcZEffEE;

    nSelCorrv = vMCZCount[3] * corrEE;
  }
  else std::invalid_argument("dimuRegion");


  // compute acceptances
  return (nSelCorrv/nEvtsv)/genAcc[dimuRegion];


  //--------------------------------------------------------------------------------------------------------------
  // Output
  //==============================================================================================================    
  cout << "*" << endl;
  cout << "* SUMMARY" << endl;
  cout << "*--------------------------------------------------" << endl;
  cout << " Z -> mu mu" << endl;
  cout << endl;

  cout << "   ================================================" << endl;
  cout << endl;
  cout << "    *** Acceptance ***" << endl;
  cout << "   AllSFCorrected: " << setw(12) << nSelCorrv   << " / " << nEvtsv << " = " << nSelCorrv/nEvtsv << endl;
  cout << endl;
} 
