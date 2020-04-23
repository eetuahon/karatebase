# Karatebase-tietokantasovellusten käyttötapaukset queryina

Sovellukselle luvatut ominaisuudet näyttävät konepellin alla seuraavilta:

## "senseinä haluan kirjautua"

Kirjautuminen toimii flask_loginin alla siten, että käyttäjän syöttämää käyttäjänimeä etsitään tietokannasta. Jos käyttäjä löytyy, tarkastetaan, että syötetty salasana vastaa kannassa tallennettua tiivistettä.

## "seiseinä haluan luoda / poistaa karatetuntien ajankohtia, ryhmiä, aiheita tai senseitä"

Lisääminen
`Events(form.name.data, d, form.time.data, form.info.data)` jossa d on form.day.data tai tämä päivä muodossa yyyy-dd-mm.
`db.session().add(e)`
`db.session().commit()`

Poistaminen
`t = Events.query.get(id)`
`db.session().delete(t)`
`db.session().commit()`

Valittu olio on tarpeen mukaan Events-olio, Belts-olio, Topics-olio tai Senseis-olio.

## "seuran jäsenä haluan katsoa kirjautumatta itselleni sopivat, lähiaikoina tulevat harjoitukset"

Etusivu näyttää seuraavan 7 päivän aikana tulevat tapahtumat perustuen Flask-SQLAlchemyn kutsuun `Events.query.order_by(Events.day, Events.time).filter(Events.day >= today, Events.day < week).all()`, jossa today on kyseinen päivä string-muodossa yyyy-mm-dd ja week viikon päästä tuleva päivä.

Jos käyttäjä haluaa rajata itselleen soveltuvia harjoituksia vyöllä, kutsu on `Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today, Events.day < week).all()`

## "seuran jäsenä haluan katsoa kirjautumatta kaikki itselleni sopivat harjoitukset"

Flask-SQLAlchemyn kutsu ei rajaa tapahtumista ainoastaan vyöarvon `Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today).all()`

## "seuran jäsenä haluan katsoa kirjautumatta tietyn aiheen kaikki harjoitukset"

`Events.query.order_by(Events.day, Events.time).filter(Events.topics.contains(topic), Events.day >= today).all()`

## "seuran jäsenä haluan katsoa kirjautumatta kaikki harjoitukset kaikille"

Kaikki harjoitukset tarkoittavat tässä yhteydessä tänään ja myöhemmin tulevia harjoituksia, ja seuran jäsen pääsee tähän Events-valikosta. Tällöin näytetään kysely `Events.query.order_by(Events.day, Events.time).filter(Events.day >= today).all()`.