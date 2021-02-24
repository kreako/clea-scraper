# clea-scraper

## What ?

This is a scraper of recipes from clea website. This produces a data directory where recipes are stored by date, in markdown format.

Now you can easily search for your favorite "brioche" recipe :

```
$ fd brioche <data-dir>
2005/12/petits-pains-brioches-a-la-farine-complete.md
2006/06/gateau-brioche-a-la-fleur-doranger.md
2006/09/brioche-farcie-a-la-provencale.md
2006/12/brioche-farcie-au-chou-rouge-et-aux-marrons.md
2007/02/briochettes-a-la-puree-damande-et-a-la-bergamote.md
2007/02/chaussons-brioches-aux-pommes.md
2007/04/briochettes-a-lhuile-dolive.md
2009/01/brioche-de-noel.md
2009/03/brioche-toute-simple.md
2009/04/brioche-aux-myrtilles.md
2009/09/brioche-a-la-farine-complete.md
2009/11/tourte-briochee-aux-fruits-de-mer.md
2010/11/brioche-a-la-courge-et-aux-epices.md
2011/01/brioche-roulee-au-the-matcha.md
2011/02/brioche-au-pesto-amandes-et-pistaches.md
2011/05/briochettes-au-fromage-de-chevre-au-thym-et-au-miel.md
2012/05/croque-brioche-aux-petits-pois-et-au-brie-de-chevre.md
2013/10/brioche-roulee-a-la-confiture-de-noix.md
2013/10/brioches-suedoises-cannelle-cardamome.md
2014/11/brioche-vegan-a-la-courge-et-a-la-cannelle.md
2016/02/briochettes-sans-gluten-a-lhuile-dolive.md
2016/08/tarte-briochee-aux-mirabelles-et-aux-noisettes.md
2018/03/croque-brioche-avocat-et-tapenade.md
2019/06/brioche-mi-complete.md
2019/10/brioche-potimarron-cacahuete.md
```


## How to use

Clone this repository.

Create a new virtualenv :

```
$ python3 -m venv env
```

Activate it :
```
$ . env/bin/activate
```

Install required dependencies :

```
$ pip install -r requirements.txt
```

Launch the scraper :
```
$ scrapy crawl cleascraper
```
