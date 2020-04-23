# Karatebase-tietokannan käyttöohje

## Karateseuran toimintojen selaaminen

Seuraavan viikon aikana tapahtuvat karatetapahtumat näkyvät sovelluksen etusivulta. Jos etusivulta on poistuttu, etusivulle pääsee takaisin valitsemalla yläreunan navigointivalikosta "Karatebase" tai "Front page".

Kaikki tulevat karatetapahtumat näkyvät valitsemalla yläreunan navigointivalikosta "Events", jolloin tapahtumat näkyvät ensisijaisesti päivämäärän ja toissijaisesti ajan perusteella kronologisesti järjestettynä. Jos käyttäjä ei ole kirjautunut, valikossa näkyy vain tulevat tapahtumat. Sensei näkee tietokannassa myös menneet tapahtumat.

Käyttäjä voi tarkastella karateseuran sensei-luetteloa valitsemalla yläreunan navigointivalikosta "Senseis". Sisään kirjautunut sensei näkee luettelossa nimien lisäksi kunkin yksilöllisen sisäänkirjautumistunnuksen.

Käyttäjä voi tarkastella tapahtumiin liittyviä vyöarvoja (lue: harjoitusryhmiä) valitsemalla yläreunan navigointivalikosta "Belts". Luettelosta voi tarkastella vyöhön liittyviä, seuraavan 14 päivän kuluessa tulevaia harjoituksia valitsemalla "The next 14 days for [beltin nimi]". Luettelosta voi myös valita vyöhön liittyvät kaikki tulevat harjoitukset valitsemalla "All events for [beltin nimi]". Lisäksi näytetään vyöhön liittyvien tapahtuvien lukumäärä. Jos vyöhön liittyviä tapahtumia ei ole, linkki muuttuu inaktiiviseksi ja kertoo, ettei tapahtumia ole.

Käyttäjä voi tarkastella seuran harjoituksissa käsiteltäviä aiheita valitsemalla yläreunan navigointivalikosta "Topics". Luettelosta voi tarkastella kunkin aihealueen tulevia harjoituksia valitsemalla "Events with [aiheen nimi]". Lisäksi näytetään aiheeseen liittyvien tapahtumien lukumäärä. Jos tulevia taphtumia aiheesta ei ole tulossa, linkki on inaktiivinen ja kertoo, ettei tapahtumia ole.

## Käyttäjän (sensei) toimenpiteet

### Kirjautuminen

Sensei voi kirjautua sisään valitsemalla yläreunan navigointivalikosta "Log in". Kirjautuminen onnistuu täyttämällä avautuvan kirjautumislomakkeen joko pääkäyttäjän käyttäjätunnuksella ja salasanalla taikka kullekin senseille yksilöllisellä sensein login-tunnuksella ja tähän liittyvällä salasanalla.

Sensei tarvitsee kirjautumiseen käyttäjätunnukset, jotka joku toinen sensei tai pääkäyttäjä voi tehdä. Kun senseille luodaan uusi käyttäjä, sensein salasana on "newuser", joka on syytä vaihtaa mahdollisimman pian.

Alla lueteltavat käyttäjän toimenpiteet edellyttävät myös ilman erillistä mainintaa, että käyttäjä on kirjautunut onnistuneesti sisään.

### Tapahtumien toimenpiteet

#### Uuden tapahtuman luominen

