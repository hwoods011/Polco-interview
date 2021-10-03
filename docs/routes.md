# Routes and Flowchart

 ## Flowchart
    Flowchart was done using https://app.diagrams.net/. 

    See User_flow.png

 ## Routes
    Please check the api_spec.yml for detailed route info. This is my first time writing in the openAPI spec but I used docs from https://swagger.io/docs/specification/describing-parameters/ and also used the VSCode plugin OpenAPI(Swagger) to help provide intellisense hints.   
    It hopefully is pretty close to right.

#### However, a few notes about the current layout  
   * Filtering the billboard list  
     * All filtering as written would be done in the UI
     * Reasons:
       * Data size is relatively tiny (100 songs) 
       * Browser would likely be faster than making an API call
     * If it was found that we wanted to filter by making another query I would modify the /billboard route to accept parameters and build out the sql query (or modify future ORM query) to do it that way. 
   * User Auth
     * Password passed in as plain text
       * This would also likely need to be changed at some point. I really included this to ensure the full flow was realized. 
  


