  create table user_groups (
         oug_id               number
         generated by default as identity
,        oug_name             varchar2(40) not null
,        oug_city             varchar2(40));

  create unique index user_groups_u1
      on user_groups(oug_id);

   alter table user_groups
     add constraint user_groups_pk
         primary key(oug_id)
         using index user_groups_u1;
