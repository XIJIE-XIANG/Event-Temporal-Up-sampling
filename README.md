# Event-Temporal-Up-sampling

## Introduction
Generate up-sampling events on the correct motion trajectory, which includes estimating the motion trajectory of the events by contrast maximization algorithm and up-sampling the events by the temporal point processes (Hawkes Process for main events, Self-correcting Process for noise).


## Code
[main.py](https://anonymous.4open.science/r/Event-Temporal-Up-sampling-70AB/main.py): up-sampling events

[Contrast_Maximization.py](https://anonymous.4open.science/r/Event-Temporal-Up-sampling-70AB/Contrast_Maximization.py): estimate event motion trajectory

[Temporal_Point_Processes.py](https://anonymous.4open.science/r/Event-Temporal-Up-sampling-70AB/Temporal_Point_Processes.py): up-sampling events by Hawkes Process and Self-correcting Process

[event_process.py](https://anonymous.4open.science/r/Event-Temporal-Up-sampling-70AB/event_process.py): including warp events, save up-sampling events, show result, etc.


## Usage
Change event_path in [main.py](https://anonymous.4open.science/r/Event-Temporal-Up-sampling-70AB/main.py) to your own path.


## Dependencies
python=3.8


