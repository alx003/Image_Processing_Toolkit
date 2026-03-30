"""
DSC 20 Project Winter 2026
Name(s): Allison Xu, Yunjia Xing
PID(s):  A19064928, A19072817
Sources: Google about deep copyju
"""

import numpy as np
import os
from PIL import Image
import copy

NUM_CHANNELS = 3


# --------------------------------------------------------------------------- #

# YOU SHOULD NOT MODIFY THESE TWO METHODS

def img_read_helper(path):
    """
    Creates an RGBImage object from the given image file
    """
    # Open the image in RGB
    img = Image.open(path).convert("RGB")
    # Convert to numpy array and then to a list
    matrix = np.array(img).tolist()
    # Use student's code to create an RGBImage object
    return RGBImage(matrix)


def img_save_helper(path, image):
    """
    Saves the given RGBImage instance to the given path
    """
    # Convert list to numpy array
    img_array = np.array(image.get_pixels())
    # Convert numpy array to PIL Image object
    img = Image.fromarray(img_array.astype(np.uint8))
    # Save the image object to path
    img.save(path)


# --------------------------------------------------------------------------- #

# Part 1: RGB Image #
class RGBImage:
    """
    Represents an image in RGB format
    """

    def __init__(self, pixels):
        """
        Initializes a new RGBImage object

        # Test with non-rectangular list
        >>> pixels = [
        ...              [[255, 255, 255], [255, 255, 255]],
        ...              [[255, 255, 255]]
        ...          ]
        >>> RGBImage(pixels)
        Traceback (most recent call last):
        ...
        TypeError

        # Test instance variables
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.pixels
        [[[255, 255, 255], [0, 0, 0]]]
        >>> img.num_rows
        1
        >>> img.num_cols
        2
        """
        # YOUR CODE GOES HERE #
        # Raise exceptions here
        # pixels is a list, at least one element
        if not isinstance(pixels, list) or len(pixels) == 0:
            raise TypeError()

        # rows are lists, at least one elem
        for row in pixels:
            if not isinstance(row, list) or len(row) == 0:
                raise TypeError()

        # rows have same length
        first_row_length = len(pixels[0])
        for row in pixels:
            if len(row) != first_row_length:
                raise TypeError()

        # elem in each row are lists of length 3
        for row in pixels:
            for pixel in row:
                if not isinstance(pixel, list) or len(pixel) != 3:
                    raise TypeError()

        # intensity value is integer from 0-255
        for row in pixels:
            for pixel in row:
                for intensity in pixel:
                    if not isinstance(intensity, int) or \
                    not (0 <= intensity <= 255):
                        raise ValueError()
                

        self.pixels = pixels
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])


    def size(self):
        """
        Returns the size of the image in (rows, cols) format

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img.size()
        (1, 2)
        """
        # YOUR CODE GOES HERE #
        return (self.num_rows, self.num_cols)

    def get_pixels(self):
        """
        Returns a copy of the image pixel array

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_pixels = img.get_pixels()

        # Check if this is a deep copy
        >>> img_pixels                               # Check the values
        [[[255, 255, 255], [0, 0, 0]]]
        >>> id(pixels) != id(img_pixels)             # Check outer list
        True
        >>> id(pixels[0]) != id(img_pixels[0])       # Check row
        True
        >>> id(pixels[0][0]) != id(img_pixels[0][0]) # Check pixel
        True
        """
        # YOUR CODE GOES HERE #
        return copy.deepcopy(self.pixels)

    def copy(self):
        """
        Returns a copy of this RGBImage object

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_copy = img.copy()

        # Check that this is a new instance
        >>> id(img_copy) != id(img)
        True
        """
        # YOUR CODE GOES HERE #
        new_pixels = self.get_pixels()

        return RGBImage(new_pixels)

    def get_pixel(self, row, col):
        """
        Returns the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid index
        >>> img.get_pixel(1, 0)
        Traceback (most recent call last):
        ...
        ValueError

        # Run and check the returned value
        >>> img.get_pixel(0, 0)
        (255, 255, 255)
        """
        # YOUR CODE GOES HERE #
        # row and col are integers
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError()

        # valid indicies
        if row < 0 or row >= self.num_rows or \
           col < 0 or col >= self.num_cols:
           raise ValueError()

        pixels_colors = self.pixels[row][col]
        return (pixels_colors[0], pixels_colors[1], pixels_colors[2])


    def set_pixel(self, row, col, new_color):
        """
        Sets the (R, G, B) value at the given position

        # Make sure to complete __init__ first
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)

        # Test with an invalid new_color tuple
        >>> img.set_pixel(0, 0, (256, 0, 0))
        Traceback (most recent call last):
        ...
        ValueError

        # Check that the R/G/B value with negative is unchanged
        >>> img.set_pixel(0, 0, (-1, 0, 0))
        >>> img.pixels
        [[[255, 0, 0], [0, 0, 0]]]
        """
        # YOUR CODE GOES HERE #
        # row and col are integers
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError()

        # row and col are valid indices
        if row < 0 or row >= self.num_rows or \
           col < 0 or col >= self.num_cols:
           raise ValueError()

        # new_color is a tuple of length 3, all integers
        if (not isinstance(new_color, tuple) or len(new_color) != 3 \
        or not all(isinstance(n, int) for n in new_color)):
            raise TypeError()

        # all values in new_color are less than or equal to 255
        for n in new_color:
            if n > 255:
                raise ValueError()

        for i, n in enumerate(new_color):
            if n < 0:
                pass
            else:
                self.pixels[row][col][i] = n


