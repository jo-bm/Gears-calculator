#include <iostream>

using namespace std;


int main(){

    cout<<"this is a gears calculator,\nusing the formulas: pitch=teeth/diameter & pitch*diameter=teeth\n";

    cout<<"enter radius for gear 1: "; float radius_1;
    cin>>radius_1;
    cout<<"enter teeth number for gear 1: "; float teeth_1;
    cin>>teeth_1;
    cout<<"enter radius for gear 2: "; float radius_2;
    cin>>radius_2;


    float diameter=radius_1*2;
    float pitch=teeth_1/diameter;

    cout<<"Gear 1\n"<<"Radius: "<<radius_1<<"\nDiameter: "<<radius_1*2<<"\nTeeth: "<<teeth_1<<"\nPitch: "<<pitch<<"\n~~~\n\n\n:";

    cout<<"Gear 2\n"<<"Radius: "<<radius_2<<"\nDiameter: "<<radius_2*2<<"\nTeeth: "<<pitch*radius_2*2<<"\nPitch: "<<pitch<<"\n~~~\n\n\n:";
    string temp;
    cin>>temp;


    return 0;

}





