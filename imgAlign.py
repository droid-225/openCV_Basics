import cv2
import numpy

# Types of Transformations:
# Translation: keeps same shape and size, changes coordinates of shape
# Euclidean: basically rotates the shape keeping shape and size the same
# Affine: Changes size and shape, but parallel lines remain parallel
# Homography: changes shape into some other quadrilateral

img1 = cv2.imread("img/form.jpg", cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img3 = cv2.imread("img/scanned-form.jpg", cv2.IMREAD_COLOR)
img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

form_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
scan_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Creating Keypoints
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(form_gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(scan_gray, None)

# keypoints are usually some interesting feature in an image that are associated with some sharp edge or corner
# keypoints are described by a set of pixel coordinates, size and the orientation of the key point
# descriptors describe the region around the keypoint, a vector representation around the keypoint
# the red circles are keypoints, the center of the circle is the location of the keypoint, size of the circle is the scale of the keypoint and the radius line represents the orientation of the keypoint

form_display = cv2.drawKeypoints(img1, keypoints1, outImage=numpy.array([]),color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
scan_display = cv2.drawKeypoints(img3, keypoints2, outImage=numpy.array([]),color=(255,0,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Matching Keypoints
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
matches = matcher.match(descriptors1, descriptors2, None)

# Sort matches by score
list(matches).sort(key=lambda x: x.distance, reverse=False)

# Remove matches with bad scores
numGoodMatches = int(len(matches) * 0.1) # * 0.1 leaves the top 10 percent of matches
matches = matches[:numGoodMatches]

img_matched = cv2.drawMatches(img1, keypoints1, img3, keypoints2, matches, None)

# Find location of good matches
points1 = numpy.zeros((len(matches), 2), dtype=numpy.float32)
points2 = numpy.zeros((len(matches), 2), dtype=numpy.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

# Find homography
h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

# Use homography to warp image
height, width, channels = img1.shape
scan_reg = cv2.warpPerspective(img3, h, (width, height))

cv2.imshow("form", img1)
cv2.imshow("scan", scan_reg)

cv2.waitKey(0)
