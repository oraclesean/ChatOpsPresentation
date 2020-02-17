# ChatOpsPresentation
Code related to my Oracle + ChatOps presentations
## Setup
The files to build the SLACK and APPUSER users, sample schema objects, functions called from the API, and permissions are in the sql folder.
## Set up Slack
Create an account.
Add a channel.
Navigate to Create a Slack App.
Add "Slash Commands" to the App. It will create a Bot user.
Get the OATH and BOT access tokens and save them for later.
Create a new command, `/dbdo` and fill in anything for the Request URL for now, it will be updated later.
Add the App to any channels you want it to run in.
## Running the app
### Get the repo
Pull the repo contents to the application (Python) host.
### Install dependencies
```
yum -y install yum-utils
yum install -y --disablerepo=ol7_developer_EPEL python36
pip install --upgrade pip
python -m pip install cx_Oracle
python -m pip install flask
pip install Flask-API
pip install python-dotenv
pip install slack
pip install slackclient
pip install slackbot
pip install requests
```
### Set the environment
```
echo "
export FLASK_APP=dbdo.py
export ORACLE_HOME=/opt/oracle/product/19c/dbhome_1
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$ORACLE_HOME/lib" >> ~/.bash_profile
```
### Build a Python virtual environment
```
python3 -m venv ~/py36env
source ~/py36env/bin/activate
```
### Add a TNS entry for the service
If necessary.
### Open a firewall port 
If necessary. On OCI, also update from the console.
### Create users and objects
See the files under the `sql` subdirectory.
### Install ngrok
```
mkdir ~/ngrok
cd ~/ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
```
Get an authtoken from dashboard.ngrok.com/auth then add it
`./ngrok authtoken`
### Start ngrok
`./ngrok http 5000`
Note the forwarding address and add it as the Request URL under your Slack App.
### Edit the .env file
Substitute relevant information into the .env file.
### Run the application
Set the Python virtual environment.
Verify `FLASK_APP` is set.
Run:
`flask run`
Issue commands via the Slack /dbdo command.
