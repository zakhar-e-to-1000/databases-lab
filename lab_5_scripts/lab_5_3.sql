delimiter $$
drop procedure random_split$$
create procedure random_split()
begin
	declare name_1 varchar(255) default "";
	declare name_2 varchar(255) default "";
    declare done int default 0;
    declare id_T int;
    declare name_T varchar(255);
    declare rand_name varchar(255) default "";
    declare curr cursor for select * from region;
    declare continue handler for not found set done=1;
	set name_1 = CONCAT("region_1_",UNIX_TIMESTAMP());
	set name_2 = CONCAT("region_2_",UNIX_TIMESTAMP());
    set @insert_query_1 = CONCAT("create table ", name_1, " like region");
    set @insert_query_2 = CONCAT("create table ", name_2, " like region");
	prepare stmt from @insert_query_1;
    execute stmt;
    deallocate prepare stmt;
	prepare stmt from @insert_query_2;
    execute stmt;
    deallocate prepare stmt;
    open curr;
    myLoop: LOOP
		fetch curr into id_T, name_T;
        if done=true then leave myLoop;
        end if;
        if rand()>0.5 then SET rand_name = name_1;
        else set rand_name = name_2;
        end if;
        set @rand_query = CONCAT("INSERT INTO ", rand_name, "(id, name) values (?, ?)");
        set @p1 = id_T;
        set @p2 = name_T;
        prepare stmt from @rand_query;
        execute stmt using @p1, @p2;
        DEALLOCATE prepare stmt;
    end LOOP;
    CLOSE curr;
end $$
DELIMITER ;
call random_split();
SHOW TABLES;