Uusi tapahtuma luodaan tapahtumaluettelosta ("Events") valitsemalla tapahtumataulukon yläreunasta "Add an event", jolloin käyttäjä saa lomakeen tapahtumien luomiseksi. Uudelle tapahtumalle syötetään lomakkeessa:
1. Name on tapahtumalle tarkoitettu uniikki nimi, joka on 3–30 merkkiä pitkä. Nimi on tapahtumalle pakollinen, ja sen tarkoituksena on yksilöidä tapahtumat senseiden muussa keskustelussa. Senseit voivat esimerkiksi sopia samaan aikaan eri tatameilla järjestettävien tapahtumien järjestämisestä käyttämällä tapahtuman nimeä. Name näkyy ainoastaan kirjautuneelle käyttäjälle.
2. Day on tapahtumalle suunniteltu päivämäärä. Päivämäärä on annettava muodossa dd.mm.yyyy eli suomalaisen käytännön mukaisesti. Jos syötettä ei voida tulkita yksiselitteiseksi päivämääräksi, tapahtuma luodaan tapahtumaan tänään.
3. Time on tapahtumalle suunniteltu ajankohta, joka voi olla 3–30 merkkiä pitkä. Tietoa ei validoida testein, joten ajankohta voi olla karateseuran käytännön mukaisesti esim. "19:00", "19:00–20:15" tai "venyttelyharjoituksen jälkeen". Tekstinä ilmoitetuissa ajoissa on otettava huomioon, että harjoitukset eivät välttämättä listaudu kronologisesti näkymässä.
4. Info on tapahtumalle tarkoitettu lisätieto, joka voi olla esimerkiksi "harjoituksissa tarvitaan nyrkkeilyhanskat" tai paikkatieto "tatami 2".

#### Tapahtuman muokkaaminen ja senseiden / vöiden / aiheiden asettamienn

Tapahtumien muokkaaminen on mahdollista valitsemalla tapahtumalistasta "Edit" muokattavaksi halutun tapahtuman kohdalta. Senseit, vyöt ja aiheet ovat tapahtuman tiedoissa allekkain taulukoituina siten, että tapahtumaan liittyvät asiat ovat vasemmalla ja loput oikealla.

Sensei, vyö tai aihe lisätään valitsemalla Senseis-, Belts- tai Topics-kohdan oikeasta reunasta inaktiivinen ja aktiiviseksi haluttu asia painamalla "Add [asia]". Muutosta ei tarvitse tallentaa enää erikseen.

Sensei, vyö tai aihe poistetaan valitsemalla Senseis-, Belts- tai Topics-kohdan vasemmasta reunasta aktiivinen ja inaktiiviseksi haluttu asia painamalla "Remove [asia]". Muutosta ei tarvitse tallentaa enää erikseen.

Tapahtuman nimeä, päivää, aikaa tai infoa voi muokata Edit-sivun alareunan Edit-taulukossa. Muutettujen tietojen on täytettävä alkuperäisten tietojen vaatimukset. Taulukkoon ei tarvitse täyttää niitä tietoja, joita ei haluta muokattavaksi. Kun muutetut tiedot ovat valmiina, käyttäjän on painettava "Change".

#### Tapahtuman poistaminen

Tapahtuman poistaminen tapahtuu samalta sivulta, josta tapahtumaa voi muokata. Tällöin alareunasta valitaan "Delete".

Yli viikon vanhat tapahtumat poistetaan automaattisesti, kun kirjautunut käyttäjä lataa Events-sivun. Poisto edellyttää kirjautumista, jotta useat seuran jäsenet eivät turhaan pyri poistamaan monta kertaa saman päivän aikana vanhoja tapahtumia.

### Senseiden toimenpiteet

#### Uuden sensein luominen tietokantaan

Uusi sensei luodaan valitsemalla ylärivin navigointivalikosta "Senseis" ja tämän jälkeen "Add a sensei" taulukon yläreunasta. Uuden sensein tiedot syötetään lomakkeelle:
1. Name on sensein näkyvä nimi, jolla tämä näkyy luettelossa ja itselleen liitetyissä tapahtumissa. Nimen ei tarvitse olla uniikki, vaan seurassa voi olla samannimisiä senseitä.
2. Logon on kirjautumistunnus, joka näkyy vain kirjautuneelle käyttäjälle ja jota sensei käyttää kirjautuessaan sisään. Logonin täytyy olla uniikki.

Sekä nimen että kirjautumistunnuksen on oltava 3–15 merkkiä. Kirjautumistunnus muutetaan automaattisesti pieniksi kirjaimiksi.

#### Sensein muokkaaminen

