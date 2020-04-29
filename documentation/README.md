# Karateseura Verinyrkki ry:n harjoituskanta

## Accounts

Kirjautuminen perustuu tietokantatauluun "Accounts", joka sisältää kirjautumiseen liittyvät nimet, käyttäjätunnukset ja salasanat. Kaikki senseit saavat accounts-tiedot, mutta pääkäyttäjä (tai pääkäyttäjät?) ei ole sensei eikä taulut siten ole sama. Pääkäyttäjän on voitava kirjautua, vaikka kaikki senseit poistettaisiinkin.

Account sisältää INT-tyyppisen ID:n, DATETIME-muodon aikaleimat date_created ja date_modified sekä VARCHAR(144)-tyyppiä olevat name, username ja password. Password on tallennettu tietokantaan tiivisteenä, vaikka tietokannan tyyppi ei sitä tiedäkään.

## Events

Events kuvaa tapahtumia eli harjoitustilanteita. Yksittäinen event on useimmiten yksittäinen karateharjoitus, mutta event voi myös olla kilpailu, näytöstapahtuma tai mitä tahansa muuta seuran järjestämää ohjelmaa.

Events sisältää INT-tyyppisen ID:n sekä TEXT-tyyppiset name, day, time ja info. Name on uniikki harjoituksen nimi, jolla senseit voivat keskenään disponoida seuran harjoituksia vaikka samallekin ajankohtalle eri tatameille ilman, että ID:tä tarvitsee tietää. Day on päivämäärän aikaleima, joka voisi olla myös DATETIME. Sovellus käyttää lokaalisti kuitenkin sqlite3-kantaa PostgreSin sijaan, jolloin DATETIME aiheuttaa ongelmia ja siksi aikaleimana käytetään tekstimuotoista ISO-standardin aikaa. Tietokanta osaa hakea formaattia YYYY-MM-DD olevat aikaleimat kronologisessa järjestyksessä, minkä jälkeen leima muutetaan käyttäjälle näkyvään muotoon dd.mm.yyyy. Time on harjoituksen ajankohta, joka voi olla esim. yksittäinen aikaleima ("19:00"), aikaväli ("19:00–20:15") tai vapaamuotoinen ("potkuharjoituksen jälkeen"). Info on osallistujille tarkoitettua vapaamuotoista tekstiä esim. harjoituksen tatamista tai harjoituksessa tarvittavista varusteista.

## Senseis

Senseis kuvaa harjoituksia vetäviä senseitä. Sensein funktio on näkyä harjoituksen vetäjänä listauksessa, mutta samalla myös yhdistyä Accounts-tauluun kirjautumista varten.

Senseis-taulu sisältää INT-tyyppisen ID:n sekä TEXT-tyyppiset name ja logon. Name on nimi, joka harjoituksen vetäjänä näkyy, ja se kopioidaan Accounts-taulun name-tiedoksi. Logon on uniikki kirjautumistunnus, joka kopioidaan Accounts-tauluun username-tiedoksi, ja jota sensei käyttää kirjautuessaan sisään. Logon ei näy ulkopuolisille.

## Belts

Belts kuvaa vyöarvoja tai muuta vastaavaa harjoitusryhmän tunnistetta.

Belts-taulu sisältää INT-tyyppisen ID:n sekä uniikki TEXT-tyyppisen tiedon Belt, joka siis viittaa vyöarvoon – esim. "6. kyu". Seura voi halutessaan käyttää vyöarvona ryhmiä, kuten "kilparyhmä" tai "juniorit".

## Topics

Topics kuvaa karateharjoitukseen lisättävää teemaa tai muuta aihetta, joka liittyy harjoitustuntiin. Topics on tarkoitettu ryhmiteltäväksi tekijäksi toisin kuin Events-taulun tapahtumien info-kenttä.

Topics-taulu sisältää INT-tyyppisen ID:n sekä uniikin TEXT-tyyppisen tiedon desc, joka on lyhenne sanasta description. Description voi olla esim. karaten perustekniikka ("gyakuzuki"), liikesarja ("pinan godan") tai yleinen aihe ("kehonhuolto").

## Yhdistelmätaulut

Belts-, Senseis- ja Topics-taulut yhdistyvät Events-tauluun many–to–many-suhteessa, koska tapahtumaan voi liittyä yksi tai useampi vyöarvo, sensei ja aihe. Riippuvuus on ratkaistu luomalla suhdetta vastaavat taulut Beltevents, Topicevents ja Senseievents. Kukin taulu sisältää INT-tyyppisen Events-taulun ID:hen viittaavat event_id:t sekä taulukohtaisesti Belts-, Senseis- tai Topics-taulun ID:hen viittaavan INT-tyyppisen belt_id:n, topic_id:n tai sensei_id:n.

## Changelog

### 29.4.2020

Kustomoidut virhekoodit 404, 405 ja 500 on nyt implementoitu. Eventsin muokkaussivulla on autofill kaikkiin vanhoihin tietoihin (tyhjä kohta ei edelleen muuta aiempaa). Eventsin duplikointi on korjattu POST-metodiin aiemmasta GET-metodista. Debug-mode on otettu pois käytöstä.

Käyttöohjetta on päivitetty vastaamaan kaikkia ominaisuuksia, ja käyttäjäkokemuksien toteutuksia on täsmennetty.

### 28.4.2020

