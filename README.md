# National Service Delivery Analytics

## About

We processed text data extracted from public sites — specifically, sites hosting discussions of National Service (NS) related services offered by Singapore's Ministry of Defence. Examples of such services include NSmen's experiences at medical check-ups and NSF's experiences in camps. 

Online reviews and forums contain substantial opinions from the NS community, so we were interested in analysing their sentiments towards these services. We visualised our insights in a dashboard app for our clients, who were project managers at the Defence Science and Technology Agency.

## Process and tools used

It was an end-to-end project lasting five months, so my teammates — [@VibhuKrovvidi](https://github.com/VibhuKrovvidi), [@zexuann](https://github.com/zexuann), [@kaieekkoh](https://github.com/kaieekkoh) — and I conducted meetings with our clients and supervisors, found relevant data sources and experimented with NLP techniques until we found what worked for our goal.

This table summarises the stages and techniques we tried. Not all stages made it into our final system design, which we charted [here](docs/system-design.jpeg).

| Stage | Details |
| -- | -- |
| Web scraping | Scraped text data from related [Reddit](https://www.reddit.com/r/nationalservicesg) and [HardwareZone](https://forums.hardwarezone.com.sg/forums/national-service-knowledge-base.162/) forums, as well as [Google Reviews](https://www.google.com/maps/place/Central+Manpower+Base+(CMPB)/@1.2802004,103.8129319,17z/data=!4m7!3m6!1s0x31da1bd0af54732f:0x9c274decbab4e599!8m2!3d1.2802117!4d103.8145684!9m1!1b1) of camps and recruitment offices, using Reddit's APIs and `Selenium`. |
| Feature extraction | Tokenisation, stop word removal and part-of-speech tagging with `NLTK`. |
| Sentiment analysis | Conducted at feature- and sentence-levels using `Stanza`. Accounted for Singlish terms in text data by scraping an online dictionary and averaging the sentiment scores of each term's definitions. |
| Topic modelling | Filtered irrelevant extracted features: first by heuristics (e.g. implementing TF-IDF cut-off values), then by topic modelling to combine similar features together. Evaluated word embedding models (`Word2Vec` and `GloVe`) and clustering techniques (e.g. k-means, affinity propagation), trained on a subset of our collected data to account for the Singlish lexicon. Looked at the effectiveness of pretrained vectors as well. |
| Entity extraction | Topic modelling didn't return useful results and we realised we couldn't expect statistical models to perform given our limited dataset; we relied on rule-based matching using `spaCy` to target the entities we want after discussion with our clients instead. |
| Dashboarding | Implemented the above processes in the backend of a dashboard developed with `Flask`, using visualisations created with `ChartJS` and [displaCy](https://explosion.ai/demos/displacy). | 
