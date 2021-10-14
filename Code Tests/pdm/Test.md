



pdm add atoti
pdm add atoti-jupyterlab
pdm add objection

objection = "^1.11.0"


$ pdm config pypi.json_api false
$ pdm cache clear
$ pdm lock && pdm sync
