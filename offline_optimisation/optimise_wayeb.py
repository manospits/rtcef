try:
    from libraries.optimisers.skopt_wrapper import SkoptWrapper
    from libraries.models.wrappers.wayeb_wraper import WayebWrapper, create_params_dict_from_list
except ImportError:
    import sys

    sys.path.append(sys.path[0] + '/..')
    from libraries.optimisers.skopt_wrapper import SkoptWrapper
    from libraries.models.wrappers.wayeb_wraper import WayebWrapper, create_params_dict_from_list

PROJECT_PATH = "/home/manospits/projects/onfore/"


def optimise_wayeb():
    fixed_params = {
        "java_port": 25334,
        "python_port": 25333,
        "k_val": 1,
        "weight_0": 1,
        "weight_1": 0,
        "threshold_time": 10000,
        "domain": "maritimejson",
        "objective_func": "nt",
        "pattern_path": PROJECT_PATH + "libraries/models/wrappers/patterns/enteringArea/pattern.sre",
        "declaration_path": PROJECT_PATH + "libraries/models/wrappers/patterns/enteringArea/declarations.sre"
    }
    model_save_path = PROJECT_PATH + "offline_optimisation/models/wayeb"
    dataset_path = PROJECT_PATH + "data/input/sample_data_100K.json"
    model = WayebWrapper(fixed_params)

    seed = 1234
    logpath = PROJECT_PATH + "offline_optimisation/logs/optimisation.log"
    pklpath = PROJECT_PATH + "offline_optimisation/logs/optimiser.pkl"
    samplespath = PROJECT_PATH + "offline_optimisation/logs/samples.txt"

    dimensions = {
        "confidence": [0.0, 1.0],
        "order": [1, 5],
        "pmin": [0.0001, 0.01],
        "gamma": [0.0001, 0.01]
    }

    opt_wrapper = SkoptWrapper(seed,
                               logpath,
                               pklpath,
                               samplespath,
                               dimensions)
    initial = 16
    total = 32
    acquisition_function = "EI"
    opt_wrapper.initialise_optimisation(initial, total, acquisition_function)

    opt_wrapper.step_by_step_optimisation()
    more_points_left = True

    iteration = 0
    while more_points_left:
        params = opt_wrapper.get_current_step_params()
        params_dict = create_params_dict_from_list(params)

        obj_params = model.train(params_dict, dataset_path, f"{model_save_path}_{iteration}")
        metrics = model.test(params_dict, dataset_path, f"{model_save_path}_{iteration}", obj_params)
        more_points_left = opt_wrapper.optimisation_step(params, metrics)
        iteration = iteration + 1

    optimisation_results = opt_wrapper.finalise()
    print(optimisation_results)
    model.close_gateway()


def main():
    optimise_wayeb()


if __name__ == "__main__":
    main()
