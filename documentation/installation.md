# Asennusohje

Sys.req:
- Python3
- pip (python)
- venv (pythonin kirjasto)

1. Tallenna tiedostot ohjelmalle varattuun kansioon, esim. [purkamalla ZIP-tiedosto](https://github.com/eetuahon/karatebase/archive/master.zip) uudeksi kansioksi.
2. Asenna virtuaaliympäristö projektin sisältävään kansioon komennolla `python3 -m venv venv` ja käynnistä se komennolla `source venv/bin/activate`.
3. Asenna tarvittavat riippuvuudet komennolla `pip install -r requirements.txt`.
4. Käynnistä ohjelma ajamalla `python3 run.py`, jonka jälkeen ohjelma on päällä ja käytettävissä osoitteessa `http://localhost:5000/`.

### Sovelluksen siirtäminen pilveen

Sovellus täytyy siirtää pilvipalveluun, jos sitä ei ajeta palvelinkäyttöön soveltuvalta koneelta.

Tarvitaan Heroku CLI tai vastaava.

1. Luo Herokuun (tai muuhun palveluun) komennolla `heroku create [haluamasi projektin nimi]`. Jos haluat sovelluksen muuhun pilveen kuin Herokuun, tee tarvittavat muutokset [application/__init__.py](https://github.com/eetuahon/karatebase/blob/master/application/__init__.py#L12) riville 12.
2. Luo kansioon tarvittava git-sisältö `git init`.
2b. Lisää venv-kansio, tietokantatiedostot yms. sälä tiedostoksi `.gitignore`, jos et halua niitä pilveen.
3. Lisää Heroku-projektin git-osoite versionhallintaan `git remote add heroku https://git.heroku.com/[projektisi nimi].git`.
4. Tee gitin kautta commit valitsemalla kaiken kansiosta `git add .` ja paketoimalla commit `git commit -m "First commit to Heroku"`.
5. Puske commit Herokuun komennolla `git push heroku master`.