
delimiter $$
drop trigger souvenir_forbid_delete;
CREATE trigger souvenir_forbid_delete before delete on souvenir
FOR each row
    signal sqlstate '45000'
    set message_text="Can't delete souvenir";

delimiter $$
create table if not exists river_logs(
		id int auto_increment primary key,
        message varchar(255),
        action_at timestamp default current_timestamp
    );$$
drop trigger river_after_delete $$
CREATE trigger river_after_delete after delete on river
FOR each row
    insert into river_logs (message) values (CONCAT("deleted river with name=", old.name));

delimiter $$
drop trigger river_before_delete $$
CREATE trigger river_before_delete before delete on river
FOR each row
BEGIN
	declare total_rows int default 0;
    select COUNT(*) into total_rows from river;
    if total_rows<11 then  signal sqlstate '45000'
    set message_text="Can't delete river, too few left";
    end if;
END$$
