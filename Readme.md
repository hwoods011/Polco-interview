
# How to run the application

1. Clone the repository: 
 > git@github.com:hwoods011/Polco-interview.git


## Docker
  You will need to have docker configured for your system.

  * Use this for Mac/Windows
  https://www.docker.com/products/docker-desktop

    - For Windows you'll need to set up WSL 
    https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

  
 If docker is configured correctly run the following commands

 > docker build -t billboard .

 Once build run the following

 > docker run -p 5000:5000 -t billboard

 You should then be able to navigate to 
 > http:// localhost:5000/  
 > http:// localhost:5000/users  
 > http:// localhost:5000/favorites/hwoods  

## Without Docker
1. If not using docker: Install Python and setup to be on system path.
2. Inside cloned folder run 
   > pip install -r requirements.txt  

## VSCode
  1. Open the folder you cloned inside VScode. (Likely is Polco-interview). Do not open the subfolder.
     1. Trust authors if it asks
  2. Go to the Run and Debug on the right hand side
  3. Click play button at the top of the panel.
  4. The flask app should start and you can then navigate to:
 > http:// localhost:5000/  
 > http:// localhost:5000/users  
 > http:// localhost:5000/favorites/hwoods  

## Terminal
 1. In your cloned folder run the following commands.
    - First set the following environment variables
   
   > FLASK_APP=songs.webapp  
   > FLASK_ENV=development  

 Now start the app
   > python -m flask run  
