# Karateseura Verinyrkki ry:n harjoituskanta

Tarkempaa dokumentaatiota ohjelman toimivuudesta päivitetään osissa kansioon [/documentation](https://github.com/eetuahon/karatebase/tree/master/documentation/README.md).

Asennusohjeet löytyvät tiedostosta [documentation/installation.md](https://github.com/eetuahon/karatebase/blob/master/documentation/installation.md).

Käyttöohjeet tietokantasovelluksen käyttämiseen ovat tiedostossa [documentation/userguide.md](https://github.com/eetuahon/karatebase/blob/master/documentation/userguide.md)

Karateseura Verinyrkki ry järjestää karatetunteja, jotka voivat olla suunnattu yhdelle tai useammalle vyöarvolle. Jokaisen tunnin vetää yksi tai useampi sensei. Seinseit voivat luoda tunteja ja niihin liittyviä vöitä, aiheita ja muita senseitä. Karateseuran järjestelmä toimii samalla periaatteella kuin ircin opit eli kaikki ovat vastuussa kaikesta.

Ominaisuuksia:
* sensein kirjautuminen [x]
* seisei luo / poistaa karatetuntien ajankohtia [x]
* sensei lisää / poistaa karatetunnille yhden tai useamman aiheen [x]
* sensei lisää / poistaa vyöarvon, aiheen tai sensein [x]
* sensei lisää tunnille yhden / useamman vyöarvon / ryhmän [x]
* seuran jäsen katsoo kirjautumatta itselleen sopivat, lähiaikoina tulevat harjoitukset [ ]
* seuran jäsen katsoo kirjautumatta kaikki itselleen sopivat harjoitukset [ ]
* seuran jäsen katsoo kirjautumatta tietyn ~~päivän~~ _aiheen_ kaikki harjoitukset [ ]*
* seuran jäsen katsoo kirjautumatta kaikki harjoitukset kaikille [x]

[16.4.2020]* triviaalin päivän harjoitusten selaaminen vaikuttaa epätodennäköiseltä vaihtoehdolta. Sen sijaan seuran jäsentä saattaisi kiinnostaa tietyn aihealueen harjoitusten tarkastelu sarjassamme, "milloin kannattaa olla paikalla, jos haluaa oppia potkuja".

[Tietokantakaavio](https://dbdiagram.io/d/5e69648f4495b02c3b88216f) tai kuvana edellä [dbdiagram.png](https://github.com/eetuahon/karatebase/blob/master/dbdiagram.png)

Herokussa [Karatebase-tsoha](http://karatebase-tsoha.herokuapp.com/)
U/P tunnuksilla "genki"/"sudo3" taikka sensein henkilökohtainen logon + "newuser" (tai vaihdettu salasana)