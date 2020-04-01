# Karateseura Verinyrkki ry:n harjoituskanta

## Kirjautuminen

Parametrien luominen ja muokkaaminen edellyttää jatkossa kirjautumista. Kirjautuminen onnistuu käyttäjätunnuksilla ja hashina tallennetuilla salasanoilla. Init luo automaattisesti tunnukset "genki"/"sudo3", jotta ohjelmaan pääsee aina sisälle. Jokaisella senseillä on logon, jolla on salasana "newuser".

## Events

Events kuvaa tapahtumia eli harjoitustilanteita. Harjoitukselle on ominaista uniikki nimi, jotta senseit voivat yksilöidä pitämänsä harjoitustunnit ilman id:tä. Harjoituksella on day eli päivä ja time eli aika, jotka toistaiseksi d.m.yyyy ja näin ollen väärässä järjestyksessä. Info on harjoitukseen liittyvä sensein viesti harjoittelijoille, ja se voi olla esim. tieto käytettävästä tatamista tai harjoitukseen mukaan tarvittavista välineistä.

Eventsiä voi muokata luettelon Edit-painikkeella. Ainoastaan muuttuneet parametrit toteutetaan, eikä tyhjäksi jätettyjä kirjoiteta tietokantaan.

Edit-painikkeesta voi asettaa eventsille sopivan / sopivat vyöt (belts).

## Senseis

Senseis kuvaa harjoituksia vetäviä senseitä. Senseille on ominaista nimi sekä uniikki logon, jolla nimikaimat voidaan erottaa toisistaan käyttämättä tietokannan id:tä. Logon luo käyttäjätunnuksen senseille, joka saa oletuksena salasanan 'newuser'.

Senseitä voidaan muokata luettelon Edit-painikkeesta. Ainoastaan muuttuneet parametrit toteutetaan.

## Belts

Belts kuvaa vyöarvoja tai muuta vastaavaa harjoitusryhmän tunnistetta. Vyöarvolle on ominaista uniikki teksti. Koska vyöarvoja on vain n kappaletta, vyöarvot luultavasti asetetaan tietokantaan ensimmäisellä kaudella ja sen jälkeen jätetään sellaiseksi. Tämän takia vyötä ei voi muokata, vaan mahdollinen kirjoitusvirhe korjataan poistamalla vyö ja lisäämällä uusi.

## Topics

Topics kuvaa karateharjoitukseen lisättävää teemaa tai muuta aihetta, joka liittyy harjoitustuntiin. Tämä voi esim. olla gyakuzuki (vastakäden lyönti), jokin liikesarja tai muu vastaava aihealue, jolla harjoituksia voi indeksoida. Karateka voi arvioida halukkuuttaan osallistua harjoitukseen yhden tai useamman harjoitukseen liittyvän teeman perusteella.

Topic voidaan muokata luettelon Edit-painikkeella, ja ainoastaan muuttunut kuvaus kirjataan tietokantaan.

## Changelog

### 1.4.2020

Eventille voi nyt lisätä (ja poistaa) beltejä, jos on kirjautunut. Kirjautumaton käyttäjä näkee Events-listassa myös kullekin harjoitukselle määrätyt vyöt.

### 31.3.2020

Käyttäjätunnuksen salasana tallennetaan tietokantaan nyt hashina eikä raakatekstinä.

### 30.3.2020

Tietokanta päivitetty viittaamaan ensisijaisesti Herokun Postgresiin.

### 26.3.2020

Auth toimii yhdessä Senseis-taulukon kanssa. Uuden sensein luoinen luo kirjautumistunnukset senseille valitulla logonilla ja oletussalasanalla 'newuser'. Sensein logon on jatkossa aina lowercase ja käyttäjän kirjautumislomake lukee käyttäjätunnuksen jatkossa aina pieninä kirjaimina.

Tapahtumia koskevat yhdistelmätaulut on tehty.