Events-lomakkeilla on valmiina nykyinen (uusi) tai aikaisempi (vanha) päiväys. Models-faili on silputtu alikansioihin. Tulevia tapahtumia voi katsoa myös senseikohtaisesti. Tapahtuman voi kahdentaa (lue: toistaa), jolloin sama event toistuu samaan aikaan (time) viikkoa myöhemmin samoilla parametreilla (sensei, aihe, vyö, info).

### 24.4.2020

Asioiden poistaminen vaatii nyt aina 2 klikkausta, jottei vahinkopoistoja tapahdu. Historialliset events-päiväykset ovat jatkossa "tänään". Elementtien margineita säädetty hieman.

### 23.4.2020

Dokumentaation päivittäminen: käyttöohjeen täydennys, käyttötapausten avaaminen, tietokannan kuvaaminen, kehitysideoiden listaus.

### 21.4.2020

Tapahtumia voi tarkastella vyökohtaisesti (14 vrk / tulevaisuus) tai aihealueittain (tulevaisuus). Ulkoasuun lisätty pieniä parannuksia. Asennusohjetta on päivitetty.

### 19.4.2020

Uuden sensein salasana ei enää näy lähdekoodissa raakatekstinä. Sensei näkee etusivulla varoituksen aiheettomien tapahtumien lisäksi ilman harjoituksia olevista vöistä. Vyövaroitus ei enää ota huomioon edellisten päivien tapahtumia varoituksen poistavana tekijänä.

### 16.4.2020

Sisäänkirjautumisen validointirajaa lievennetty, jotta lomake hyväksyy bruteforcella myös varmasti vääriä vaihtoehtoja.

Yli viikkoa aikaisemmin menneet tapahtumat poistetaan automaattisesti tietokannasta, kun kirjautunut käyttäjä avaa Events-sivun.

### 15.4.2020

Käytettävyyttä parannettu: kirjautumaton käyttäjä ei enää näe menneitä tapahtumia Events-listalla. Uusi tapahtuma luodaan nyt yläreunasta, jottei (mahdollisesti) pitkän luettelon loppuun tarvitse kelata. Auth-virheiden ulkonäkö yhtenäistetty flash-muotoiluihin mutta virheet näytetään punaisella.

Sensei voi nyt vaihtaa salasanaansa, pääkäyttäjä 'genki' luonnollisestikaan ei voi.

Käyttöoppaan runko lisätty.

### 14.4.2020

Lisätty positiivisia varoituksia (flash) onnistuneista toimenpiteistä: sisäänkirjautuminen, asioiden luominen, muokkaus, poistaminen.

### 13.4.2020

Auktorisointi lisätty eiliseen kieltoon muokata muiden tietoja (pl. pääkäyttäjä genki). Bootstrap-ulkoasua päivitetty myös tietokannan tietojen muokaamiseen. Tietokannassa oleva Id näkyy jatkossa vain pääkäyttäjä (lue: devaaja) genkille.

Etusivulla näkyy jatkossa seuraavan 7 päivän harjoitukset. Kirjautunut kättäjä näkee lisäksi eventit (myös muut kuin 7 päivän sisällä), joista puuttuu aihe. Varoitus ei kuitenkaan enää huomioi menneitä tapahtumia.

### 12.4.2020

Lisätty validointeja kenttien muokkauksiin ja luomisiin. Tietokantaan ei enää voi syöttää uniikeiksi tarkoitettuja tietoja.

Sensei voi jatkossa muokata vain omia tietojaan, vaikka senseit voivat poistaa toisiaan. Lisäksi superuser 'genki' voi muokata keitä tahansa.

### 2.4.2020

Events, joilla ei ole aihetta, kerätään listana erillisessä yhteenvetokyselyssä, mutta luonnollisesti vain kirjuatuneella käyttäjällä. Tämä näkyy Events-valikossa ylimpänä, kun kirjautunut käyttäjä on Events-valikossa. Jos kaikilla harjoituksilla on vähintään 1 aihe, varoitusilmoitus ei näy. Belts-valikko antaa kirjautuneelle käyttäjälle varoitusilmoituksen ja luettelon, jos jollakin vyöllä ei ole lainkaan harjoituksia. Jos kaikilla ryhmillä on harjoituksia, varoitusta ei näy.

Ulkoasu: Events on valikossa lähimpänä Home-sivua. Sivut päivitetty siniseen ('primary') Bootstrap-tyyliin.

### 1.4.2020

Eventille voi nyt lisätä (ja poistaa) beltejä ja topiceja, jos on kirjautunut. Kirjautumaton käyttäjä näkee Events-listassa myös kullekin harjoitukselle määrätyt vyöt ja aiheet.

Eventin nimi ei jatkossa näy luettelossa, koska nimi on tarkoitettu senseiden sisäiseen yhteydenpitoon: lähinnä keskustelemaan samaan aikaan mahdollisesti olevista eri eventseistä ilman, että id:tä täytyy tietää.

Aikaformaatti muutettu takaisin muotoon YYYY-MM-DD, jotta sorttausta voidaan parannella.

### 31.3.2020

Käyttäjätunnuksen salasana tallennetaan tietokantaan nyt hashina eikä raakatekstinä.

### 30.3.2020

Tietokanta päivitetty viittaamaan ensisijaisesti Herokun Postgresiin.

### 26.3.2020

Auth toimii yhdessä Senseis-taulukon kanssa. Uuden sensein luoinen luo kirjautumistunnukset senseille valitulla logonilla ja oletussalasanalla 'newuser'. Sensein logon on jatkossa aina lowercase ja käyttäjän kirjautumislomake lukee käyttäjätunnuksen jatkossa aina pieninä kirjaimina.

Tapahtumia koskevat yhdistelmätaulut on tehty.