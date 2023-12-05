from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
	sleep(0.005)
for elem in tqdm(range(333)):
	sleep(0.005)
for elem in ft_tqdm(range(999)):
	sleep(0.001)
for elem in tqdm(range(999)):
	sleep(0.001)
for elem in ft_tqdm(range(100)):
	sleep(0.009)
for elem in tqdm(range(100)):
	sleep(0.009)
