import os
import sys
import pickle
import numpy as np
from numpy.lib.format import open_memmap

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from feeder import Feeder_mediapipe

toolbar_width = 30

def print_toolbar(rate, annotation=''):
    # setup toolbar
    sys.stdout.write("{}[".format(annotation))
    for i in range(toolbar_width):
        if i * 1.0 / toolbar_width > rate:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('-')
        sys.stdout.flush()
    sys.stdout.write(']\r')

def end_toolbar():
    sys.stdout.write("\n")

def gendata(data_path, label_path, data_out_path, label_out_path, num_hand_in=1, num_hand_out=1, max_frame=300):
    feeder = Feeder_mediapipe(
        data_path=data_path,
        label_path=label_path,
        num_hand_in=num_hand_in,
        num_hand_out=num_hand_out,
        window_size=max_frame)

    sample_name = feeder.sample_name
    sample_label = []

    fp = open_memmap(
        data_out_path,
        dtype='float32',
        mode='w+',
        shape=(len(sample_name), 3, max_frame, 21, num_hand_out))

    for i, s in enumerate(sample_name):
        data, label = feeder[i]
        print_toolbar(i * 1.0 / len(sample_name), '({:>5}/{:<5}) Processing data: '.format(i + 1, len(sample_name)))
        fp[i, :, 0:data.shape[1], :, :] = data
        sample_label.append(label)

    with open(label_out_path, 'wb') as f:
        pickle.dump((sample_name, list(sample_label)), f)

if __name__ == '__main__':
    part = ['train', 'val']
    for p in part:
        data_path = '{}/mediapipe_{}'.format('JSON_data', p)
        label_path = '{}/mediapipe_{}_label.json'.format('JSON_data', p)
        data_out_path = '{}/{}_data.npy'.format('output_dataset', p)
        label_out_path = '{}/{}_label.pkl'.format('output_dataset', p)
        gendata(data_path, label_path, data_out_path, label_out_path)