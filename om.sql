create table  staff (
    s_id int primary key,
    s_name varchar(20) not null,
    s_address varchar(50) not null,
    s_role varchar(20) not null
);
describe staff;

create table stadium(
    st_name varchar(50) primary key,
    st_location varchar(100),
    st_capacity int,
    st_dimensions varchar(100),
    s_id int,
    foreign key (s_id) references staff(s_id)
);
describe stadium;

create table teams(
    t_name varchar(50) primary key not null,
    t_strength int,
    t_captain varchar(50),
    t_performance varchar(100)
);
describe teams;

insert into teams values("Patna Pirates",8,"Om Mishra","Excellent");
select * from teams;

create table player(
    p_id int primary key not null,
    p_name varchar(20),
    p_gender varchar(20),
    p_statistics  varchar(100),
    p_team varchar(50),
    s_id int,
    t_name  varchar(20),
    foreign key (s_id) references staff(s_id),
    foreign key (t_name) references teams(t_name)
);
describe player;

alter table player drop column p_gender;
describe player;

alter table teams modify column t_strength varchar(50);
describe teams;

create table sponsors(
  sp_name varchar(20) primary key not null,
  sp_ROI varchar(10),
  sp_income int,
  sp_amount int
);
describe sponsors;

insert into sponsors values("TATA","3%","200000","10000");
select * from sponsors;

create table audience(
  a_seatno int primary key not null,
  a_preference varchar(30),
  a_age int,
  a_gender varchar(20)
);
describe audience;

insert into audience values(201,"Lower",50,"FeMale");
select * from audience;

create table prizes(
  pr_name varchar(20) primary key not null,
  pr_amount int,
  pr_recipient varchar(20),
  pr_type varchar(20),
  sp_name varchar(20),
  foreign key (sp_name) references sponsors(sp_name)
);
describe prizes;

create table equipments(
  e_name varchar(20) primary key,
  e_material varchar(20),
  e_type varchar(20),
  e_price int
);
describe equipments;

create table matches(
  m_number int primary key,
  m_time int,
  m_winner varchar(20),
  m_venue varchar(50),
  st_name varchar(20),
  foreign key (st_name) references stadium(st_name)
);
describe matches;

create table batsman(
  p_id int primary key,
  b_style varchar(50),
  b_position varchar(20),
  b_average int,
  foreign key (p_id) references player(p_id)
);
describe batsman;

create table bowler(
  p_id int primary key,
  bo_style varchar(50),
  bo_wicketstaken int,
  bo_average int,
  foreign key (p_id) references player(p_id)
);
describe bowler;

create table allrounder(
  p_id int primary key,
  al_impactpoints int,
  al_type  varchar(20),
  al_rating int,
  foreign key (p_id) references player(p_id)
);
describe allrounder;

insert into staff values(101,"Nihal","Mira Road","Trainer");
insert into staff values(102,"Parth","Thane","Coach");
select * from staff;

