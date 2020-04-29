# Karatebase-tietokantasovellusten käyttötapaukset queryina

Sovellukselle luvatut ominaisuudet näyttävät konepellin alla seuraavilta:

## "senseinä haluan kirjautua"

Kirjautuminen toimii flask_loginin alla siten, että käyttäjän syöttämää käyttäjänimeä etsitään tietokannasta. Jos käyttäjä löytyy, tarkastetaan, että syötetty salasana vastaa kannassa tallennettua tiivistettä.

## "seiseinä haluan luoda / poistaa karatetuntien ajankohtia, ryhmiä, aiheita tai senseitä"

Tapahtuman lisääminen tapahtuu luomalla Events-olio `e = Events(form.name.data, d, form.time.data, form.info.data)` jossa d on form.day.data tai tämä päivä muodossa yyyy-dd-mm ja form.name, form.time ja form.info ovat lomakkeesta saadut tiedot koskien tapahtuman nimeä, aikaa ja lisätietoja.
`db.session().add(e)`
`db.session().commit()`

Poistaminen tapahtuu etsimällä Events-olio id:n perusteella `e = Events.query.get(id)` ja poistamalla se.
`db.session().delete(e)`
`db.session().commit()`

Valittu olio on tarpeen mukaan Events-olio, Belts-olio (parametrina belt), Topics-olio (parametrina desc) tai Senseis-olio (parametreina name ja logon).

## "seuran jäsenä haluan katsoa kirjautumatta itselleni sopivat, lähiaikoina tulevat harjoitukset"

Etusivu näyttää seuraavan 7 päivän aikana tulevat tapahtumat perustuen Flask-SQLAlchemyn kutsuun `Events.query.order_by(Events.day, Events.time).filter(Events.day >= today, Events.day < week).all()`, jossa today on kyseinen päivä string-muodossa yyyy-mm-dd ja week viikon päästä tuleva päivä.

Jos käyttäjä haluaa rajata itselleen soveltuvia harjoituksia vyöllä, kutsu on `Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today, Events.day < week).all()`

Näissä today vastaa tämän päivän aikaleimaa ja week viikon kuluttua olevaa aikaleimaa tietokannan tallennusmuodoissa yyyy-mm-dd. Belt on Belt-olio, joka voidaan etsiä esim. ID:llä, kuten Belts-sivun filtteröintitaulukossa on tehty.

Itselle soveltuvat, lähiaikoina piettävät harjoitukset näkyvät Belts-sivulta vyökohtaisesti. Jokaisen vyön kohdalta sopivat harjoitukset näyttävä linkki myös kertoo, montako soveltuvaa harjoitusta on tarjolla. Lukumäärä saadaan manuaalisesti SQL-kyselyllä `SELECT COUNT(BE.event_id) FROM Beltevents BE LEFT JOIN Events E ON BE.event_id = E.id WHERE BE.belt_id = :a AND E.day >= :b AND E.day < :c`, jossa :a korvataan halutun vyön ID:llä, :b tämän päivän aikaleimalla (edellä today) ja :c viikon kuluttua olevalla aikaleimalla (week).

## "seuran jäsenä haluan katsoa kirjautumatta kaikki itselleni sopivat harjoitukset"

Flask-SQLAlchemyn kutsu ei rajaa tapahtumista ainoastaan vyöarvon `Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today).all()` eikä enää viikon sisällä olevaa rajoitetta käytetä, kuten edellä. "Kaikki" on käyttäjän kannalta helpoin ymmärtää tulevaisuuteen, joten menneet tapahtumat on kuitenkin rajattava pois.

## "seuran jäsenä haluan katsoa kirjautumatta tietyn aiheen kaikki harjoitukset"

Tietyn aiheen harjoitukset voidaan katsoa Topics-sivulla valitsemalla halutun aiheen kohdalta tulevien tapahtumien näkymä. Aiheen kohdalla on linkki, joka luo Topics-olion topic, jolla tapahtumia filtteröidään, kuten yllä.

`Events.query.order_by(Events.day, Events.time).filter(Events.topics.contains(topic), Events.day >= today).all()`

## "seuran jäsenä haluan katsoa kirjautumatta kaikki harjoitukset kaikille"

Kaikki harjoitukset tarkoittavat tässä yhteydessä tänään ja myöhemmin tulevia harjoituksia, ja seuran jäsen pääsee tähän Events-valikosta. Tällöin näytetään kysely `Events.query.order_by(Events.day, Events.time).filter(Events.day >= today).all()`, jolloin ainoastaan menneet tapahtumat filtteröidään pois.