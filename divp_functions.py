import tensorflow as tf
import numpy as np

IMG_SIZE = (256, 256)

def compute_distance(vec1, vec2):
    index1 = np.argmax(vec1)
    index2 = np.argmax(vec2)

    if index1 == index2:
        return np.linalg.norm(vec1 - vec2)
    else:
        return np.linalg.norm(np.sqrt(np.abs(vec1 - vec2)))

def rank_images_by_similarity(query_features, dataset_features):
    distances = [compute_distance(query_features, features) for features in dataset_features]
    ranked_indices = np.argsort(distances)
    return ranked_indices


def get_img_features(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=1)
    img = tf.image.resize(img, size=IMG_SIZE)
    img = tf.expand_dims(img, axis=0)
    img_feature = tf.nn.softmax(loaded_model.predict(img)[0])
    return img_feature