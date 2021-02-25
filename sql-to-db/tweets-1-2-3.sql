--import new files
source SQL/10-11-20-tweets.sql
source SQL/10-11-20-media.sql
source SQL/10-11-20-words.sql



drop table tweets1, tweets2, tweets3;
create table tweets1 as select * from tweets left join media on tweets.id = media.tweet_id;
create table tweets2 as select * from tweets1 left join vietas on tweets1.geo = vietas.nosaukums;
ALTER TABLE tweets2 ORDER BY created_at ASC;
create table tweets3 as select * from tweets2 t left join (SELECT distinct(tvits) FROM words o) AS o ON o.tvits = t.id;
