# ChessMateIn3
A projekt egy matt 3 lépésben feladvány megoldót valósít meg. 

A projektet készítették:
- Csabai Balázs
- Ujvári Máté
- Vizsy Domonkos

## Futtatás
A program futtatásának elkezdéséhez egy FEN bemenetre van szükség. Az alábbi linken matt 3 lépésben feladványok találhatóak: https://wtharvey.com/m8n3.txt.

<p align="center">
<img width=200 src="./pictures/FEN.png">
</p>

A kiválasztott FEN bemásolása után, ha a feladvány nem megoldható kiírja, hogy "Nincsen matt 3 lépésből". (A fenti linken minden feladvány megoldható 3 lépésben, nemleges válaszért a https://wtharvey.com/m8n4.txt linken találhatóak 4 lépésben megoldható feladványok.)

<p align="center">
<img width=200 src="./pictures/ne.png">
</p>

Ha a feladvány megoldható, megad egy lehetséges első lépést, majd az ellenfél válaszát kéri, megjeleníti a jelenlegi állást a sakktáblán és kiírja a lehetséges összes lépését az ellenfélnek. Így megadhatjuk akár a saját lépésünket is a feladványban szereplő lépés mellett. 

<p align="center">
<img width=500 src="./pictures/m1.png">
</p>

Ha véletlen nem szabályos lépést adunk meg, akkor új bemenetet kér a program: 

<p align="center">
<img width=200 src="./pictures/illegal_move.png">
</p>

Ha jó a megadott lépése az ellenfélnek, akkor ezt is megjeleníti:

<p align="center">
<img width=350 src="./pictures/m2.png">
</p>

Majd a program megadja a választott lépésre a matthoz vezető következő lehetséges lépést és újból az ellenfél lépését kéri. 

<p align="center">
<img width=350 src="./pictures/m3.png">
</p>

Az ellenfél következő lépése: 

<p align="center">
<img width=350 src="./pictures/m4.png">
</p>

Végezetül a matt:

<p align="center">
<img width=350 src="./pictures/m5.png">
</p>
