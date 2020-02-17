  create or replace function appuser.oug_cities (
         oug                  in     user_groups.oug_name%TYPE
,        city                 in     user_groups.oug_city%TYPE
,        oug_message             out varchar2)
  return number
      as
         v_oug_id             user_groups.oug_id%TYPE;
         v_oug_name           user_groups.oug_name%TYPE;
         v_oug_city           user_groups.oug_city%TYPE;
   begin
           select oug_id
         ,        oug_name
         ,        oug_city
             into v_oug_id
         ,        v_oug_name
         ,        v_oug_city
             from user_groups
            where upper(oug_name) = upper(oug);

      if v_oug_city = city
    then oug_message := 'There was no change to ' || v_oug_name || '.';
    else
            update user_groups
               set oug_city      = city
             where oug_id        = v_oug_id;
          commit;

                 if v_oug_city is null
               then oug_message := 'The ' || oug || ' user group now has meetings in ' || city || '.';
              elsif v_oug_city != city
               then oug_message := 'The ' || oug || ' user group previously met in ' || v_oug_city || ' but now meets in ' || city || '.';
             end if;
   end if;
          return v_oug_id;

exception
     when no_data_found
     then   insert
              into user_groups (
                   oug_name
          ,        oug_city)
            values (
                   oug
          ,        city)
                   returning oug_id into v_oug_id;
          commit;

          oug_message := 'The ' || oug || ' user group that meets in ' || city || ' was added to the database.';
          return v_oug_id;
      end oug_cities;
/
