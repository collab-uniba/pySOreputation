/* use stackoverflow_march; */

drop table if exists question;
create table question as select Id 'QId', AcceptedAnswerId 'QAcceptedAnswerId', OwnerUserId 'QOwnerUserId' from posts where posts.PostTypeId = 1 and posts.AcceptedAnswerId is not null;
alter table question add primary key(QId);
alter table question modify QId integer not null auto_increment;

drop table if exists answer;
create table answer as select Id 'AId', OwnerUserId 'AOwnerUserId', CreationDate 'ACreationDate' from posts where PostTypeId = 2;
alter table answer add primary key(AId);
alter table answer modify AId integer not null auto_increment;

drop table if exists question_answer;
create table question_answer as select * from question inner join answer on question.QAcceptedAnswerId = answer.AId;
create index i1question_answer on question_answer (ACreationDate, AOwnerUserId);
create index i2question_answer on question_answer (ACreationDate, QOwnerUserId);

drop table if exists posts_votes1;
create table posts_votes1 as select posts.OwnerUserId, votes.CreationDate from posts inner join votes on posts.Id = votes.PostId where posts.PostTypeId = 1 and votes.VoteTypeId = 2;
create index iposts_votes1 on posts_votes1 (CreationDate, OwnerUserId);

drop table if exists posts_votes2;
create table posts_votes2 as select posts.OwnerUserId, votes.CreationDate from posts inner join votes on posts.Id = votes.PostId where posts.PostTypeId = 1 and votes.VoteTypeId = 3;
create index iposts_votes2 on posts_votes2 (CreationDate, OwnerUserId);

drop table if exists posts_votes3;
create table posts_votes3 as select posts.OwnerUserId, votes.CreationDate from posts inner join votes on posts.Id = votes.PostId where posts.PostTypeId = 2 and votes.VoteTypeId = 2;
create index iposts_votes3 on posts_votes3 (CreationDate, OwnerUserId);

drop table if exists posts_votes4;
create table posts_votes4 as select posts.OwnerUserId, votes.CreationDate from posts inner join votes on posts.Id = votes.PostId where posts.PostTypeId = 2 and votes.VoteTypeId = 3;
create index iposts_votes4 on posts_votes4 (CreationDate, OwnerUserId);
