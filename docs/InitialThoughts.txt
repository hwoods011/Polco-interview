Initial thoughts


Applications seems reasonably straightforward. 
Below are my thoughts and design desisions.
For the part I will code I've chosen to a portion of the backend.
  Specifically here is what I want to have implemented when I submit this
    DB, setup and seeding automatically or by running a command
	   - Generate some seed data.
	Backend: 
	   - Implement two routes, 
	     health check route 
		 route to get all user favorite songs
		   this will ensure that I have my data model mostly correct as I will need to query all tables to show this.
		- Make it run as a docker image
		  - just for fun and because I don't think it will take that long. 
		add unittests
		  For my route add tests, seed data and query.
	   
	   


DB:
  SQLLite 3
    - basic and pure sql so easily able to port to something later
	  - No/little DB specific syntax that could impact changes later
	- simple
	- can spin up in memory so I don't have to mock db connections/queries in my tests


Backend Architecture

Language
  - Python
    pros:
	  - easy to work with with VSCode, (pretty much works out of the box)
	  - easy to configure tests
	  - easy debugging
	  - no transpiling into other versions
	cons:
	  - lack of strongly typing leaves room for errors
	  - having multiple versions of python can be a pain
   
  - Node.js/typescript
    pros:
	  - strongly typed
	  - lots of nice features and very modern. 
	  - can be transpiled to run on any system
	cons:
	  - not as familiar with compiler process especially with TS
		- could take me the entire 4 hours to just get it compiling and running
		   ( based on past experiences)
	  - choosing what version to compile into can be a mess.
	  
	Decision:
	  I'm going to go with python. While I'll lose the ability to more strongly type my code I think
	  not having to try and compile typescript and being able to use some inbuilt vscode niceties I will be better off for this project
	  If fully building out this app I would very likely choose nodejs and typescript as backend language. 
	  
Backend webserver
    Flask seems like the obvious choice to me. It's easy to use(more importantly I've used it many times before) and documentation surrounding it is good. 
	
SQL Interaction library
   Admittely I'm not super familiar with using DB's with python but it looks like a very used library is SQLAlchemy. I'm going to start with that
    
	
Rest vs graphql
    For backend web interface I'm going to do a rest api. I've never setup a graphql endpoint from scratch( however it looks maybe fairly simple so I may give it a shot)
	I've enjoyed a project I'm working on now where we are using a GQL backend with node however I'm not sure I will have the time to properly set it up. I still may try if everything else is going well.
	


FrontEnd
    I'm not going to implement this part but if I were I would choose react. 
	  I've been using it on my most recent project and I've really come to enjoy using it. 

	  
	