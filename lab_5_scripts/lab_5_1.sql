use lab_1;

drop table if exists souvenir;
create table souvenir(
	id int auto_increment primary key,
    name varchar(100),
    river_id int
);

drop trigger souvenir_before_insert;
delimiter $$
create trigger souvenir_before_insert before insert on souvenir
for each row
begin
	if not exists (SELECT 1 FROM river where id=NEW.river_id)
    then signal sqlstate '45000'
    set message_text="souvenir river not found";
    end if;
end$$
delimiter ;
