import os
import math
import numpy as np

from event_process import dist_main_noise, event_trace, min_inter, limit_num, show_events, save_event
from Contrast_Maximization import contra_max
from Temporal_Point_Processes import HP, SP

if __name__ == '__main__':
    event_path = 'data/shapes_6dof.npy'
    event = np.load(event_path)

    # hyper parameters
    rangeX, rangeY = 240, 180
    limit_up_rate = 4

    X = event[:, 1]
    Y = event[:, 2]
    P = event[:, 3]
    T = (event[:, 0] - event[0, 0]) * 10 ** 6

    # save path of results
    save_path = 'results/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    gen_events = []

    event_num = 10000
    num = math.ceil(event.shape[0] / event_num)
    for k in range(int(num)):
        x = X[k * event_num:(k + 1) * event_num]
        y = Y[k * event_num:(k + 1) * event_num]
        p = P[k * event_num:(k + 1) * event_num]
        t = T[k * event_num:(k + 1) * event_num]

        t_min = np.min(t)
        t_ref = np.max(t)

        flow = contra_max(x, y, p, t, t_ref, rangeX, rangeY)

        # trajectory of noise and main events
        ref, nx, ny, mx, my = dist_main_noise(flow, x, y, p, t, t_ref, rangeX, rangeY)
        print(k + 1, '/', num, '. Noise events: ', nx.size, ', Main events: ', np.sum(np.abs(ref)) - nx.size)

        trace = event_trace(flow, x, y, p, t, t_ref, rangeX, rangeY)
        min_i = min_inter(t_ref, mx, my, trace)

        cur_gen_events = []

        # up-sampling noise by Self-correcting Process
        for i in range(nx.size):
            u = 1.0 / (t_ref - np.min(t))
            b = 1
            th = 1
            up_noise = SP(trace[nx[i]][ny[i]][0], t_min, t_ref, u, b, th, mx, my, flow, rangeX, rangeY)
            cur_gen_events.append(up_noise)
        cur_gen_events = np.array(cur_gen_events).squeeze()

        # up-sampling main events by Self-correcting Process

        basic_w = 0.0001
        basic_w = basic_w * (nx.size / (np.sum(np.abs(ref)) - nx.size) + 2) # n/m + 2 ~ lambda
        w = basic_w / np.log(min_i) # min_t ~ 1/lambda

        for i in range(mx.size):

            cur_events = np.array(trace[mx[i]][my[i]])

            # event number of ON events and OFF events
            n_on = np.where(cur_events[:, 2] > 0)
            n_off = np.where(cur_events[:, 2] == 0)
            up_main_events = HP(cur_events, [len(n_off[0]) * w, len(n_on[0]) * w], w, mx[i], my[i], flow, t_ref, min_i, a=np.array([[1.0, 0.0], [0.0, 1.0]]), rangeX=rangeX, rangeY=rangeY)

            # limiting the number of up-sampling events
            up_main_events = limit_num(cur_events, up_main_events, limit_up_rate)

            cur_gen_events = np.append(cur_gen_events, up_main_events, axis=0)

        if k == 0:
            gen_events = np.array(gen_events)
            gen_events = cur_gen_events
        else:
            gen_events = np.append(gen_events, cur_gen_events, axis=0)

        print('The number of original events are: ', x.size)
        print('The number of up-sampling events are: ', cur_gen_events.shape[0])

        show_events(np.array(cur_gen_events), x, y, p, t)

    save_event(gen_events, X, Y, P, T, save_path=save_path)
