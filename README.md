# Event-Temporal-Up-sampling

# Introduction
Generate up-sampling events on the correct motion trajectory, which includes estimating the motion trajectory of the events by contrast maximization algorithm and up-sampling the events by the temporal point processes (Hawkes Process for main events, Self-correcting Process for noise).

## Code
[main.py](https://github.com/XIJIE-XIANG/Event-Temporal-Up-sampling/blob/main/main.py): up-sampling events
[Contrast_Maximization.py](https://github.com/XIJIE-XIANG/Event-Temporal-Up-sampling/blob/main/Contrast_Maximization.py): estimate event motion trajectory
[Temporal_Point_Processes.py](https://github.com/XIJIE-XIANG/Event-Temporal-Up-sampling/blob/main/Temporal_Point_Processes.py): up-sampling events by Hawkes Process and Self-correcting Process
[event_process.py](https://github.com/XIJIE-XIANG/Event-Temporal-Up-sampling/blob/main/event_process.py): including warp events, save up-sampling events, show result, etc.

## Usage
Change event_path in [main.py](https://github.com/XIJIE-XIANG/Event-Temporal-Up-sampling/blob/main/main.py) to your own path.

## Dependencies
python=3.8


