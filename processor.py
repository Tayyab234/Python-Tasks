import random
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def imageprocess(img):
    duration = random.uniform(2, 6)
    print(f"{img} processing for {duration:.2f} seconds")
    time.sleep(duration)
    if duration > 4:
        raise Exception(f"{img} processing took too long: {duration:.2f} seconds")
    return f"{img} processed successfully in {duration:.2f} seconds"

if __name__ == "__main__":
    images = ['img1', 'img2', 'img3', 'img4']
    success = []
    timeout = []

    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(imageprocess, img): img for img in images}

        for future in as_completed(futures):
            img = futures[future]
            try:
                result = future.result()
                success.append((img, result))
            except Exception as e:
                timeout.append((img, str(e)))

    print("\nSummary:")
    print("Successful tasks: ", success)
    print("Unsuccessful tasks: ", timeout)
