#!/usr/bin/python
from pydub import AudioSegment
import time
import os

def get_file_size_in_megabytes(file_path):
    size = os.path.getsize(file_path)
    return size / (1024 * 1024)

def get_audio_duration_in_seconds(sound_file):
	return len(sound_file) / (1000 * 60)

start_time = time.time()

input_file_path = 'audio/input.wav'
output_file_path = 'audio/output.wav'

sound_file = AudioSegment.from_wav(input_file_path)
stripped_audio = AudioSegment.strip_silence(sound_file, silence_len=1100, silence_thresh=-25, padding=200)
stripped_audio.export(output_file_path, format='wav')

elapsed_time = time.time() - start_time
elapsed_time = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
print 'script exec time: {}'.format(elapsed_time)

input_file_size = get_file_size_in_megabytes(input_file_path)
output_file_size = get_file_size_in_megabytes(output_file_path)
diff_size = input_file_size - output_file_size
print 'input: {}mb, output: {}mb, diff: {}mb'.format(input_file_size, output_file_size, diff_size)
print "input length: {} minutes".format(get_audio_duration_in_seconds(sound_file))
print "output length: {} minutes".format(get_audio_duration_in_seconds(stripped_audio))