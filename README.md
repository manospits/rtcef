# Run-Time Optimisation for Complex Event Forecasting (_RTCEF_)

_RTCEF_ is a framework for run-time optimisation of Complex Event Foecasting. It contains several services running synergistically over Kafka with the aim of undisrupted CEF, and run-time updating of deployed CEF models for continuous adaptation to input stream evolutions.


## _RTCEF_

### Complex Event Forecasting (CEF)
Complex Event Forecasting (CEF) is a process whereby Complex Events (CEs) are forecasted over an input stream. For example, in the maritime domain CEF could forecast a CE expressing the arrival of a ship in a specific port, over a stream of maritime positional data.
For CEF, _RTCEF_, currently supports Wayeb, a Scala implemented CEF engine. In the future more engines/models will be supported.

### Run-time hyper-parameter optimisation
For many CEF models, hyper-parameters play major role in performance. While offline hyper-parameter optimisation can yield a near optimal set of parameters for a fixed time period, in practice it is not sufficient. This is because our world, and therefore data, is constantly evolving. For example, maritime vessels adapt their routes according to weather, fraudsters adapt their tactics to avoid detection and so on.

_RTCEF_ offers the solution to this problem, by allowing run-time optimisation for finding near-optimal hyper-paramaters. More specifically, it utilises Bayesian optimisation. Furthermore, since hyper-parameter optimisation can be an expensive task, it offers a retrain vs reoptimise policy. Finally, _RTCEF_ does not hinder performance, as retrain or optimisation procedures happen in parallel to CEF.




### Architecture

![arch](https://github.com/manospits/rtcef/blob/main/docs/arch.png?raw=true)

As seen in the above figure, _RTCEF_ has five services, the engine, the observer, the collector, the controller and the model factory. These work as follows:

* **Engine:** The engine performs CEF, it reads simple events from the input stream and produces forecasts. Additionally, it produces a stream of performance reports (scores).
* **Observer:** The observer service, monitors performance of the engine, and using a trend based policy it detects performance deterioration and issues **retrain** or **optimise** instructions.  
* **Collector:** The collector service, reads in parallel to the engine the input stream. In order to perform model retraining or optimisation appropriate dataset should be used. Therefore the collector using a window based policy retains subsets of the input stream in a sliding window approach and creates dataset versions.
* **Controller:** The controller service, controls retraining or optimisation procedures. It reads instructions provided by the observer and accordingly commands the factory to create a model via retraining, or initialises an optimisation procedure with the factory, during which the controller serves as the optimiser.
* **Factory:** The factory service, trains (and tests) models for retraining and optimisation procedures. Once a new model is available, i.e. a retrained model, or the best performing model of an optimisation procedure, the factory sends a model version to the Engine. The engine replaces its underlying model, and continues CEF with the most recent model version. 
## Installation
 + _RTCEF_ is mostly implemented in Python 3.9.18, therefore the appropriate python version must be installed.
   + Additionally, the python packages included in the `requirements.txt` should be installed as well.
 + Services of _RTCEF_ communicate over Kafka. For your convenience, in folder `scripts`, there is a docker file setting up Confluent's Kafka. Therefore to set up Kafka, you need to have docker installed, and then execute the `scripts/start_kafka.sh` script.
 + Wayeb, the current CEF engine requires a Scala installation. Once Scala is installed navigate to `libraries/models/wrappers/wayeb` and run `sbt assembly`. This will compile Wayeb.  

## Usage
To run existing experiments navigate to the `scripts` folder.

1. Make sure that Kafka is up and run the following command ```./deploy_services.sh init ```. This will create the appropriate communication topics in Kafka.

2. To start CEF with _RTCEF_ you need a configuration file. In  the `configs` folder there configuration files for maritime situational awareness and credit card fraud detection experiments. To run a specific experiment replace the path of the configuariton file in the `deploy_services.sh` script accordingly. Then run the experiment with ```./deploy_services.sh start``` 
In case you want to run an experiment without run-time updating of CEF models execute instead: ```./deploy_services.sh start_offline```

3. To stop the framework run ```./deploy_services.sh kill```

**Note:** Before running a new experiment you should ''clean'' the Kafka topics. To do this run:

```./deploy_services.sh clean```

## License

## Project status

_RTCEF_ is a project with ongoing development.