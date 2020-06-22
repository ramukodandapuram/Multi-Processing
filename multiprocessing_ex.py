# import multiprocessing
import concurrent.futures
import time
from PIL import Image, ImageFilter


img_names = [

'photo-1493976040374-85c8e12f0c0e.jpg',
'photo-1504198453319-5ce911bafcde.jpg'

]

start = time.perf_counter()

size = (1000,1000)
def process_image(img_name):
# for img_name in img_names:
	img = Image.open(img_name)

	img = img.filter(ImageFilter.GaussianBlur(15))
	img.thumbnail(size)
	img.save(f'processed/{img_name}')
	print(f'{img_name} was processed...')

# def do_something(seconds):
# 	print(f'Sleeping {seconds} second(s)....')
# 	time.sleep(seconds)
# 	return f'Done sleeping....{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
	executor.map(process_image, img_names)
 	# secs = [5,4,3,2,1]
# 	results = executor.map(do_something, secs)

# 	for result in results:
# 		print(result)
	# for f in concurrent.futures.as_completed(results):
	# 	print(f.result())

# processes = []
# for _ in range(10):
# 	p=multiprocessing.Process(target = do_something, args=[1.5])
# 	p.start()
# 	processes.append(p)
# for process in processes:
# 	process.join()

# p1 = multiprocessing.Process(target = do_something)
# p2 = multiprocessing.Process(target = do_something)

# p1.start()
# p2.start()
# p1.join()
# p2.join()
finish = time.perf_counter()

print(f'Finished in {round(finish-start)} seconds(s)')