use lab_1;

delimiter $$
drop procedure quick_insert_location $$
create procedure quick_insert_location(location_name varchar(50), region_name varchar(50), la double, lo double)
begin
	declare region_id int default null;
    select r.id into region_id from region r where r.name=region_name;
    insert into location (name, region_id, latitude, longitude) values (location_name, region_id, 0, 0);
    select * from location where id=last_insert_id();
end $$
call quick_insert_location("Test proc", 'Name_1', 0, 0)$$
delimiter $$
drop function getRiverStat $$
create function getRiverStat(stat_type varchar(3))
returns double deterministic
begin
	declare result double;
    select case
    when stat_type="MIN" then MIN(r.length)
    when stat_type="MAX" then MAX(r.length)
    when stat_type="AVG" then AVG(r.length)
    when stat_type="SUM" then SUM(r.length)
    else null
    end
    from river r
    into result;
    return result;
end $$


DELIMITER $$
drop procedure GetRiverStats $$
CREATE PROCEDURE GetRiverStats(stat_type VARCHAR(3))
BEGIN
    SELECT getRiverStat(stat_type) AS BalanceStat;
END $$

DELIMITER ;
call GetRiverStats("MIN");


DELIMITER $$
drop procedure InsertNoName$$
create procedure InsertNoName()
begin
	declare i int default 1;
    inner_loop: LOOP
		if i > 10 then leave inner_loop; end if;
        insert into region(name) values (concat("Name_", i));
        set i = i+1;
	end loop inner_loop;
end$$
DELIMITER ;
call InsertNoName();
select * from region;
delete from region where name like("Name_%");

delimiter $$
drop procedure convinient_insert $$
create procedure convinient_insert(river_name varchar(50), location_name varchar(50))
begin
	declare river_id int default NULL;
	declare location_id int default NULL;
    select id into river_id from river r where r.name = river_name;
	select id into location_id from location l where l.name = location_name;
    INSERT INTO measurement_point(river_id, location_id) values (river_id, location_id);
	select * from measurement_point where id=last_insert_id();
end$$
call convinient_insert("Дніпро", "Лиманка")$$
DELIMITER ;

