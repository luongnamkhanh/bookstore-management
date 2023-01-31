use master;
go
create database bookstore
go

use bookstore;

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
	price decimal check(price >0),
	publisher_name varchar(255),
	publication_date date,
	quantity int check(quantity>0),
);

create table authors(
  author_id int identity(500,1) primary key,
  author_name varchar(255)
);

create table orders(
  order_id int identity(1,1) primary key,
  customer_id int,
  status int check(status in (0,1,2)),
  order_date datetime,
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
alter table orders add foreign key (customer_id) references customers(customer_id) on update cascade on delete NO ACTION; 
alter table orders add foreign key (staff_id) references staffs(staff_id) on update cascade on delete NO ACTION; 
-- Foreign Keys in orderlines
alter table orderlines add foreign key (order_id) references orders(order_id) on update cascade on delete NO ACTION;
alter table orderlines add foreign key (book_id) references books(book_id) on update cascade on delete NO ACTION;
-- Foreign Keys in book_author
alter table book_author add foreign key (author_id) references authors(author_id) on update cascade on delete cascade;
alter table book_author add foreign key (book_id) references books(book_id) on update cascade on delete cascade;
-- Foreign Keys in book_genre
alter table book_genre add foreign key (genre_id) references genres(genre_id) on update cascade on delete cascade;
alter table book_genre add foreign key (book_id) references books(book_id) on update cascade on delete cascade;

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

--Login Staffs
go 
create procedure login_staff(@account AS VARCHAR(255), @password AS VARCHAR(255))
as begin
select * from staffs
where account = @account and password = @password;
end;


--search books by title
go
create procedure search_by_title(@title AS VARCHAR(255))
as begin
select *
from books
where title LIKE @title;
end;


--search books by author_name
go
create procedure search_by_author(@author_name AS VARCHAR(255))
as begin
select b.*
from books as b
join book_author as ba on b.book_id = ba.book_id
join authors as a on a.author_id = ba.author_id
where author_name LIKE @author_name; 
end;


--search books by genre_name
go
create procedure search_by_genre(@genre_name AS VARCHAR(255))
as begin
select b.*
from books as b
join book_genre as bg on b.book_id = bg.book_id
join genres as g on g.genre_id = bg.genre_id
where genre_name LIKE @genre_name; 
end;


--search books by publisher_name
go
create procedure search_by_publisher(@publisher_name AS VARCHAR(255))
as begin
select distinct *
from books 
where publisher_name LIKE @publisher_name;
end;


--display all books
go
create procedure all_books
as begin
select *
from books
end;

--display all genres
go
create procedure all_genres
as begin 
select *
from genres
end;

--display all authors
go
create procedure all_authors
as begin 
select *
from authors
end;

--display all customers
go
create procedure all_customers
as begin
select *
from customers
end;


--display all staffs 
go
create procedure all_staffs
as begin
select *
from staffs
end;

--display total sales by months
go
create procedure sale_by_month (@month as int, @year as int)
as begin 
select * from orders 
where datepart(year, order_date) = @year and datepart(month, order_date)=@month;
end;



-- -----------------------------------------------------INSERT -----------------------------------------------------------------------------

-- insert new books
go
create procedure insert_books(@book_id AS INT, @title AS VARCHAR(255), @price AS DECIMAL, @publisher_name AS VARCHAR(255), @publication_date AS DATE, @quantity AS INT)
as begin
insert into books(book_id,title,price,publisher_name,publication_date,quantity) values(@book_id, @title, @price, @publisher_name, @publication_date, @quantity);
end;


-- insert new authors
go 
create procedure insert_authors(@author_name AS VARCHAR(255))
as begin
insert into authors(author_name) values (@author_name);
end;


-- insert new genres
go 
create procedure insert_genres(@genre_name AS VARCHAR(255))
as begin
insert into genres(genre_name) values (@genre_name);
end;


-- insert new book_author
go 
create procedure insert_book_author(@author_id AS INT, @book_id AS INT)
as begin
insert into book_author(author_id, book_id) values (@author_id, @book_id);
end;


-- insert new book_genre
go 
create procedure insert_book_genre(@genre_id AS INT, @book_id AS INT)
as begin
insert into book_genre(genre_id, book_id) values (@genre_id, @book_id);
end;


--insert new customer
go
create procedure insert_customers(@customer_id AS INT, @first_name AS varchar(255), @last_name as varchar(255), @gender as int, @dob as date, @email as varchar(255), @phone_number as varchar(255), @address as varchar(255))
as begin 
insert into customers(customer_id, first_name, last_name, gender, dob, email, phone_number, address) values (@customer_id, @first_name, @last_name, @gender, @dob, @email, @phone_number, @address);
end;


--insert new orders
go 
create procedure insert_orders(@customer_id as int, @status as int, @order_date as datetime, @staff_id as int)
as begin  
insert into orders(customer_id, status, order_date, staff_id) values (@customer_id, @status, @order_date, @staff_id);
end;


--insert new orderlines
go 
create procedure insert_orderlines(@orderline_id as int, @order_id as int, @book_id as int, @quantity as int)
as begin
insert into orderlines(orderline_id, order_id, book_id, quantity) values (@orderline_id, @order_id, @book_id, @quantity);
-- instantly update orders_amount
update orders
set amount = (select sum(ol.quantity*b.price) from orderlines as ol join books as b on b.book_id = ol.book_id where order_id = @order_id group by order_id)  
where order_id = @order_id;
end;


--insert new staffs
go
create procedure insert_staffs(@staff_id as int, @name as varchar(255), @account as varchar(255), @password as varchar(255), @role as int)
as begin 
insert into staffs(staff_id, name, account, password, role) values (@staff_id, @name, @account, @password, @role);
end;


-- -----------------------------------------------------UPDATE -----------------------------------------------------------------------------

--update book_price by book_title 
go
create procedure update_book_price (@book_title as varchar(255), @new_price as decimal)
as begin
if (@new_price > 0) begin update books set price=@new_price where title LIKE @book_title end;
end;

--update book_quantity by book_id in orderlines (mannual)
go 
create procedure update_book_quantity(@book_id as int, @new_quantity as int)
as begin
if(@new_quantity >=0) 
begin
update books
set quantity = @new_quantity
where book_id = @book_id;
end;
end;

-- -----------------------------------------------------DELETE -----------------------------------------------------------------------------

-- delete books by book_id
go
create procedure delete_books(@book_id as int)
as begin 
delete from books where book_id = @book_id;
end;

-- delete authors by author_id
go
create procedure delete_authors(@author_id as int)
as begin 
delete from authors where author_id = @author_id;
end;

-- delete genres by genre_id 
go 
create procedure delete_genres(@genre_id as int)
as begin
delete from genres where genre_id = @genre_id;
end;

-- -----------------------------------------------------TRANSACTION ------------------------------------------------------------------------
