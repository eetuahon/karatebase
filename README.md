# Karateseura Verinyrkki ry:n harjoituskanta "Karatebase"

Karateseura Verinyrkki ry järjestää karatetunteja, jotka voivat olla suunnattu yhdelle tai useammalle vyöarvolle. Jokaisen tunnin vetää yksi tai useampi sensei. Seinseit voivat luoda tunteja ja niihin liittyviä vöitä, aiheita ja muita senseitä. Karateseuran järjestelmä toimii samalla periaatteella kuin ircin opit eli kaikki ovat vastuussa kaikesta.

Karatebase on tietokantasovellus, joka toteuttaa Verinyrkki ry:n tarvitsemat ja alla luetellut ominaisuudet. Sovelluksen avulla karateseuran senseit voivat tiedottaa jäsenille seuran harjoituksista sekä niiden ajankohdista, vetäjistä, aiheista, vyökoevaatimuksista ja muista lisätiedoista.

Yleisluontoinen dokumentaatio ohjelman osista on tiedostossa [/documentation/README.md](https://github.com/eetuahon/karatebase/tree/master/documentation/README.md), jossa on myös changelog.

Asennusohjeet löytyvät tiedostosta [documentation/installation.md](https://github.com/eetuahon/karatebase/blob/master/documentation/installation.md).

Käyttöohjeet tietokantasovelluksen käyttämiseen ovat tiedostossa [documentation/userguide.md](https://github.com/eetuahon/karatebase/blob/master/documentation/userguide.md)

Kehitysideoita on tiedostossa [documentation/forthefuture.md](https://github.com/eetuahon/karatebase/blob/master/documentation/forthefuture.md).

Ominaisuuksia:
* sensein kirjautuminen
* seisei luo / poistaa karatetuntien ajankohtia
* sensei lisää / poistaa karatetunnille yhden tai useamman aiheen
* sensei lisää / poistaa vyöarvon, aiheen tai sensein
* sensei lisää tunnille yhden / useamman vyöarvon / ryhmän
* seuran jäsen katsoo kirjautumatta itselleen sopivat, lähiaikoina tulevat harjoitukset
* seuran jäsen katsoo kirjautumatta kaikki itselleen sopivat harjoitukset
* seuran jäsen katsoo kirjautumatta tietyn aiheen* kaikki harjoitukset*
* seuran jäsen katsoo kirjautumatta kaikki harjoitukset kaikille

[16.4.2020]* Tarkoituksena oli aluksi selata tapahtumia tietyn päivän perusteella, mutta se vaikuttaa epätodennäköiseltä vaihtoehdolta. Sen sijaan seuran jäsentä saattaisi kiinnostaa tietyn aihealueen harjoitusten tarkastelu sarjassamme, "milloin kannattaa olla paikalla, jos haluaa oppia potkuja".

Tietokantakaavio on [verkkosivulla dbdiagram.io](https://dbdiagram.io/d/5e69648f4495b02c3b88216f) sekä projektin juureen tallennettuna kuvana [dbdiagram.png](https://github.com/eetuahon/karatebase/blob/master/dbdiagram.png)

[SQL-skeemat](https://github.com/eetuahon/karatebase/blob/master/documentation/schemas.md) ja [käyttötapausten toteutukset](https://github.com/eetuahon/karatebase/blob/master/documentation/userstories.md) ovat myös dokumentaatiossa.

Sovellus toimii demona Herokussa projektina [Karatebase-tsoha](http://karatebase-tsoha.herokuapp.com/)
U/P tunnuksilla "genki"/"sudo3" taikka kunkin sensein henkilökohtainen logon + "newuser" (tai vaihdettu salasana)