# Part 2: Image Processing Template Methods #
class ImageProcessingTemplate:
    """
    Contains assorted image processing methods
    Intended to be used as a parent class
    """

    def __init__(self):
        """
        Creates a new ImageProcessingTemplate object

        # Check that the cost was assigned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0

    def get_cost(self):
        """
        Returns the current total incurred cost

        # Check that the cost value is returned
        >>> img_proc = ImageProcessingTemplate()
        >>> img_proc.cost = 50 # Manually modify cost
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        return self.cost

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check if this is returning a new RGBImage instance
        >>> img_proc = ImageProcessingTemplate()
        >>> pixels = [
        ...              [[255, 255, 255], [0, 0, 0]]
        ...          ]
        >>> img = RGBImage(pixels)
        >>> img_negate = img_proc.negate(img)
        >>> id(img) != id(img_negate) # Check for new RGBImage instance
        True

        # The following is a description of how this test works
        # 1 Create a processor
        # 2/3 Read in the input and expected output
        # 4 Modify the input
        # 5 Compare the modified and expected
        # 6 Write the output to file
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()                            # 1
        >>> img = img_read_helper('img/test_image_32x32.png')                 # 2
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')  # 3
        >>> img_negate = img_proc.negate(img)                               # 4
        >>> img_negate.pixels == img_exp.pixels # Check negate output       # 5
        True
        >>> img_save_helper('img/out/test_image_32x32_negate.png', img_negate)# 6
        """
        # YOUR CODE GOES HERE #
        new_pixels_negate = [[[255-n for n in pixel] for pixel in row]for \
        row in image.get_pixels()]

        return RGBImage(new_pixels_negate)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_gray.png')
        >>> img_gray = img_proc.grayscale(img)
        >>> img_gray.pixels == img_exp.pixels # Check grayscale output
        True
        >>> img_save_helper('img/out/test_image_32x32_gray.png', img_gray)
        """
        # YOUR CODE GOES HERE #
        deepcopy_pixels = image.get_pixels()

        grey_pixels = [[
            [(sum(pixel) // 3)] * 3 for pixel in row]\
             for row in deepcopy_pixels]

        return RGBImage(grey_pixels)
        

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image

        # See negate for info on this test
        # You can view the output in the img/out/ directory
        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_rotate.png')
        >>> img_rotate = img_proc.rotate_180(img)
        >>> img_rotate.pixels == img_exp.pixels # Check rotate_180 output
        True
        >>> img_save_helper('img/out/test_image_32x32_rotate.png', img_rotate)
        """
        # YOUR CODE GOES HERE #
        deepcopy_pixels = image.get_pixels()

        # up down flip copy[::-1]
        # left right flip row[::-1]
        rotate_pixels = [row[::-1] for row in deepcopy_pixels[::-1]]

        return RGBImage(rotate_pixels)
        


    def get_average_brightness(self, image):
        """
        Returns the average brightness for the given image

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.get_average_brightness(img)
        86
        """
        # YOUR CODE GOES HERE #
        deepcopy_pixels = image.get_pixels()

        pixel_brightnesses = [
            sum(pixel)//3 for row in deepcopy_pixels for pixel in row]

        num_pixels = image.num_rows * image.num_cols
        avg_brightness = sum(pixel_brightnesses)//num_pixels

        return avg_brightness


    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level

        >>> img_proc = ImageProcessingTemplate()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_adjusted.png')
        >>> img_adjust = img_proc.adjust_brightness(img, 1.2)
        >>> img_adjust.pixels == img_exp.pixels # Check adjust_brightness
        True
        >>> img_save_helper('img/out/test_image_32x32_adjusted.png', img_adjust)
        """
        # YOUR CODE GOES HERE #
        if not isinstance(intensity, float):
            raise TypeError()

        deepcopy_pixels = image.get_pixels()

        new_color_pixels = [[
            [max(0, min(255, int(n * intensity))) for n in pixel]
            for pixel in row]
            for row in deepcopy_pixels]

        return RGBImage(new_color_pixels)



# Part 3: Standard Image Processing Methods #
class StandardImageProcessing(ImageProcessingTemplate):
    """
    Represents a standard tier of an image processor
    """

    def __init__(self):
        """
        Creates a new StandardImageProcessing object

        # Check that the cost was assigned
        >>> img_proc = StandardImageProcessing()
        >>> img_proc.cost
        0
        """
        # YOUR CODE GOES HERE #
        self.cost = 0
        self.free_calls = 0

    def negate(self, image):
        """
        Returns a negated copy of the given image

        # Check the expected cost
        >>> img_proc = StandardImageProcessing()
        >>> img_in = img_read_helper('img/square_32x32.png')
        >>> negated = img_proc.negate(img_in)
        >>> img_proc.get_cost()
        5

        # Check that negate works the same as in the parent class
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_negate.png')
        >>> img_negate = img_proc.negate(img)
        >>> img_negate.pixels == img_exp.pixels # Check negate output
        True
        """
        # YOUR CODE GOES HERE #
        if self.free_calls > 0:
            self.free_calls -= 1
        else: 
            self.cost += 5

        return super().negate(image)

    def grayscale(self, image):
        """
        Returns a grayscale copy of the given image

        """
        # YOUR CODE GOES HERE #
        if self.free_calls > 0:
            self.free_calls -= 1
        else:
            self.cost += 6

        return super().grayscale(image)

    def rotate_180(self, image):
        """
        Returns a rotated version of the given image
        """
        # YOUR CODE GOES HERE #
        if self.free_calls > 0:
            self.free_calls -= 1
        else: 
            self.cost += 10

        return super().rotate_180(image)

    def adjust_brightness(self, image, intensity):
        """
        Returns a new image with adjusted brightness level
        """
        # YOUR CODE GOES HERE #
        if self.free_calls > 0:
            self.free_calls -= 1
        else:
            self.cost += 1

        return super().adjust_brightness(image, intensity)


    def redeem_coupon(self, amount):
        """
        Makes the given number of methods calls free

        # Check that the cost does not change for a call to negate
        # when a coupon is redeemed
        >>> img_proc = StandardImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_proc.redeem_coupon(1)
        >>> img = img_proc.rotate_180(img)
        >>> img_proc.get_cost()
        0
        """
        # YOUR CODE GOES HERE #
        if not isinstance(amount, int):
            raise TypeError()
        if amount <= 0:
            raise ValueError()

        self.free_calls += amount



# Part 4: Premium Image Processing Methods #
class PremiumImageProcessing(ImageProcessingTemplate):
    """
    Represents a paid tier of an image processor
    """

    def __init__(self):
        """
        Creates a new PremiumImageProcessing object

        # Check the expected cost
        >>> img_proc = PremiumImageProcessing()
        >>> img_proc.get_cost()
        50
        """
        # YOUR CODE GOES HERE #
        self.cost = 50

    def pixelate(self, image, block_dim):
        """
        Returns a pixelated version of the image, where block_dim is the size of 
        the square blocks.

        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_pixelate = img_proc.pixelate(img, 4)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_pixelate.png')
        >>> img_exp.pixels == img_pixelate.pixels # Check pixelate output
        True
        >>> img_save_helper('img/out/test_image_32x32_pixelate.png', img_pixelate)
        """
        # YOUR CODE GOES HERE #
        pixels_copy = image.get_pixels()
        rows = len(pixels_copy)
        cols = len(pixels_copy[0])

        pixelate = image.get_pixels()

        # every loop is a block_dim * block_dim square / rectangle on edge
        for r in range(0, rows, block_dim):
            for c in range(0, cols, block_dim):
                r_sum = g_sum = b_sum = 0
                block_count = 0

                # all the pixels within the block (r, r+block_dim)
                for i in range(r, min(r+block_dim, rows)):
                    for j in range(c, min(c+block_dim, cols)):
                        r_sum += pixels_copy[i][j][0]
                        g_sum += pixels_copy[i][j][1]
                        b_sum += pixels_copy[i][j][2]
                        block_count += 1

                r_avg = r_sum // block_count
                g_avg = g_sum // block_count
                b_avg = b_sum // block_count

                for i in range(r, min(r+block_dim, rows)):
                    for j in range(c, min(c+block_dim, cols)):
                        pixelate[i][j] = [r_avg, g_avg, b_avg]

        return RGBImage(pixelate)

    def edge_highlight(self, image):
        """
        Returns a new image with the edges highlighted

        >>> img_proc = PremiumImageProcessing()
        >>> img = img_read_helper('img/test_image_32x32.png')
        >>> img_edge = img_proc.edge_highlight(img)
        >>> img_exp = img_read_helper('img/exp/test_image_32x32_edge.png')
        >>> img_exp.pixels == img_edge.pixels # Check edge_highlight output
        True
        >>> img_save_helper('img/out/test_image_32x32_edge.png', img_edge)
        """
        # YOUR CODE GOES HERE #
        copy_pixels = image.get_pixels()
        rows = image.num_rows
        cols = image.num_cols

        gray = [[(p[0] + p[1] + p[2]) // 3 for p in row] for row in copy_pixels]

        kernel = [
            [-1, -1, -1], 
            [-1, 8, -1], 
            [-1, -1, -1]]

        # every pixel as the center of kernel
        edges = []

        for row in range(rows):
            new_row = []

            for col in range(cols):
                edge_value = 0

                # in teh kernel matrix
                for kernel_row in range(3):
                    for kernel_col in range(3):

                        # according indices in the gray matrix
                        neighbor_row = row + kernel_row - 1
                        neighbor_col = col + kernel_col - 1

                        if (0 <= neighbor_row < rows) and \
                        (0 <= neighbor_col < cols):
                            weight = kernel[kernel_row][kernel_col]
                            edge_value += gray[neighbor_row][neighbor_col] * weight
                
                edge_value = max(0, min(255, edge_value))

                new_row.append(edge_value)

            edges.append(new_row)

        new_pixels = [
            [[n, n, n] for n in row]
            for row in edges]

        return RGBImage(new_pixels)





# Part 5: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Represents a simple KNNClassifier
    """

    def __init__(self, k_neighbors):
        """
        Creates a new KNN classifier object
        """
        # YOUR CODE GOES HERE #
        self.k_neighbors = k_neighbors
        self.data = None

    def fit(self, data):
        """
        Stores the given set of data and labels for later
        data: list of (RGMImage, 'label')
        """
        # YOUR CODE GOES HERE #
        if len(data) < self.k_neighbors:
            raise ValueError()

        self.data = data

    def distance(self, image1, image2):
        """
        Returns the distance between the given images

        >>> img1 = img_read_helper('img/steve.png')
        >>> img2 = img_read_helper('img/knn_test_img.png')
        >>> knn = ImageKNNClassifier(3)
        >>> knn.distance(img1, img2)
        15946.312896716909
        """
        # YOUR CODE GOES HERE #
        if not isinstance(image1, RGBImage):
            raise TypeError()
        if not isinstance(image2, RGBImage):
            raise TypeError()
        if image1.size() != image2.size():
            raise ValueError()

        pixels1 = image1.get_pixels()
        pixels2 = image2.get_pixels()

        return (
        sum(
            (pixels1[r][c][p] - pixels2[r][c][p]) ** 2
            for r in range(len(pixels1))
            for c in range(len(pixels1[0]))
            for p in range(3)
            )
        ) ** 0.5


    def vote(self, candidates):
        """
        Returns the most frequent label in the given list

        >>> knn = ImageKNNClassifier(3)
        >>> knn.vote(['label1', 'label2', 'label2', 'label2', 'label1'])
        'label2'
        """
        # YOUR CODE GOES HERE #
        counts = {}

        for label in candidates:
            if label not in counts:
                counts[label] = 0
            counts[label] += 1

        max_label = ''
        max_count = 0

        for label in counts:
            if counts[label] > max_count:
                max_count = counts[label]
                max_label = label

        return max_label


    def predict(self, image):
        """
        Predicts the label of the given image using the labels of
        the K closest neighbors to this image

        The test for this method is located in the knn_tests method below
        """
        # YOUR CODE GOES HERE #
        if self.data is None:
            raise ValueError

        img_label = [(self.distance(image, data_img[0]), data_img[-1])\
            for data_img in self.data]
        img_label.sort()
        
        k = self.k_neighbors
        candidates = [p[-1] for p in img_label][:k]

        return self.vote(candidates)


def knn_tests(test_img_path):
    """
    Function to run knn tests

    >>> knn_tests('img/knn_test_img.png')
    'nighttime'
    """
    # Read all of the sub-folder names in the knn_data folder
    # These will be treated as labels
    path = 'knn_data'
    data = []
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        # Ignore non-folder items
        if not os.path.isdir(label_path):
            continue
        # Read in each image in the sub-folder
        for img_file in os.listdir(label_path):
            train_img_path = os.path.join(label_path, img_file)
            img = img_read_helper(train_img_path)
            # Add the image object and the label to the dataset
            data.append((img, label))

    # Create a KNN-classifier using the dataset
    knn = ImageKNNClassifier(5)

    # Train the classifier by providing the dataset
    knn.fit(data)

    # Create an RGBImage object of the tested image
    test_img = img_read_helper(test_img_path)

    # Return the KNN's prediction
    predicted_label = knn.predict(test_img)
    return predicted_label
