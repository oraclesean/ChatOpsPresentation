/* Create an application user to own objects and code */
create user appuser identified by ###STRONG_PASSWORD###;
grant create session, resource to appuser;
alter user appuser quota unlimited on ###APPLICATION_TABLESPACE###;

/* Create a Slack user to run code remotely from the Slack API */
create user slack identified by ###STRONG_PASSWORD###;
grant create session to slack;
