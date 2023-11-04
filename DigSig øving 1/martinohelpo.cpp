#include <iostream>



int x = 0;  
//Hva skal funksjon gjøre
//FØrst skru på lys 4 og 5
strip.setPixelColor(4,strip.colo(0,255,0));
strip.setPixelColor(5,strip.colo(0,255,0));
for(int i = 0; i <= 4; i++){
    //Nå vente litt tid så skru på 3 og 6
    x = x + 1;
    strip.setPixelColor(4-x,strip.color(0,255,0));
     strip.setPixelColor(5+x,strip.color(0,255,0));
     delay(500);
}