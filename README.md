# Federal Employee Meeting Cost Tracker
`fed_sal`

`salary_lookup` is a commandline tool that enables the user to track the cost of a meeting attended by federal employees.

The goal is to make a back-end with [Falcon](http://falcon.readthedocs.io/en/stable/) so a more usable front-end can be deployed.

`falcon_lookup` and `falcon_resource` are the basis of the WSGI app which will call functions from `salary_lookup`.
