# Documentation

## Database Model  
#### Technologies
* SQLite 3. It's easy to use and get started with. 
* Refer to db_model.png in the github repo for clean picture


## Back-end architecture  
  
  ### What I set out to acheive
   * Ease of use. 
   * Not hard to install dependencies and is a popular library offering ensuring that documentation is good.
   * Ease of testing, when running tests my goal is for them to be as repeatable as possible but as close to production as possible. 
     - SQLite 3 is unique because by default it stores the entire DB in a file or can be run in memory (like so each instance of a unittest could have it's own db instance). This enables tests to be able to run against actual data and not mocked data. 
     - The dataset seems to be very tiny in size so I would have no problem using SQLite3 going forward. 


  ### What I chose to do for the coding portion  
  ##### Python and Flask
   * Python  
     - I'm a big fan of python for scripting and it's ease of use getting things done quickly. I have used it quite a bit at my current job and so it seemed like a good tool for the job   
   * Flask
     - A popular, super slim, python web framework that allows you to do whatever you want with it without forcing it's own 'opinions' on how you structure the code. 
     - We use flask at my current job fairly extensively for some of our stateless 'validation' webhook applications. 
     - It boasts a super simple setup to get going which initially to me was very appealing. 
       - In practice I spent more time than I would've liked getting it stood up to use with a DB or in a 'stateful' manner. However I did get a solution working that could be expanded on an improved when building out a full fledged application.

    Overall I'm pleased with how it turned out. If I would've had more time I would've liked to start and implement a simple test to show how I would implement testing. 
  
  ### Hindsight  
  #### Node.js and Typescript Graphql  
   * Considering some of the difficulties I had getting Flask working in a way that I was happy with it may have been the better to go with a Node.js/Typescript backend. I would likely use express as the webserver because of it's relative ease to get stood up.   
    I really like the using Typescript as I find that the compiler is really good at finding bugs which is just another way to find potential errors before even running your code. 

  ##### So Why didn't I do this?  
    
   * I've never really started a node.js/Typescript project from complete scratch before and the few dabblings I've had with it on my current project I ran into all sorts of isses with the transpilings. I didn't want to waste prececious time on that. 
   * In hindsight I maybe should've gone for it as Flask gave me trouble as well. 

 ### Future enhancements
   * Setup a docker compose instance to allow for a reliable webservice that auto updates with changes. 
   * Eventual solution could land in some sort of container platform or be stood up on Kubernetes if the user load dictated it. 
   * Automation to ingest and update the billboard top 100. 
    - This would be a microservice that would add the data to our database via rest api calls. 
   

## Methodology for accessing data

 As the project currently stands. The backend is a Python/Flask RestAPI with a SQLite3 data layer.
 * The RestAPI returns JSON data to the front end to be displayed to the user.
  
  Currently data fetches are handled by using parameterized raw sql. Going forward one task would be to look into an ORM to allow some niceties to be done to either speed up adding new functionality or to cut down on boilerplate code. 
 

## Frontend Architecture
  For frontend architecture I would use a React front end. I like the modular and reusable nature of React Components.
  * Querying: React-query. An awesome query library to handle fetching data.
   - React query provides lots of nice hooks to allow for dynamic rendering of components based on when data is fetched. It would also make adding additional microservices to easy. 
  * Tables: React-table. Since we're talking about a list of things most likely a table will be needed at some point. This library makes tables pretty east to create and allows for them to be reusable. 

## Testing strategy

#### Unittests
* Repeatability
   - All official tests would be run by using a Dockerfile.test for all pieces of the application.
   - A Dockerfile.test would be nearly the same as the Dockerfile to build and run the application but instead would run the testing command vs the command to start the app. This ensures that you have a reliable (relatively) platform agnostic vehicle in which to execute your tests. 

These tests could be run using a jenkins instance or the CI/CD platform of choice.


* Backend:
  - Flask allows for testing of the webservice itself or each function could be tested individually. 
  - Goals of testing would be to:
    - Minimize mocking through the use of a reliable seed and in memory database that allows real queries to be executed. 

* Frontend
   - Jest would like be test runner. Testing library is also good for performing render tests on what users would see when buttons are clicked.
   - MSW for react provides a good way to Mock API calls without having to use jest mocks. I find this is very helpful for not having to mock out anything to do with external sources.


#### Integration tests
  Unit tests are only so good as there is still room for error when the client and microservices are tested in silos.
  If I were architecting this out I would spin up a docker-compose instance with a full app running and then use Selenium or some other popular Integration test library to conduct repeatable integration tests





 