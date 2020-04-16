# Karatebase-tietokannan käyttöohje

## Karateseuran toimintojen selaaminen

Seuraavan viikon aikana tapahtuvat karatetapahtumat näkyvät sovelluksen etusivulta. Jos etusivulta on poistuttu, etusivulle pääsee takaisin valitsemalla yläreunan navigointivalikosta "Karatebase" tai "Front page".

Kaikki tulevat karatetapahtumat näkyvät valitsemalla yläreunan navigointivalikosta "Events", jolloin tapahtumat näkyvät ensisijaisesti päivämäärän ja toissijaisesti ajan perusteella kronologisesti järjestettynä. Jos käyttäjä ei ole kirjautunut, valikossa näkyy vain tulevat tapahtumat. Sensei näkee tietokannassa myös menneet tapahtumat.

Käyttäjä voi tarkastella karateseuran sensei-luetteloa valitsemalla yläreunan navigointivalikosta "Senseis". Sisään kirjautunut sensei näkee luettelossa nimien lisäksi kunkin yksilöllisen sisäänkirjautumistunnuksen.

Käyttäjä voi tarkastella tapahtumiin liittyviä vyöarvoja (lue: harjoitusryhmiä) valitsemalla yläreunan navigointivalikosta "Belts".

Käyttäjä voi tarkastella seuran harjoituksissa käsiteltäviä aiheita valitsemalla yläreunan navigointivalikosta "Topics".

## Käyttäjän (sensei) toimenpiteet

### Kirjautuminen

Sensei voi kirjautua sisään valitsemalla yläreunan navigointivalikosta "Log in". Kirjautuminen onnistuu täyttämällä avautuvan kirjautumislomakkeen joko pääkäyttäjän käyttäjätunnuksella ja salasanalla taikka kullekin senseille yksilöllisellä sensein login-tunnuksella ja tähän liittyvällä salasanalla.

Alla lueteltavat käyttäjän toimenpiteet edellyttävät myös ilman erillistä mainintaa, että käyttäjä on kirjautunut onnistuneesti sisään.

### Tapahtumien toimenpiteet

#### Uuden tapahtuman luominen

Uusi tapahtuma luodaan tapahtumaluettelosta ("Events") valitsemalla tapahtumataulukon yläreunasta "Add an event", jolloin käyttäjä saa lomakeen tapahtumien luomiseksi. Uudelle tapahtumalle syötetään lomakkeessa:
1. Name on tapahtumalle tarkoitettu uniikki nimi, joka on 3–30 merkkiä pitkä. Nimi on tapahtumalle pakollinen, ja sen tarkoituksena on yksilöidä tapahtumat senseiden muussa keskustelussa. Senseit voivat esimerkiksi sopia samaan aikaan eri tatameilla järjestettävien tapahtumien järjestämisestä käyttämällä tapahtuman nimeä.
2. Day on tapahtumalle suunniteltu päivämäärä. Päivämäärä on annettava muodossa dd.mm.yyyy eli suomalaisen käytännön mukaisesti. Jos syötettä ei voida tulkita yksiselitteiseksi päivämääräksi, tapahtuma luodaan tapahtumaan tänään.
3. Time on tapahtumalle suunniteltu ajankohta, joka voi olla 3–30 merkkiä pitkä. Tietoa ei validoida testein, joten ajankohta voi olla karateseuran käytännön mukaisesti esim. "19:00", "19:00–20:15" tai "tapahtuman x jälkeen". Tekstinä ilmoitetuissa ajoissa on otettava huomioon, että harjoitukset eivät välttämättä listaudu kronologisesti näkymässä.
4. Info on tapahtumalle tarkoitettu lisätieto, joka voi olla esimerkiksi "harjoituksissa tarvitaan nyrkkeilyhanskat" tai paikkatieto "tatami 2".

### Senseiden toimenpiteet

#### Uuden sensein luominen tietokantaan

#### Sensein muokkaaminen

#### Sensein poistaminen

### Vyöarvojen toimenpiteet

### Aihealueiden toimenpiteet

### Ylläpitäjän varoitukset

Karateseuran toiminnan kannalta on suotavaa, että jokaisella tulevalla tapahtumalla on vähintään yksi aihe. Lisäksi on suotavaa, että jokaiselle harjoitusryhmälle on vähintään yksi harjoitus.

### Salaasnan vaihtaminen

Käyttäjä (muu kuin sensei-luettelosta riippumaton pääkäyttäjä) voi vaihtaa salasanansa yläreunan navigointivalikon oikeasta reunasta valitsemalla "Change password". Tällöin aukeaa lomake, johon täytyy syöttää vanha salasana sekä uusi salasana kahdesti kirjoitusvirheen välttämiseksi.

Uuden salasanan on oltava vähintään 8 ja enintään 64 merkkiä pitkä. Kun salasana on vaihdettu onnistuneesti, käyttäjä saa ilmoituksen onnistuneesta salasanan vaihtamisesta.

### Kirjautuminen ulos

Käyttäjä voi kirjautua ulos painamalla yläreunan navigointivalikon oikeasta reunasta "Log out".