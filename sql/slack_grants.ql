/* OPTIONAL: Prevent the application owner from being able to log in; 
   this user has object privileges and revoking create session protects against login. */
revoke create session from appuser;

grant execute on appuser.oug_cities to slack;
grant execute on appuser.db_info to slack;
create synonym slack.oug_cities for appuser.oug_cities;
create synonym slack.db_info for appuser.db_info;
