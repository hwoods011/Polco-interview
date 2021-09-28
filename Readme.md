
# How to run the application

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

## VSCode

 
