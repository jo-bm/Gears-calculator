#include <iostream>
#include <math.h>
using namespace std;


int main(){

    cout<<"this is a worm gear calculator,\nusing the formula: Diameter=Pitch*Number of teeth/Pi\n\n\n";

    cout<<"what is the pitch?: "; float pitch;
    cin>>pitch;
    cout<<"what is the number of teeth?: "; float teeth;
    cin>>teeth;

    cout<<"diameter is: "<<pitch*teeth/M_PI;

    string temp;
    cin>>temp;

    return 0;

}


