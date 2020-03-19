# Karateseura Verinyrkki ry:n harjoituskanta

## Events

Events kuvaa tapahtumia eli harjoitustilanteita. Harjoitukselle on ominaista uniikki nimi, jotta senseit voivat yksilöidä pitämänsä harjoitustunnit ilman id:tä. Harjoituksella on day eli päivä ja time eli aika, jotka toistaiseksi ovat vapaamuotoisia (formaatti implementoidaan myöhemmin). Info on harjoitukseen liittyvä sensein viesti harjoittelijoille, ja se voi olla esim. tieto käytettävästä tatamista tai harjoitukseen mukaan tarvittavista välineistä.

Eventsiä voi muokata luettelon Edit-painikkeella. Ainoastaan muuttuneet parametrit toteutetaan, eikä tyhjäksi jätettyjä kirjoiteta tietokantaan.

## Senseis

Senseis kuvaa harjoituksia vetäviä senseitä. Senseille on ominaista nimi sekä uniikki logon, jolla nimikaimat voidaan erottaa toisistaan käyttämättä tietokannan id:tä. Logon implementoidaan mahdollisesti myöhemmin sisäänkirjaukseen.

Senseitä voidaan muokata luettelon Edit-painikkeesta. Ainoastaan muuttuneet parametrit toteutetaan.

## Belts

Belts kuvaa vyöarvoja tai muuta vastaavaa harjoitusryhmän tunnistetta. Vyöarvolle on ominaista uniikki teksti. Koska vyöarvoja on vain n kappaletta, vyöarvot luultavasti asetetaan tietokantaan ensimmäisellä kaudella ja sen jälkeen jätetään sellaiseksi. Tämän takia vyötä ei voi muokata, vaan mahdollinen kirjoitusvirhe korjataan poistamalla vyö ja lisäämällä uusi.

## Topics

Topics kuvaa karateharjoitukseen lisättävää teemaa tai muuta aihetta, joka liittyy harjoitustuntiin. Tämä voi esim. olla gyakuzuki (vastakäden lyönti), jokin liikesarja tai muu vastaava aihealue, jolla harjoituksia voi indeksoida. Karateka voi arvioida halukkuuttaan osallistua harjoitukseen yhden tai useamman harjoitukseen liittyvän teeman perusteella.

Topic voidaan muokata luettelon Edit-painikkeella, ja ainoastaan muuttunut kuvaus kirjataan tietokantaan.