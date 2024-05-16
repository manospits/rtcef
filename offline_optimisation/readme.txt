Offline optimisation script

0. Build wayeb in onfore/libraries/wrappers/wayeb as usual (sbt assembly)

1. Install requirements from onfore/requirements.txt in a conda environment with python 3.9.18 (other python versions
   might not work)
    - detailed package versions available also in conda-package-list.txt (safer to use requirements first)

2. Change PROJECT_PATH in offline_optimisation/optimise_wayeb.py and offline_optimisation/run.sh

3. Extract sample_data_100K.json from data/input/sample.tar.gz to data/input/sample_data_100K.json

4. Call run.sh
    - run.sh starts (a) a wayeb server listening on a specific port and (b) starts the optimiser which
      sends calls to the wayeb server
    - when you call run.sh, wayeb server PID is printed in wayeb_server_pid.txt in case you need to kill it.
    - logs folder will contains optimisation logs
    - models folder contains wayeb models

