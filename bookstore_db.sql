use master;
go

drop database if exists bookstore;
go
--drop database bookstore
create database bookstore;
go

use bookstore;

-- -----------------------------------------------------TABLES-----------------------------------------------------------------------------
create table customers(
	customer_id int primary key,
	first_name varchar(255),
	last_name varchar(255),
	gender int check (gender in (0,1)), --0 female 1 male
	dob date,
	email varchar(255),
	phone_number varchar(50),
	address varchar(255),
	staff_id int
);
create table staffs(
	staff_id int primary key,
	name varchar(255),
	account varchar(255),
	password varchar(255),
	role int check (role in (1,2)) --1 sales 2 managers
);

create table books(
	book_id int primary key,
	title varchar(255),
	price float check(price >0),
	publisher_name varchar(255),
	publication_date date,
	quantity int check (quantity>=0) ,
);

create table authors(
  author_id int identity(500,1) primary key,
  author_name varchar(255)
);

create table orders(
  order_id int identity(1,1) primary key,
  customer_id int,
  status int check(status in (0,1,2)) default 0, --0 pending 1 processed 2 canceled
  order_date datetime,
  amount float,
  staff_id int
);

create table orderlines(
  orderline_id int,
  order_id int,
  book_id int,
  quantity int,
  primary key(orderline_id,order_id)
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
alter table orderlines add foreign key (order_id) references orders(order_id) on update cascade on delete cascade;
alter table orderlines add foreign key (book_id) references books(book_id) on update cascade on delete NO ACTION;
-- Foreign Keys in book_author
alter table book_author add foreign key (author_id) references authors(author_id) on update cascade on delete cascade;
alter table book_author add foreign key (book_id) references books(book_id) on update cascade on delete cascade;
-- Foreign Keys in book_genre
alter table book_genre add foreign key (genre_id) references genres(genre_id) on update cascade on delete cascade;
alter table book_genre add foreign key (book_id) references books(book_id) on update cascade on delete cascade;
-- Foreign Keys in customers
alter table customers add foreign key (staff_id) references staffs(staff_id) on update NO ACTION on delete NO ACTION;

-- -----------------------------------------------------INSERT INTO TABLE -----------------------------------------------------------------------------
 
 -- admintrator
insert into adminstrator(account,password) values('admin','123456');
 
 -- authors
INSERT INTO authors (author_name)
VALUES 
('J.K. Rowling'), 
('Stephen King'), 
('George R.R. Martin'), 
('J.R.R. Tolkien'), 
('Agatha Christie'), 
('Dan Brown'), 
('Neil Gaiman'), 
('Harper Lee'), 
('Margaret Atwood'), 
('Philip Pullman'),
('Terry Pratchett'),
('Roald Dahl'),
('Khaled Hosseini'),
('Arthur Conan Doyle'),
('Jane Austen'),
('F. Scott Fitzgerald'),
('Leo Tolstoy'),
('Charles Dickens'),
('Mark Twain'),
('Charlotte Bronte'),
('Emily Bronte'),
('Edgar Allan Poe'),
('Virginia Woolf'),
('Ernest Hemingway'),
('William Faulkner'),
('Gabriel Garcia Marquez'),
('James Joyce'),
('Chinua Achebe'),
('Maya Angelou'),
('Toni Morrison'),
('Zadie Smith'),
('Sylvia Plath'),
('Cormac McCarthy'),
('Don DeLillo'),
('David Foster Wallace'),
('Franz Kafka'),
('Hermann Hesse'),
('Albert Camus'),
('J.D. Salinger'),
('John Steinbeck'),
('Jack Kerouac'),
('Ken Kesey'),
('George Orwell'),
('Aldous Huxley'),
('Ray Bradbury'),
('Isaac Asimov'),
('Ursula K. Le Guin'),
('Octavia Butler'),
('Margaret Peterson Haddix'),
('Veronica Roth'),
('Suzanne Collins'),
('J.K. Rowling'),
('Rick Riordan'),
('J.R.R. Tolkien'),
('George R.R. Martin'),
('Stephenie Meyer'),
('Stephen King'),
('Haruki Murakami'),
('Gillian Flynn'),
('Paula Hawkins'),
('John Grisham'),
('Michael Connelly'),
('Dean Koontz'),
('David Baldacci'),
('James Patterson'),
('Dan Brown'),
('Jo Nesbo'),
('Stieg Larsson'),
('Agatha Christie'),
('Patricia Cornwell'),
('Kathy Reichs'),
('Tess Gerritsen'),
('Mary Higgins Clark'),
('James Rollins'),
('Clive Cussler'),
('Lee Child'),
('Jeffery Deaver'),
('Karin Slaughter'),
('Lisa Gardner'),
('J.D. Robb'),
('Janet Evanovich'),
('Nora Roberts'),
('Kristin Hannah'),
('Jodi Picoult'),
('Nicholas Sparks'),
('John Green'),
('Khaled Hosseini'),
('Mitch Albom'),
('Dan Brown'),
('Neil Gaiman'),
('Markus Zusak'),
('Paolo Coelho'),
('Yann Martel'),
('Graeme Simsion'),
('David Mitchell'),
('Hanya Yanagihara'),
('Anthony Doerr'),
('Donna Tartt'),
('George Saunders'),
('Jeffrey Eugenides'),
('Jonathan Franzen'),
('Junot Diaz'),
('Margaret Atwood'),
('Zadie Smith'),
('Chimamanda Ngozi Adichie'),
('Arundhati Roy'),
('Jhumpa Lahiri'),
('Haruki Murakami'),
('Kazuo Ishiguro'),
('Gabriel Garcia Marquez'),
('Isabel Allende'),
('Laura Esquivel'),
('Julia Alvarez'),
('N.K. Jemisin'),
('Ted Chiang'),
('Stephen Graham Jones'),
('Cixin Liu'),
('Nnedi Okorafor'),
('Marlon James');


 -- books
 -- Insert 1000 random rows of sample data
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
-- 
DECLARE @counter INT = 14
WHILE @counter <= 1000
BEGIN
    INSERT INTO books (book_id, title, price, publisher_name, publication_date, quantity)
    VALUES
        (@counter, 'Title ' + CAST(@counter AS VARCHAR(10)), RAND()*100, 'Publisher ' + CAST(FLOOR(RAND()*10) AS VARCHAR(10)), DATEADD(DAY, -CAST(RAND()*20000 AS INT), GETDATE()), CAST(RAND()*100 AS INT))
    SET @counter = @counter + 1
END;

 -- staffs
insert into staffs(staff_id,name,account,password,role) values(1,'Khanh','staff1','1',2);
insert into staffs(staff_id,name,account,password,role) values(2,'Tu','staff2','1',2);
insert into staffs(staff_id,name,account,password,role) values(3,'Huy','staff3','1',1);

 --book_author
DECLARE @counter INT = 1
WHILE @counter <= 1000
BEGIN
    INSERT INTO book_author (author_id,book_id)
    VALUES
        (CAST((RAND()*(618-500)+500) AS INT),@counter)
    SET @counter = @counter + 1
END;
 --genres
INSERT INTO genres (genre_name) VALUES
('Action'),
('Comedy'),
('Drama'),
('Horror'),
('Romance'),
('Thriller'),
('Science Fiction'),
('Adventure'),
('Animation'),
('Documentary'),
('Fantasy'),
('Mystery'),
('Crime'),
('Historical'),
('Musical'),
('Western'),
('War'),
('Superhero'),
('Spy'),
('Family'),
('Sports'),
('Disaster'),
('Comedy-drama'),
('Satire'),
('Parody'),
('Romantic comedy'),
('Period drama'),
('Teen'),
('Action-adventure'),
('Social drama'),
('Historical drama'),
('Melodrama'),
('Slasher'),
('Supernatural'),
('Epic'),
('Neo-noir'),
('Political drama'),
('Coming-of-age'),
('Heist'),
('Black comedy'),
('Buddy'),
('Chick flick'),
('Caper'),
('Road'),
('Sports drama'),
('Gangster'),
('Space opera'),
('True Crime'),
('Zombie'),
('Apocalyptic');

--book_genre
DECLARE @counter INT = 1
WHILE @counter <= 1000
BEGIN
    INSERT INTO book_genre (genre_id,book_id)
    VALUES
        (CAST((RAND()*(7049-7000)+7000) AS INT),@counter)
    SET @counter = @counter + 1
END;

--customer
INSERT INTO customers (customer_id, first_name, last_name, gender, dob, email, phone_number, address, staff_id) VALUES
(1, 'John', 'Doe', 1, '1990-01-01', 'johndoe@email.com', '123-456-7890', '123 Main St', 1),
(2, 'Jane', 'Doe', 0, '1991-02-02', 'janedoe@email.com', '234-567-8901', '456 Maple Ave', 2),
(3, 'Bob', 'Smith', 1, '1992-03-03', 'bobsmith@email.com', '345-678-9012', '789 Oak Blvd', 3),
(4, 'Sue', 'Johnson', 0, '1993-04-04', 'suejohnson@email.com', '456-789-0123', '1011 Elm St', 1),
(5, 'Mike', 'Jones', 1, '1994-05-05', 'mikejones@email.com', '567-890-1234', '1213 Cedar Ave', 2),
(6, 'Emily', 'Davis', 0, '1995-06-06', 'emilydavis@email.com', '678-901-2345', '1415 Birch Rd', 3),
(7, 'David', 'Wilson', 1, '1996-07-07', 'davidwilson@email.com', '789-012-3456', '1617 Pine St', 1),
(8, 'Amanda', 'Taylor', 0, '1997-08-08', 'amandataylor@email.com', '890-123-4567', '1819 Maple Ave', 2),
(9, 'Brian', 'Miller', 1, '1998-09-09', 'brianmiller@email.com', '901-234-5678', '2021 Oak St', 3),
(10, 'Melissa', 'Anderson', 0, '1999-10-10', 'melissaanderson@email.com', '012-345-6789', '2223 Elm Rd', 1),
(11, 'Tom', 'Brown', 1, '2000-11-11', 'tombrown@email.com', '123-456-7890', '2425 Cedar Ave', 2),
(12, 'Katie', 'Davis', 0, '2001-12-12', 'katiedavis@email.com', '234-567-8901', '2627 Birch Rd', 3),
(13, 'James', 'Johnson', 1, '2002-01-13', 'jamesjohnson@email.com', '345-678-9012', '2829 Pine St', 1),
(14, 'Erica', 'Smith', 0, '2003-02-14', 'ericasmith@email.com', '456-789-0123', '3031 Maple Ave', 2),
(15, 'Ryan', 'Wilson', 1, '2004-03-15', 'ryanwilson@email.com', '567-890-1234', '3233 Oak Blvd', 3),
(16, 'Linda', 'Taylor', 0, '2005-04-16', 'lindataylor@email.com','038-507-1828', 'trai tim em', 2);

-- -----------------------------------------------------SELECT -----------------------------------------------------------------------------

--Login Staffs
go 
create or alter procedure login_staff(@account AS VARCHAR(255), @password AS VARCHAR(255))
as begin
select * from staffs
where account = @account and password = @password;
end;


--search books by title
go
create or alter procedure search_by_title(@title AS VARCHAR(255))
as begin
select *
from books
where title LIKE concat('%',@title,'%');
end;


--search books by title with given author_id
go
create or alter procedure search_by_author(@title AS VARCHAR(255),@author_id AS INT)
as begin
select b.*
from books as b
join book_author as ba on b.book_id = ba.book_id
join authors as a on a.author_id = ba.author_id
where title LIKE concat('%',@title,'%') and a.author_id = @author_id; 
end;


--search books by title with given genre_id
go
create or alter procedure search_by_genre(@title AS VARCHAR(255),@genre_id AS INT)
as begin
select b.*
from books as b
join book_genre as bg on b.book_id = bg.book_id
join genres as g on g.genre_id = bg.genre_id
where title LIKE concat('%',@title,'%') and g.genre_id = @genre_id; 
end;


--search books by publisher_name
go
create or alter procedure search_by_publisher(@publisher_name AS VARCHAR(255))
as begin
select distinct *
from books 
where publisher_name LIKE concat('%',@publisher_name,'%');
end;
-- search genres by genre_name
go
create or alter procedure search_genres_by_genre_name(@genre_name AS VARCHAR(255))
as begin
select *
from genres 
where genre_name LIKE concat('%',@genre_name,'%');
end;
-- search authors by author_name
go
create or alter procedure search_authors_by_author_name(@author_name AS VARCHAR(255))
as begin
select *
from authors 
where author_name LIKE concat('%',@author_name,'%');
end;

-- search customers by phone_number
go
create or alter procedure search_customer_by_phone(@phone_number AS VARCHAR(255))
as begin
select *
from customers 
where phone_number = @phone_number;
end;
-- search customers by email
go
create or alter procedure search_customer_by_email(@email AS VARCHAR(255))
as begin
select *
from customers
where email LIKE concat('%',@email,'%');
end;
--display all books
go
create or alter procedure all_books
as begin
select *
from books
end;

--display all genres
go
create or alter procedure all_genres
as begin 
select *
from genres
end;

--display all authors
go
create or alter procedure all_authors
as begin 
select *
from authors
end;

--display all customers
go
create or alter procedure all_customers
as begin
select *
from customers
end;


--display all staffs 
go
create or alter procedure all_staffs
as begin
select *
from staffs
end;

--display total sales by months
go
create or alter procedure sale_by_month (@month as int, @year as int)
as begin 
select * from orders 
where datepart(year, order_date) = @year and datepart(month, order_date)=@month and status = 1;
end;
--display total sales by days
go
create or alter procedure sale_by_day (@day as int,@month as int, @year as int)
as begin 
select * from orders 
where datepart(year, order_date) = @year and datepart(month, order_date)=@month and datepart(day,order_date)=@day and status = 1;
end;
--display total sales by years
go
create or alter procedure sale_by_year ( @year as int)
as begin 
select * from orders 
where datepart(year, order_date) = @year  and status = 1;
end;


-- -----------------------------------------------------INSERT -----------------------------------------------------------------------------

-- insert new books
go
create or alter procedure insert_books(@book_id AS INT, @title AS VARCHAR(255), @price AS DECIMAL, @publisher_name AS VARCHAR(255), @publication_date AS DATE, @quantity AS INT)
as begin
insert into books(book_id,title,price,publisher_name,publication_date,quantity) values(@book_id, @title, @price, @publisher_name, @publication_date, @quantity);
end;


-- insert new authors
go 
create or alter procedure insert_authors(@author_name AS VARCHAR(255))
as begin
insert into authors(author_name) values (@author_name);
end;


-- insert new genres
go 
create or alter procedure insert_genres(@genre_name AS VARCHAR(255))
as begin
insert into genres(genre_name) values (@genre_name);
end;


-- insert new book_author
go 
create or alter procedure insert_book_author(@author_id AS INT, @book_id AS INT)
as begin
insert into book_author(author_id, book_id) values (@author_id, @book_id);
end;


-- insert new book_genre
go 
create or alter procedure insert_book_genre(@genre_id AS INT, @book_id AS INT)
as begin
insert into book_genre(genre_id, book_id) values (@genre_id, @book_id);
end;


--insert new customer
go
create or alter procedure insert_customers(@customer_id AS INT, @first_name AS varchar(255), @last_name as varchar(255), @gender as int, @dob as date, @email as varchar(255), @phone_number as varchar(255), @address as varchar(255), @staff_id as int)
as begin 
insert into customers(customer_id, first_name, last_name, gender, dob, email, phone_number, address, staff_id) values (@customer_id, @first_name, @last_name, @gender, @dob, @email, @phone_number, @address, @staff_id);
end;


--insert new orders
go 
create or alter procedure insert_orders(@customer_id as int, @order_date as datetime, @staff_id as int)
as begin  
insert into orders(customer_id, order_date, staff_id) values (@customer_id, @order_date, @staff_id);
end;


--insert new orderlines
go 
create or alter procedure insert_orderlines(@orderline_id as int, @order_id as int, @book_id as int, @quantity as int)
as begin
if (@quantity <= (select quantity from books where book_id = @book_id))
begin
insert into orderlines(orderline_id, order_id, book_id, quantity) values (@orderline_id, @order_id, @book_id, @quantity);

update orders
set amount = (select sum(ol.quantity*b.price) from orderlines as ol join books as b on b.book_id = ol.book_id where order_id = @order_id group by order_id)  
where order_id = @order_id;
end
else
begin
select ERROR_MESSAGE();
end;
end;


--insert new staffs
go
create or alter procedure insert_staffs(@staff_id as int, @name as varchar(255), @account as varchar(255), @password as varchar(255), @role as int)
as begin 
insert into staffs(staff_id, name, account, password, role) values (@staff_id, @name, @account, @password, @role);
end;


-- -----------------------------------------------------UPDATE -----------------------------------------------------------------------------

--update status of orders
--create a temporary view
go
create view book_in_orderlines
as
select books.*, orderlines.quantity as order_quantity, orderlines.order_id
from books
join orderlines on books.book_id = orderlines.book_id;

--update status by order_id
go
create or alter procedure update_status_by_orderid (@order_id as int, @new_status as int)
as begin  
update orders
set status = @new_status
where order_id = @order_id;
end;

--trigger auto update
go
CREATE OR ALTER TRIGGER update_book_in_orderlines
ON orders
AFTER UPDATE
AS
BEGIN
  -- Check if the status column has been updated
  IF UPDATE(status)
  BEGIN
    -- Get the old and new values of the status column
    DECLARE @old_status int, @new_status int;
    SELECT @old_status = status FROM deleted;
    SELECT @new_status = status FROM inserted;

    -- Check if the new status is 1
    IF @new_status = 1
    BEGIN
      -- Update the book_in_orderlines table
      UPDATE book_in_orderlines
      SET quantity = quantity - order_quantity
      WHERE order_id IN (SELECT order_id FROM inserted);
    END
    -- Check if the new status is 2
    ELSE IF @new_status = 2
    BEGIN
      -- Delete the order from the orders table
      DELETE FROM orders WHERE order_id IN (SELECT order_id FROM inserted);
    END
  END
END;

-- -----------------------------------------------------DELETE -----------------------------------------------------------------------------

-- delete books by book_id
go
create or alter procedure delete_books(@book_id as int)
as begin 
delete from books where book_id = @book_id;
end;

-- delete authors by author_id
go
create or alter procedure delete_authors(@author_id as int)
as begin 
delete from authors where author_id = @author_id;
end;

-- delete genres by genre_id 
go 
create or alter procedure delete_genres(@genre_id as int)
as begin
delete from genres where genre_id = @genre_id;
end;

-- delete orderlines 
go 
create or alter procedure delete_orderlines(@order_id as int, @orderline_id as int)
as begin
delete from orderlines where orderline_id = @orderline_id and order_id = @order_id;
update orders set amount = (select sum(ol.quantity*b.price) from orderlines as ol join books as b on b.book_id = ol.book_id where order_id = @order_id group by order_id)
where order_id = @order_id; 
end;
-- delete staffs
go
create or alter procedure delete_staffs(@staff_id as int)
as begin
delete from staffs where staff_id = @staff_id;
end;

-- index
 
-- -----------------------------------------------------INDEX ------------------------------------------------------------------------

create index book_title_index on books(title);
create index publisher_name_index on books(publisher_name);