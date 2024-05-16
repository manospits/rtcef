# Run-Time Optimisation for Complex Event Forecasting (_RTCEF_)

_RTCEF_ is a framework for optimisation of Complex Event Foecasting. It contains several services running synergistically over Kafka with the aim of undisrupted CEF, and run-time updating of deployed CEF models for continuous adaptation to input stream evolutions.


## _RTCEF_

### Complex Event Forecasting (CEF)
Complex Event Forecasting (CEF) is a process whereby Complex Events (CEs) are forecasted over an input stream. For example, in the maritime domain CEF could forecast a CE expressing the arrival of a ship in a specific port, over a stream of maritime positional data.
For CEF, _RTCEF_, currently supports Wayeb, a Scala implemented CEF engine. In the future more engines/models will be supported.

### Architecture

![arch](https://github.com/manospits/rtcef/blob/main/docs/arch.png?raw=true)

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