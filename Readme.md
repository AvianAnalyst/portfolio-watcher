# Portfolio Watcher

### Quick Start: <br>
```bash
# starting in the project home directory
pipenv sync
invoke start-django
# open a new terminal
invoke start-vue
```

To add investments, open your browser to the django project: [Default](http://localhost:8000/).

Follow the links and instructions from there. The link to view your reports links to the default location for the Vue
Dev server, [here](http://localhost:8080/). If it doesn't work, please navigate to the proper URL manually.

___

### Backend API

To get a report directly from the django project, the proper endpoint is `/investments`, to generate a historical report 
pass an `investments_date` parameter in the query string in the format YYYY-MM-DD (i.e. 
`/investments?investment_date=2019-10-1`). 