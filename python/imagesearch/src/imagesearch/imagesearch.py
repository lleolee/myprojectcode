# import the necessary packages
import argparse

import cv2
from colordescriptor import ColorDescriptor
from searcher import Searcher


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
    help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = False,
    help = "Path to the result path")
args = vars(ap.parse_args())
 
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))
# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
print('results='+str(results))
# display the query
cv2.namedWindow(args["query"],cv2.WINDOW_NORMAL)
cv2.imshow(args["query"], query)
cv2.waitKey(0)
cv2.destroyAllWindows()

# loop over the results
i = 0
for (score, resultID) in results:
    # load the result image and display it
    i+=1
    print(str(i) + ': result score='+str(score)+' path='+resultID)
    result = cv2.imread(resultID)
    if result is not None:
        cv2.namedWindow(resultID,cv2.WINDOW_NORMAL)
        cv2.imshow(resultID, result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
