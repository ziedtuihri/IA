create database employee
CREATE TABLE employee2 (
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   gender  INT              NOT NULL,
   salary  VARCHAR(20)        NOT NULL,
   department   VARCHAR (50)    NOT NULL,       
   PRIMARY KEY (ID)
);

CREATE TABLE Company2 (
   ID_E   INT              NOT NULL,
   NAME_E VARCHAR (20)     NOT NULL,
   PRIMARY KEY (ID_E)
);


INSERT INTO employee2 values 
(1,'zied tuihri',500,'salah','departe 1'),
(2,'zied tuihri',600,'salah','departe 2'),
(3,'zied tuihri',700,'salah','departe 3'),
(4,'zied tuihri',800,'salah','departe 4')






