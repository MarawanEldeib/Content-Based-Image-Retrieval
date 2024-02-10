## **Content-Based Image Retrieval**

### **Assignment for Digital Image and Video Processing**

This project explores **Content-Based Image Retrieval (CBIR)** techniques, utilizing **Convolutional Neural Networks (CNNs)** for image classification and retrieval. The study showcases the effectiveness of CNNs in achieving high accuracy and demonstrates their potential for future advancements in image retrieval systems.

---

### **Precision-Recall Curve**

Both precision and recall are crucial metrics for evaluating the performance of an image retrieval system. The precision-recall curve illustrates the trade-off between precision and recall for different threshold values.

![Precision-Recall Curve](https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/1f7fa104-df5d-49ad-85fa-c094d2ef6657)

---

### **Precision Curve**

The precision curve demonstrates the model's ability to return relevant images among all retrieved images.

![Precision Curve](https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/060f27c5-906f-4cba-a231-beedc1ca03f3)

---

### **Recall Curve**

The recall curve showcases how many relevant images the model can retrieve among all relevant images available.

![Recall Curve](https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/8a74ffab-d3e8-40cc-9f9f-e5693a679577)


---

### **Graphical User Interface (GUI)**

![GUI](https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/e4c7f25a-9fae-4e18-8548-2fb6362c1127)

---

### **Image Preprocessing**

<img src="https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/1199b7f1-82cb-421f-9ee2-ca75156447a8" alt="Noise Removal" width="300"/> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img src="https://github.com/MarawanEldeib/Content-Based-Image-Retrieval/assets/105850133/19aa0544-a72a-46be-9b75-cc1cc990e3ea" alt="Hole Filling" width="300"/>

**Techniques Used:**
- **Morphological operations** with 3x3 kernel for noise removal
- **Hole filling** to preserve structural integrity within images
- **Gaussian boundary smoothing** with a 5x5 kernel for edge refinement
- **Normalization** to standardize image sizes for uniform processing

---

### **Image Retrieval System**

**Key Components:**
- **Feature Extraction:** CNN model extracts feature vectors for each image.
- **Similarity Measurement:** Euclidean distance calculates similarity between feature vectors.
- **Ranking and Retrieval:** Images ranked by similarity to the query, ensuring relevant retrieval.

**Feature Extraction Using CNNs:**
- **Convolutional Layers:** Capturing features such as edges, textures, and patterns.
- **Pooling Layers:** Reducing spatial dimensions to prevent overfitting.
- **Fully Connected Layers:** Interpreting extracted features.
- **Output Layer:** Softmax activation for probabilistic class distribution.

**Model Training:**
- Convolution and Max Pooling layers with Adam optimizer.
- Categorical Cross Entropy loss function.
- Batch size of 32 and 5 epochs for training.

--- 

This README provides an overview of the Content-Based Image Retrieval project, detailing its various components and methodologies utilized. For further details, refer to the project's source code and documentation.
