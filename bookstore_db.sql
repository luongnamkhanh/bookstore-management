create database bookstore;
use bookstore;
SELECT *
FROM INFORMATION_SCHEMA.TABLES;
 --drop database bookstore;
-- -----------------------------------------------------TABLES-----------------------------------------------------------------------------
create table customers(
	customer_id int primary key,
	first_name varchar(255),
	last_name varchar(255),
	gender int check (gender in (0,1)),
	dob date,
	email varchar(255),
	phone_number varchar(50),
	address varchar(255)
);
create table staffs(
	staff_id int primary key,
	name varchar(255),
	account varchar(255),
	password varchar(255),
	role int check (role in (1,2))
);

create table books(
	book_id int primary key,
	title varchar(255),
	price decimal,
	publisher_name varchar(255),
	publication_date date,
	quantity int check(quantity >0),
);

create table authors(
  author_id int identity(500,1) primary key,
  author_name varchar(255)
);

create table orders(
  order_id int identity(1,1) primary key,
  customer_id int,
  status int check(status in (0,1,2)),
  order_date date,
  amount decimal,
  staff_id int
);
create table orderlines(
  orderline_id int,
  order_id int,
  book_id int,
  quantity int,
);
create table book_author(
  author_id int,
  book_id int,
  primary key(author_id,book_id)
);
create table book_genre(
  genre_id int,
  book_id int,
  primary key(genre_id,book_id)
);
create table genres(
  genre_id int identity(7000,1) primary key,
  genre_name varchar(255)
);
create table adminstrator(
  account varchar(255),
  password varchar(255)
);
-- -----------------------------------------------------ALTER TABLE -----------------------------------------------------------------------------


-- -----------------------------------------------------FOREIGN KEYS-----------------------------------------------------------------------------
 
-- Foreign Keys in orders 
alter table orders add foreign key (customer_id) references customers(customer_id); 
alter table orders add foreign key (staff_id) references staffs(staff_id); 
-- Foreign Keys in orderlines
alter table orderlines add foreign key (order_id) references orders(order_id);
alter table orderlines add foreign key (book_id) references books(book_id);
-- Foreign Keys in book_author
alter table book_author add foreign key (author_id) references authors(author_id);
alter table book_author add foreign key (book_id) references books(book_id);
-- Foreign Keys in book_genre
alter table book_genre add foreign key (genre_id) references genres(genre_id);
alter table book_genre add foreign key (book_id) references books(book_id);

-- -----------------------------------------------------INSERT INTO TABLE -----------------------------------------------------------------------------
 
 -- admintrator
insert into adminstrator(account,password) values('admin','123456');
 
 -- authors
insert into Authors(author_name) values('Robert Stevenson');
insert into Authors(author_name) values('Jon Krakauer');
insert into Authors(author_name) values('John Green');
insert into Authors(author_name) values('Colleen Hover');
insert into Authors(author_name) values('Jane Austen');
insert into Authors(author_name) values('Gillian Flynn');
insert into Authors(author_name) values('Peter Straub');

 -- books
insert into books(book_id,title,price,publisher_name,publication_date,quantity) values(1,'Treasure Island',345.12,'Kim Dong','1990-12-12',10);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(2,'Life of Pi',295.56,'Nha Nam','2022-01-12',10);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(3,'Black House',800.36,'Tre','2002-09-06',5);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(4,'Ghost Story',499.2,'Lao Dong','2012-02-09',9);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(5,'The Grownup',99.47,'Tong Hop','2004-08-12',10);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(6,'Gone Girl',367.45,'Kim Dong','2018-01-01',10);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(7,'Paper Towns',199.12,'Lao Dong','2008-01-01',199);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(8,'Fault in our Stars',687.96,'Nha Nam','2012-02-09',687);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(9,'Layla',1598.23,'Tre','2020-02-07',98);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(10,'Ugly Love',350.19,'Nha Nam','2014-09-21',50);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(11,'Pride & Prejudice',295.78,'Kim Dong','1813-08-12',95);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(12,'Mysteries of Udolpho',795.67,'Tre','1993-05-20',5);
insert into Books(book_id,title,price,publisher_name,publication_date,quantity) values(13,'Into Thin Air',568.91,'Tre','1964-12-12',68);

 -- staffs
insert into staffs(staff_id,name,account,password,role) values(1,'Khanh','staff1','1',2);
insert into staffs(staff_id,name,account,password,role) values(2,'Tu','staff2','1',2);
insert into staffs(staff_id,name,account,password,role) values(3,'Huy','staff3','1',1);

 -- book_author
insert into book_author(author_id,book_id) values(500,1);
insert into book_author(author_id,book_id) values(500,2);
insert into book_author(author_id,book_id) values(506,3);
insert into book_author(author_id,book_id) values(506,4);
insert into book_author(author_id,book_id) values(505,5);
insert into book_author(author_id,book_id) values(505,6);
insert into book_author(author_id,book_id) values(502,7);
insert into book_author(author_id,book_id) values(502,8);
insert into book_author(author_id,book_id) values(503,9);
insert into book_author(author_id,book_id) values(503,10);
insert into book_author(author_id,book_id) values(504,11);
insert into book_author(author_id,book_id) values(504,12);
insert into book_author(author_id,book_id) values(501,13);
insert into book_author(author_id,book_id) values(502,13);

 --genres
insert into genres(genre_name) values('Adventure');
insert into genres(genre_name) values('Horror');
insert into genres(genre_name) values('Mystery');
insert into genres(genre_name) values('Romance');

 --book_genre
insert into book_genre(genre_id,book_id) values(7000,1);
insert into book_genre(genre_id,book_id) values(7000,2);
insert into book_genre(genre_id,book_id) values(7001,3);
insert into book_genre(genre_id,book_id) values(7001,4);
insert into book_genre(genre_id,book_id) values(7001,5);
insert into book_genre(genre_id,book_id) values(7002,6);
insert into book_genre(genre_id,book_id) values(7002,7);
insert into book_genre(genre_id,book_id) values(7003,8);
insert into book_genre(genre_id,book_id) values(7002,9);
insert into book_genre(genre_id,book_id) values(7003,10);
insert into book_genre(genre_id,book_id) values(7003,11);
insert into book_genre(genre_id,book_id) values(7001,12);
insert into book_genre(genre_id,book_id) values(7002,12);
insert into book_genre(genre_id,book_id) values(7000,13);

-- -----------------------------------------------------SELECT -----------------------------------------------------------------------------


-- -----------------------------------------------------INSERT -----------------------------------------------------------------------------


-- -----------------------------------------------------UPDATE -----------------------------------------------------------------------------

-- -----------------------------------------------------DELETE -----------------------------------------------------------------------------

-- -----------------------------------------------------TRANSACTION ------------------------------------------------------------------------
