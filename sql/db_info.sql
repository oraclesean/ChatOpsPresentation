/* Function to get database information used by `/dbdo [database|instance]` demo. */
grant select on v_$database to appuser;
grant select on v_$instance to appuser;

create or replace function appuser.db_info (
         v_type               in     varchar2
,        message              out varchar2)
  return number
      as
         v_message            varchar2(1000) := 'Invalid TYPE.';
   begin

      if v_type = 'database'
    then select 'The current database is ' || name || ', running version ' || version || '.'
           into v_message
           from v$database, v$instance;
   elsif v_type = 'instance'
    then select 'Instance ' || instance_name || ' was started ' || to_char(startup_time, 'YYYY-MM-DD HH24:MI')
           into v_message
           from v$instance;
   end if;
          return 0;
      end db_info;
/