Senseitä voi muokata Sensei-luettelosta valitsemalla halutun sensein kohdalta "Edit". Pääkäyttäjä voi muokata kaikkia senseitä, mutta sensei voi muokata voin omia tietojaan (pl. poistaminen).

Lomakkeella voi syöttää uuden sensein nimen ja logon-tiedon, ja tiedot tallenetaan painamalla "Change". Ainoastaan muuttunut tieto täytyy kirjoittaa lomakkeeseen.

#### Sensein poistaminen

Sensei poistetaan Sensei-luettelosta valitsemalla sensein kohdalta "Edit". Tämän jälkeen aukeaa valikko, josta sensei saadaan poistettua valitsemalla "Delete".

### Vyöarvojen toimenpiteet

#### Vyöarvon luominen

Uusi vyöarvo luodaan valitsemalla ylärivin navigointivalikosta "Belts" ja tämän jälkeen "Add a belt". Vyölle annetaan taulukossa sisältö kohtaan "Belt / group", johon syötetään 3–15 merkkiä pitkä selite vyölle, esim. "6. kyu". Tieto tallennettaan valitsemalla "Add a new belt".

#### Vyöarvon muokkaus ja deletointi

Karaten vyöarvot ovat stabiileja, joten luultavasti kaikki variaatiot vyöarvoista lienevät tietokannassa muutaman ensimmäisen käyttökerran jälkeen. Siksi vyötä ei voi muokata, vaan mahdollinen kirjoitusvirhe korjataan poistamalla vyö ja luomalla uusi.

Vyö poistetaan valitsemalla vyöluettelosta "Delete", minkä jälkeen aukeaa vielä vyön tiedot sisältävä sivu. Sivulta valitaan "Delete", jolloin vyö poistetaan tietokannasta.

### Aihealueiden toimenpiteet

#### Aihealueen lisääminen

Aihealue lisätään valitsemalla yläreunan navigointivalikosta "Topics" ja tämän jälkeen "Add a topic". Tällöin aukeaa lomake, johon uuden aiheen kuvauksen voi syöttää. Aiheen on oltava 3–30 merkkiä pitkä. Uusi aihe tallennetaan valitsemalla "Add a new topic".

#### Aihealueen muokkaaminen ja poistaminen

Aihealueen muokkaaminen ja poistaminen tapahtuvat valitsemalla aihealuiden luettelosta halutun aiheen kohdalta "Edit".

Muutettu kuvaus, jonka on vastattava alkuperäisen aiheen ehtoja, voidaan syöttää kohtaan "New description" ja tallentaa valitsemalla "Change". Aihe voidaan poistaa valitsemalla "Delete", jolloin aihe poistetaan tietokannasta.

### Ylläpitäjän varoitukset

Karateseuran toiminnan kannalta on suotavaa, että jokaisella tulevalla tapahtumalla on vähintään yksi aihe. Lisäksi on suotavaa, että jokaiselle harjoitusryhmälle on vähintään yksi harjoitus. Jos näin ei ole, sisäänkirjautunut käyttäjä saa etusivulla varoituksen. Lisäksi aiheettomista tapahtumista varoitetaan Events-sivulla ja harjoituksettomista vyöarvoista Belts-sivulla.

### Salasanan vaihtaminen

Käyttäjä (muu kuin sensei-luettelosta riippumaton pääkäyttäjä) voi vaihtaa salasanansa yläreunan navigointivalikon oikeasta reunasta valitsemalla "Change password". Tällöin aukeaa lomake, johon täytyy syöttää vanha salasana sekä uusi salasana kahdesti kirjoitusvirheen välttämiseksi.

Uuden salasanan on oltava vähintään 8 ja enintään 64 merkkiä pitkä. Kun salasana on vaihdettu onnistuneesti, käyttäjä saa ilmoituksen onnistuneesta salasanan vaihtamisesta.

### Kirjautuminen ulos

Käyttäjä voi kirjautua ulos painamalla yläreunan navigointivalikon oikeasta reunasta "Log out".