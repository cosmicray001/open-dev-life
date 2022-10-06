### get elasticsearch info in your system
```curl 'http://localhost:9200/?pretty'```

### get count
```
GET /_count
{
    "query": {
        "match_all": {}
        }
}


GET index_name/_count
{
    "query": {
        "match_all": {}
        }
}
```

### create doc
```
PUT /megacorp/employee/3
{
    "first_name": "Douglas",
    "last_name": "Fir",
    "age": 35,
    "about": "I like to build cabinets",
    "interests": [
      "forestry"
    ]
}
```

### retrive doc
```
GET /index_name/type_name/1

GET /megacorp/employee/1
```
